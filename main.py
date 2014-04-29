#!/usr/bin/python2

# Import
import pygame as pyg
from Common import TimeControl, reset_screen, play_music
from Constants import *
import os


# Main function
def main():

    # Init module
    pyg.init()

    # Init screen
    reset_screen(INSTRUCTION_FILE)

    # Play music
    play_music(MUSIC_FILE, volume=50.0)

    # Load ressources
    with TimeControl(INSTRUCTION_TIME):
        from Map import Map

    for i in xrange(1, 9):
        # Create map
        mp = Map(MAP_FORMAT.format(i))

        # Main loop
        mp.view.reactor_loop()

    # Quit
    pyg.quit()


# Call the main function
if __name__ == '__main__': main()
