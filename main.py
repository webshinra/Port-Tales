# Import
import pygame as pyg

# Main function
def main():
    # Init module
    pyg.init()

    # Imports
    from Map import Map

    # Create map
    mp = Map("file.txt")

    # Main loop
    mp.view.reactor_loop()


 # Call the "main" function if running this script
if __name__ == '__main__': main()
