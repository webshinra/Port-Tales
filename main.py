#!/usr/bin/python2
# Import
import pygame as pyg
from Common import reset_screen, play_music
from Constants import *
import os



# Main function
def main():
    # Init module
    pyg.init()

    # Init screen
    reset_screen()

    # Sound
    play_music(MUSIC_FILE, 0.5)

    # Imports
    from Map import Map

    for i in xrange(1, 9):
        # Create map
        filename = os.path.join(MAP_DIR, MAP_FORMAT.format(i))
        mp = Map(filename)

        # Main loop
        mp.view.reactor_loop()

    pyg.quit()


 # Call the "main" function if running this script
if __name__ == '__main__': main()
