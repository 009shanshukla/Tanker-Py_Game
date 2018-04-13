import pygame
import random
### will initialize the screen 
pygame.init()

### loading sounds
FireSound = pygame.mixer.Sound("fire.wav")
BombSound = pygame.mixer.Sound("bomb.wav")
pygame.mixer.music.load("game.wav")
pygame.mixer.music.play(-1)           ##-1 is for infinite loop of sound 

### color format (R, G, B)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

red = (200, 0, 0)
light_red = (255, 0, 0)

green = (34, 177, 76)
light_green = (0, 255, 0)

yellow = (200, 200, 0)
light_yellow = (255, 255, 0)

###Display Parameter
DisplayWidth = 800
DisplayHeight = 600
GroundHeight = 35

### Tank Parameter
TankWidth = 40
TankHeight = 20
WheelWidth = 5
TurretWidth = 5

### will give length and width to the screen
GameDisplay = pygame.display.set_mode((DisplayWidth, DisplayHeight))

### giving title to the scree
pygame.display.set_caption('Tanker')

### load image of icon
#icon = pygame.image.load('apple1.jpg')
#pygame.display.set_icon(icon)


### clock object initialization
clock = pygame.time.Clock()
FPS = 20    ## frame per second

### font object initialization using system font
SmallFont = pygame.font.SysFont("comicsansms", 25)
MedFont = pygame.font.SysFont("comicsansms", 50)
LargeFont = pygame.font.SysFont("comicsansms", 80)

###defining barrier
def barrier(BarrierX, BarrierHeight, BarrierWidth):
    pygame.draw.rect(GameDisplay, black, [BarrierX, DisplayHeight-BarrierHeight, BarrierWidth, BarrierHeight])


###defing explosion when hit something
def explosion(x, y, size = 50):

    pygame.mixer.Sound.play(BombSound)
    explode = True

    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        StartPoint = x, y
        ColorChoices = [yellow, green, light_green, red, light_red]
        magnitude = 1

        ### Blit 50 times on different types within a range randomly 
        while magnitude < size:
            
            ExplodingBlitX = x + random.randrange(-1*magnitude, magnitude)  
            ExplodingBlitY = y + random.randrange(-1*magnitude, magnitude)
            
            pygame.draw.circle(GameDisplay, ColorChoices[random.randrange(0,5)], (ExplodingBlitX, ExplodingBlitY),random.randrange(1,5))
            magnitude += 1
            
            pygame.display.update()
            clock.tick(100)

        explode = False

###Main tank
def tank(x, y, TurrepPos):

    ### 1st co-ordinate of turrep point (2nd will be (x, y)(tank upper circle)) and for rotation there will be 9 co-ordinates are available
    TurrepList = [
        (x-27, y-2),
        (x-26, y-5),
        (x - 25, y - 8),
        (x - 23, y - 12),
        (x - 20, y - 14),
        (x - 18, y - 15),
        (x - 15, y - 17),
        (x - 13, y - 19),
        (x - 11, y - 21)
    ]
    ### draw upper circle of tank
    pygame.draw.circle(GameDisplay, black, (x, y), int(TankHeight/2))
    ### draw rectangle of tank
    pygame.draw.rect(GameDisplay, black, (x-TankHeight, y, TankWidth, TankHeight))
    ### draw turrep of tank
    pygame.draw.line(GameDisplay, black, (x, y), TurrepList[TurrepPos], TurretWidth)
    ### draw 8 wheels of tank
    pygame.draw.circle(GameDisplay, black, (x-15, y+20), WheelWidth)
    pygame.draw.circle(GameDisplay, black, (x-10, y+20), WheelWidth)
    pygame.draw.circle(GameDisplay, black, (x-5, y+20), WheelWidth)
    pygame.draw.circle(GameDisplay, black, (x, y+20), WheelWidth)
    pygame.draw.circle(GameDisplay, black, (x+5, y+20), WheelWidth)
    pygame.draw.circle(GameDisplay, black, (x+10, y+20), WheelWidth)
    pygame.draw.circle(GameDisplay, black, (x+15, y+20), WheelWidth)
    pygame.draw.circle(GameDisplay, black, (x+15, y+20), WheelWidth)

    return TurrepList[TurrepPos]
        
