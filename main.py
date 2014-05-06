#!/usr/bin/python2

# this file is part of Port Tales
# Copyright (C) 2014
# Yann Asset <shinra@electric-dragons.org>,
# Vincent Michel <vxgmichel@gmail.com>,
# Cyril Savary <cyrilsavary42@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Import
import pygame as pyg
from Common import TimeControl, reset_screen, play_music, gen_stage_screen
from Constants import *
import os


# Main function
def main():

    # Init module
    pyg.init()
    pyg.mouse.set_visible(False)

    # Init screen
    reset_screen(INSTRUCTION_FILE)

    # Play music
    play_music(MUSIC_FILE, volume=VOLUME)

    # Load ressources
    with TimeControl(FIRST_INSTRUCTION_TIME):
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
                mp = Map(MAP_FORMAT.format(i), i)

                # Main loop
                win, reset = mp.view.reactor_loop()

                # Test victory
                if win: break

                # Game over screen
                if not reset:
                    with TimeControl(GAMEOVER_TIME):
                        reset_screen(GAMEOVER_FILE)

            # Hard Reset
            #if hard_reset: break

        if not reset:
            # End screen
            with TimeControl(ENDSCREEN_TIME):
                reset_screen(ENDSCREEN_FILE)

            # Credits screen
            with TimeControl(CREDITS_TIME):
                reset_screen(CREDITS_FILE)

        # Instruction screen
        with TimeControl(INSTRUCTION_TIME):
            reset_screen(INSTRUCTION_FILE)

    # Quit
    pyg.quit()


# Call the main function
if __name__ == '__main__': main()
