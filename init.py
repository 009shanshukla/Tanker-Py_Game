import pygame

### will initialize the screen 
pygame.init()

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

DisplayWidth = 800
DisplayHeight = 600

### Tank Parameter
TankX = int(DisplayWidth * 0.9)
TankY = int(DisplayHeight*0.9)
TankWidth = 40
TankHeight = 20
WheelWidth = 5
TurretWidth = 5

### will give length and width to the screen
GameDisplay = pygame.display.set_mode((DisplayWidth, DisplayHeight))

### giving title to the scree
pygame.display.set_caption('Tanker')

### load image of icon, sanke head and apple
#icon = pygame.image.load('apple1.jpg')
#pygame.display.set_icon(icon)

#img = pygame.image.load('snakeHead.jpg')
#appleimg = pygame.image.load('apple1.jpg')
#snakebody = pygame.image.load('Body.jpg')

### clock object initialization
clock = pygame.time.Clock()
FPS = 20    ## frame per second

### font object initialization using system font
SmallFont = pygame.font.SysFont("comicsansms", 25)
MedFont = pygame.font.SysFont("comicsansms", 50)
LargeFont = pygame.font.SysFont("comicsansms", 80)

### drawing tank
def tank(x, y):
    pygame.draw.circle(GameDisplay, black, (x, y), int(TankHeight/2))
    pygame.draw.rect(GameDisplay, black, (x-TankHeight, y, TankWidth, TankHeight))
    pygame.draw.line(GameDisplay, black, (x, y), (x-10, y-20), TurretWidth)
    
    pygame.draw.circle(GameDisplay, black, (x-15, y+20), WheelWidth)
    pygame.draw.circle(GameDisplay, black, (x-10, y+20), WheelWidth)
    pygame.draw.circle(GameDisplay, black, (x-5, y+20), WheelWidth)
    pygame.draw.circle(GameDisplay, black, (x, y+20), WheelWidth)
    pygame.draw.circle(GameDisplay, black, (x+5, y+20), WheelWidth)
    pygame.draw.circle(GameDisplay, black, (x+10, y+20), WheelWidth)
    pygame.draw.circle(GameDisplay, black, (x+15, y+20), WheelWidth)
    pygame.draw.circle(GameDisplay, black, (x+15, y+20), WheelWidth)
    

### looping all events
def GameLoop():
	### Game variables
	GameExit = False
	GameOver = False

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

			### if an arrow key is pressed
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					pass
				elif event.key == pygame.K_RIGHT:
					pass
				elif event.key == pygame.K_UP:
					pass
				elif event.key == pygame.K_DOWN:
					pass
				elif event.key == pygame.K_p:
					pause()

		GameDisplay.fill(white)
		tank(TankX, TankY)


		### will update the whole display screen
		pygame.display.update()

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


### opening screen of game
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