###enemy tank
def EnemyTank(x, y, TurrepPos):

    ### 1st co-ordinate of turrep point (2nd will be (x, y)(tank upper circle)) and for rotation there will be 9 co-ordinates are available
    TurrepList = [
        (x + 27, y - 2),
        (x + 26, y - 5),
        (x + 25, y - 8),
        (x + 23, y - 12),
        (x + 20, y - 14),
        (x + 18, y - 15),
        (x + 15, y - 17),
        (x + 13, y - 19),
        (x + 11, y - 21)
    ]
    ### draw upper circle of tank
    pygame.draw.circle(GameDisplay, black, (x, y), int(TankHeight/2))
    ### draw rectangle of tank
    pygame.draw.rect(GameDisplay, black, (x-TankHeight, y, TankWidth, TankHeight))
    ### draw turrep of tank
    pygame.draw.line(GameDisplay, black, (x, y), TurrepList[TurrepPos], TurretWidth)
    ### draw 8 wheels of tank
    pygame.draw.circle(GameDisplay, black, (x-15, y+20), WheelWidth)
    pygame.draw.circle(GameDisplay, black, (x-10, y+20), WheelWidth)
    pygame.draw.circle(GameDisplay, black, (x-5, y+20), WheelWidth)
    pygame.draw.circle(GameDisplay, black, (x, y+20), WheelWidth)
    pygame.draw.circle(GameDisplay, black, (x+5, y+20), WheelWidth)
    pygame.draw.circle(GameDisplay, black, (x+10, y+20), WheelWidth)
    pygame.draw.circle(GameDisplay, black, (x+15, y+20), WheelWidth)
    pygame.draw.circle(GameDisplay, black, (x+15, y+20), WheelWidth)

    return TurrepList[TurrepPos]

    
###main tank firing
def fireshell(xy, TankX, TankY, CurrentPos, GunPower, BarrierX, BarrierHeight, BarrierWidth, EnemyTankX, EnemyTankY):

    pygame.mixer.Sound.play(FireSound)
    fire = True
    StartingShell = list(xy)
    damage = 0

    ### keep firing until not hit something     
    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        ###drawing fire 
        pygame.draw.circle(GameDisplay, red, (StartingShell[0], StartingShell[1]), 5)

        ### equation to find y and x moving co-ordinate of firing        
        StartingShell[0] -= (12 - CurrentPos)*2
        StartingShell[1] += int((((StartingShell[0]-xy[0])*0.015/(GunPower/50))**2) -(CurrentPos + CurrentPos/(12-CurrentPos)))

        ### if fire hit the ground 
        if StartingShell[1] > DisplayHeight-GroundHeight:
            HitX = int((StartingShell[0]*DisplayHeight-GroundHeight)/StartingShell[1])
            HitY = int(DisplayHeight-GroundHeight)
            explosion(HitX, HitY)
            
            if EnemyTankX + 10 > HitX > EnemyTankX - 10:
                damage = 25
            elif EnemyTankX + 15 > HitX > EnemyTankX - 15:
                damage = 18
            elif EnemyTankX + 25 > HitX > EnemyTankX - 25:
                damage = 10
            elif EnemyTankX + 35 > HitX > EnemyTankX - 35:
                damage = 5
            
            fire = False

        ### this condition will check if fire crosses the right of barrier
        CheckX1 = StartingShell[0] <= BarrierX + BarrierWidth
        ### this condition will check if fire is behind left of barrier          -> wall fire wall (if checkx1 and checkx2 true)
        CheckX2 = StartingShell[0] >= BarrierX
        ### this condition will check if fire crosses the ground 
        CheckY1 = StartingShell[1] >= DisplayHeight - BarrierHeight
        ### this condition will check if fire is above of y-display
        CheckY2 = StartingShell[1] <= DisplayHeight

        ### if hit the barrier
        if CheckX1 and CheckX2 and CheckY1 and CheckY2:
            explosion(StartingShell[0], StartingShell[1])
            fire = False
                        
        pygame.display.update()
        clock.tick(100)
    return damage

