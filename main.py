# Import
import pygame as pyg
import os

MAP_DIR = "maps"
MAP_FORMAT = "map{}.txt"
MAP_ID = 3

# Main function
def main():
    # Init module
    pyg.init()

    # Imports
    from Map import Map

    # Create map
    filename = os.path.join(MAP_DIR, MAP_FORMAT.format(MAP_ID))
    mp = Map(filename)

    # Main loop
    mp.view.reactor_loop()


 # Call the "main" function if running this script
if __name__ == '__main__': main()
