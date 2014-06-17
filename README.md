Port-Tales
==========

A 2-players cooperative puzzle mainly developed in 48h during the StunJam 2014. 
Little wordless tale about octets.

![Alt text](/data/screenshot.png?raw=true "ScreenShot")

# Windows executable

This file already includes the sources, python and pygame:
https://sourceforge.net/projects/porttales/files/latest/download

# Requirements

To run the game from the sources, these programs are needed:

 - Python 2.7 32 bits
 - Pygame 1.9 32 bits

# Running it

To run the game from the sources, launch PortTales.pyw

# Bundling it

To create a single windows executable, run: pyinstaller PortTales.spec

# Keyboard mapping 

Player 1 : 	

- Direction : Z, Q, S, D or W, A, S, D
- Action :	Space

Player 2 : 	

- Direction : UP, LEFT, DOWN, RIGHT
- Action : 	Enter

Toggle fullscreen : F

Reset stage : 		R

# XBOX 360 controller mapping 

Plug the controller(s) before you run the game

- Direction : Stick or Hat
- Validate : 	A, B or X
- Reset stage: 	Y

# Improving it

Port tales is under the GPLv3, the only file which is not is the music, licensing of it being unknown.
You can build your own level using the free software «tiled» and add them to the data/maps directory.

# Credits

The game comes from the joint work of 3 persons:

- Vincent Michel as the main developer
- Cyril Savary as the level designer
- Yann Asset as a 3D artist (and a little application architecture).