###enemy tank firing
def Efireshell(xy, TankX, TankY, CurrentPos, GunPower, BarrierX, BarrierHeight, BarrierWidth, PTankX, PTankY):

    pygame.mixer.Sound.play(FireSound)
    PowerFound = False
    CurrentPower = 1
    damage = 0

    ### getting power which will hit the player, from brute force 
    while not PowerFound:
        CurrentPower += 1
        if CurrentPower > 100:
            PowerFound = True

        fire = True
        StartingShell = list(xy)

        ### keep firing until not hit something     
        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            ###drawing fire 
            #pygame.draw.circle(GameDisplay, red, (StartingShell[0], StartingShell[1]), 5)

            ### equation to find y and x moving co-ordinate of firing
            StartingShell[0] += (12 - CurrentPos)*2

            StartingShell[1] += int((((StartingShell[0]-xy[0])*0.015/(CurrentPower/50))**2) -(CurrentPos + CurrentPos/(12-CurrentPos)))

            ### if fire hit the ground 
            if StartingShell[1] > DisplayHeight-GroundHeight:
                HitX = int((StartingShell[0]*DisplayHeight-GroundHeight)/StartingShell[1])
                HitY = int(DisplayHeight-GroundHeight)
                #explosion(HitX, HitY)
                if PTankX + 15 > HitX > PTankX - 15:
                    PowerFound = True
                
                fire = False

            ### this condition will check if fire crosses the right of barrier
            CheckX1 = StartingShell[0] <= BarrierX + BarrierWidth
            ### this condition will check if fire is behind left of barrier          -> wall fire wall (if checkx1 and checkx2 true)
            CheckX2 = StartingShell[0] >= BarrierX
            ### this condition will check if fire crosses the ground 
            CheckY1 = StartingShell[1] >= DisplayHeight - BarrierHeight
            ### this condition will check if fire is above of y-display
            CheckY2 = StartingShell[1] <= DisplayHeight

            ### if hit the barrier
            if CheckX1 and CheckX2 and CheckY1 and CheckY2:
                #explosion(StartingShell[0], StartingShell[1])
                fire = False
                            
    
    fire = True
    StartingShell = list(xy)

    ### keep firing until not hit something     
    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        ###drawing fire 
        pygame.draw.circle(GameDisplay, red, (StartingShell[0], StartingShell[1]), 5)

        ### equation to find y and x moving co-ordinate of firing
        StartingShell[0] += (12 - CurrentPos)*2

        GunPower = random.randrange(int(CurrentPower*0.90), int(CurrentPower*1.10))

        StartingShell[1] += int((((StartingShell[0]-xy[0])*0.015/(GunPower/50))**2) -(CurrentPos + CurrentPos/(12-CurrentPos)))

        ### if fire hit the ground 
        if StartingShell[1] > DisplayHeight-GroundHeight:
            HitX = int((StartingShell[0]*DisplayHeight-GroundHeight)/StartingShell[1])
            HitY = int(DisplayHeight-GroundHeight)
            if PTankX + 10 > HitX > PTankX - 10:
                damage = 25
            elif PTankX + 15 > HitX > PTankX - 15:
                damage = 18
            elif PTankX + 25 > HitX > PTankX - 25:
                damage = 10
            elif PTankX + 35 > HitX > PTankX - 35:
                damage = 5
            
            explosion(HitX, HitY)
            fire = False

        ### this condition will check if fire crosses the right of barrier
        CheckX1 = StartingShell[0] <= BarrierX + BarrierWidth
        ### this condition will check if fire is behind left of barrier          -> wall fire wall (if checkx1 and checkx2 true)
        CheckX2 = StartingShell[0] >= BarrierX
        ### this condition will check if fire crosses the ground 
        CheckY1 = StartingShell[1] >= DisplayHeight - BarrierHeight
        ### this condition will check if fire is above of y-display
        CheckY2 = StartingShell[1] <= DisplayHeight

        ### if hit the barrier
        if CheckX1 and CheckX2 and CheckY1 and CheckY2:
            explosion(StartingShell[0], StartingShell[1])
            fire = False
                        
        pygame.display.update()
        clock.tick(100)

    return damage




