#!/usr/bin/python2

# Import
import pygame as pyg
from Common import TimeControl, reset_screen, play_music, gen_stage_screen
from Constants import *
import os


# Main function
def main():

    # Init module
    pyg.init()

    # Init screen
    reset_screen(INSTRUCTION_FILE)

    # Play music
    play_music(MUSIC_FILE, volume=00.0)

    # Load ressources
    with TimeControl(INSTRUCTION_TIME):
        from Map import Map

    # Loop infinitely
    while True:

        # Loop over levels
        for i in xrange(1, NB_LEVELS+1):

            # Loop over game overs
            while True:

                # Print stage screen
                with TimeControl(STAGE_TIME):
                    gen_stage_screen(i)

                # Create map
                mp = Map(MAP_FORMAT.format(i))

                # Main loop
                win = mp.view.reactor_loop()

                # Test victory
                if win: break

                # Game over screen
                with TimeControl(GAMEOVER_TIME):
                    reset_screen(GAMEOVER_FILE)

        # End screen
        with TimeControl(ENDSCREEN_TIME):
            reset_screen(ENDSCREEN_FILE)

        # Credits screen
        with TimeControl(CREDITS_TIME):
            reset_screen(CREDITS_FILE)

        with TimeControl(INSTRUCTION_TIME):
            reset_screen(INSTRUCTION_FILE)

    # Quit
    pyg.quit()


# Call the main function
if __name__ == '__main__': main()
