import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = "C:/Python36/tcl/tcl8.6"
os.environ['TK_LIBRARY'] = "C:/Python36/tcl/tk8.6"

executables = [cx_Freeze.Executable("init.py")]

cx_Freeze.setup(
        name = "Tanker Py_Game",
        options = {"build.exe":{"packages":["pygame"], "includee_files":["bomb.wav", "fire.wav", "game.wav"]}},
        description = "Tanker Py_Game tut",
        executables = executables

        )