###draw power score above middle of the screen
def power(level):
    text = SmallFont.render("Power: "+str(level)+"%", True, black)
    GameDisplay.blit(text, [DisplayWidth/2, 0])


def HealthBars(PlayerHealth, EnemyHealth):
    
    if PlayerHealth > 75:
        PlayerHealthColor = green
    elif PlayerHealth > 50:
        PlayerHealthColor = yellow
    else:
        PlayerHealthColor = red

    if EnemyHealth > 75:
        EnemyHealthColor = green
    elif EnemyHealth > 50:
        EnemyHealthColor = yellow
    else:
        EnemyHealthColor = red

    pygame.draw.rect(GameDisplay, EnemyHealthColor, (20, 25, EnemyHealth, 25))
    pygame.draw.rect(GameDisplay, PlayerHealthColor, (680, 25, PlayerHealth, 25))


### looping all events
def GameLoop():
    ### Game variables
    GameExit = False
    GameOver = False

    ###main tank
    TankX = int(DisplayWidth*0.9)            #(90%right, 90% down the screen)
    TankY = int(DisplayHeight*0.9)    
    TankMove = 0
    PlayerHealth = 100
    damage = 0

    ###enemy tank
    EnemyTankX = int(DisplayWidth*0.1)
    EnemyTankY = int(DisplayHeight*0.9)
    EnemyHealth = 100
    EnemyDamage = 0
    
    TurrepPos = 0
    CurrentTurrep = 0
    
    FirePower = 50
    ChangePower = 0
    
    BarrierWidth = 50
    BarrierX = (DisplayWidth / 2) + random.randint(-0.1 * DisplayWidth, 0.1 * DisplayWidth)
    BarrierHeight = random.randrange(DisplayHeight * 0.1, DisplayHeight * 0.6)

    while not GameExit:
        
        if GameOver == True:
            message_to_screen("Game Over", red, -50,
                              FontSize="large")  ### -50 is telling y-displacement from the centre of text
            message_to_screen("Press c to continue or q to quit", black, 50, FontSize="small")
            pygame.display.update()

        while GameOver == True:
            ### if c ,q our quit is pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GameExit = True
                    GameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        GameExit = True
                        GameOver = False
                    if event.key == pygame.K_c:
                        GameLoop()

        ### if one of arrow keys or quit is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameExit = True

            ### if an key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    TankMove = -5
                elif event.key == pygame.K_RIGHT:
                    TankMove = 5
                elif event.key == pygame.K_UP:
                    TurrepPos = 1
                elif event.key == pygame.K_DOWN:
                    TurrepPos = -1
                elif event.key == pygame.K_p:
                    pause()
                elif event.key == pygame.K_a:
                    ChangePower = 1
                    
                elif event.key == pygame.K_d:
                    ChangePower = -1
                elif event.key == pygame.K_SPACE:
                    EnemyDamage = fireshell(Gunpos, TankX, TankY, CurrentTurrep, FirePower, BarrierX, BarrierHeight, BarrierWidth, EnemyTankX, EnemyTankY)
                    damage = Efireshell(EnemyGunPos, EnemyTankX, EnemyTankY, 8, 50, BarrierX, BarrierHeight, BarrierWidth, TankX, TankY)
                    PlayerHealth -= damage
                    EnemyHealth -= EnemyDamage

                    PossibleMovements = ['r', 'f']
                    MoveIndex = random.randrange(0, 2)

                    for x in range(random.randrange(0, 10)):
                        if DisplayWidth * 0.3 > EnemyTankX > DisplayWidth * 0.03:
                            if PossibleMovements[MoveIndex] == 'r':
                                EnemyTankX += 5
                            if PossibleMovements[MoveIndex] == 'l':
                                EnemyTankX -= 5

                            GameDisplay.fill(white)

                            HealthBars(PlayerHealth, EnemyHealth)
                            Gunpos = tank(TankX, TankY, CurrentTurrep)
                            EnemyGunPos = EnemyTank(EnemyTankX, EnemyTankY, 8)

                            FirePower += ChangePower
                            power(FirePower)

                            barrier(BarrierX, BarrierHeight, BarrierWidth)
                            ###fill the green ground
                            GameDisplay.fill(green, rect = [0, DisplayHeight-GroundHeight, DisplayWidth, GroundHeight])

                            ### will update the whole display screen
                            pygame.display.update()

                            clock.tick(FPS)

                            
                        


            ### if key is unpressed        
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    TankMove = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                     TurrepPos = 0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    ChangePower = 0


        TankX += TankMove
        CurrentTurrep += TurrepPos

        ### as turreplist only has 8 rotations
        if CurrentTurrep > 8:
            CurrentTurrep = 8
        elif CurrentTurrep < 0:
            CurrentTurrep = 0

        ### if this is the case then from upper side tank will move 5 unit left and from this case it will move 5 unit right, means cancel out (tank will look stable) 
        if TankX - (TankWidth/2) < BarrierX + BarrierWidth:
            TankX += 5

        GameDisplay.fill(white)

        HealthBars(PlayerHealth, EnemyHealth)
        Gunpos = tank(TankX, TankY, CurrentTurrep)
        EnemyGunPos = EnemyTank(EnemyTankX, EnemyTankY, 8)

        FirePower += ChangePower
        if FirePower > 100:
            FirePower = 100
        elif FirePower < 0:
            FirePower = 0
        power(FirePower)

        barrier(BarrierX, BarrierHeight, BarrierWidth)
        ###fill the green ground
        GameDisplay.fill(green, rect = [0, DisplayHeight-GroundHeight, DisplayWidth, GroundHeight])

        ### will update the whole display screen
        pygame.display.update()
        
        if PlayerHealth <= 0:
            GameOverScreen()

        if EnemyHealth <= 0:
            YouWinScreen()
            

        ### give freeze time frame per seconds
        clock.tick(FPS)

    ### quitting from pygame
    pygame.quit()

    ### quitting from program
    quit()




### control screen of game
def GameControl():
	cntrl = True

	while cntrl:

		### events(Press c to enter or q to exit) and direct exit x
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		GameDisplay.fill(white)
		message_to_screen("Game Controls !!", red, -100, "medium")
		message_to_screen("Fire: Spacebar ", black, -60)
		message_to_screen("Move Tanker: left, right  ", black, -20)
		message_to_screen("Move Turret: up, down", black, 20)
		message_to_screen("pause: press p", blue, 60)

		button("Play", 150, 500, 100, 50, green, light_green, action= "play")
		#button("Controls", 350, 500, 100, 50, yellow, light_yellow, action= "controls")
		button("Quit", 550, 500, 100, 50, red, light_red, action= "quit")
		pygame.display.update()
		clock.tick(15)

### function is used to get surface and inside rectangle of the whole text
def text_objects(text, color, FontSize):
	if FontSize == "small":
		TextSurface = SmallFont.render(text, True, color)
	elif FontSize == "medium":
		TextSurface = MedFont.render(text, True, color)
	elif FontSize == "large":
		TextSurface = LargeFont.render(text, True, color)		
	return TextSurface, TextSurface.get_rect()

### defining text on buttons
def text_button(msg, color, buttonX, buttonY, bWidth, bHeight, size = "small"):
	TextSurface, TextRect = text_objects(msg, color, size)
	TextRect.center = (buttonX + (bWidth/2)), (buttonY + (bHeight/2))
	GameDisplay.blit(TextSurface, TextRect)

### defining buttons
def button(msg, buttonX, buttonY, bWidth, bHeight, inactive_color, active_color, action = None):
	cur = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if buttonX+bWidth > cur[0] > buttonX and buttonY+bHeight > cur[1] > buttonY:
		pygame.draw.rect(GameDisplay, active_color, (buttonX, buttonY, bWidth, bHeight))
		if click[0] == 1 and action != None:
			if action == "play":
				GameLoop()
			if action == "controls":
				GameControl()
			if action == "quit":
				pygame.quit()
				quit()
	else:
		pygame.draw.rect(GameDisplay, inactive_color, (buttonX, buttonY, bWidth, bHeight))

	text_button(msg, black, buttonX, buttonY, bWidth, bHeight)

### message that needs to be printed on screen
def message_to_screen(msg, color, y_displace = 0, FontSize = "small"):
	TextSurface, TextRect = text_objects(msg, color, FontSize)
	TextRect.center = (DisplayWidth/2), (DisplayHeight/2) + y_displace         ### y_dispalce is used to get y displacement from centre
	GameDisplay.blit(TextSurface, TextRect)

### score printing
def score(score):
	text = SmallFont.render("Score: "+ str(score), True, black)
	GameDisplay.blit(text, [0, 0])
					
### pausing the screen
def pause():
	paused = True
	message_to_screen("Paused", red, -100, "large")
	message_to_screen("Press c to continue or q to quit", black, -20)

	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
				elif event.key == pygame.K_c:
					paused = False

		pygame.display.update()					


### game over screen of game
def GameOverScreen():
	over = True

	while over:

		### events(Press c to enter or q to exit) and direct exit x
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
				if event.key == pygame.K_c:
					over = False

		GameDisplay.fill(white)
		message_to_screen("You Died!!", red, -100, "medium")
		message_to_screen("Game Over ", black, -60)
		# message_to_screen("Press c to enter, Press p to pause or q to exit", blue, 100)

		button("Play Again", 150, 500, 150, 50, green, light_green, action= "play")
		button("Controls", 350, 500, 100, 50, yellow, light_yellow, action= "controls")
		button("Quit", 550, 500, 100, 50, red, light_red, action= "quit")
		pygame.display.update()
		clock.tick(15)

### You Win screen of game
def YouWinScreen():
	win = True

	while win:

		### events(Press c to enter or q to exit) and direct exit x
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
				if event.key == pygame.K_c:
					win = False

		GameDisplay.fill(white)
		message_to_screen("You Win!!", red, -100, "medium")
		message_to_screen("Congratulations ", black, -60)
		# message_to_screen("Press c to enter, Press p to pause or q to exit", blue, 100)

		button("Play Again", 150, 500, 150, 50, green, light_green, action= "play")
		button("Controls", 350, 500, 100, 50, yellow, light_yellow, action= "controls")
		button("Quit", 550, 500, 100, 50, red, light_red, action= "quit")
		pygame.display.update()
		clock.tick(15)

### Win screen of game
def GameIntro():
	intro = True

	while intro:

		### events(Press c to enter or q to exit) and direct exit x
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
				if event.key == pygame.K_c:
					intro = False

		GameDisplay.fill(white)
		message_to_screen("WELCOME TO Tanker!!", red, -100, "medium")
		message_to_screen("There is a tanker which helps you to kill enemies ", black, -60)
		message_to_screen("Kill more enemies and score more ", black, -20)
		message_to_screen("Kill them, before they kill you", black, 20)
		# message_to_screen("Press c to enter, Press p to pause or q to exit", blue, 100)

		button("Play", 150, 500, 100, 50, green, light_green, action= "play")
		button("Controls", 350, 500, 100, 50, yellow, light_yellow, action= "controls")
		button("Quit", 550, 500, 100, 50, red, light_red, action= "quit")
		pygame.display.update()
		clock.tick(15)

GameIntro()
GameLoop()
  
