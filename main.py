# Import
import pygame as pyg
import os

MAP_DIR = "maps"
MAP_FORMAT = "map{}.txt"
MAP_ID = 1


# Main function
def main():
    # Init module
    pyg.init()

    # Sound
    pyg.mixer.init()
    sound_file = "son/puzz.ogg"
    sound = pyg.mixer.Sound(sound_file)
    sound.set_volume(0.5)
    channel = sound.play()

    # Imports
    from Map import Map

    for i in xrange(1, 4):
        # Create map
        filename = os.path.join(MAP_DIR, MAP_FORMAT.format(i))
        mp = Map(filename)

        # Main loop
        mp.view.reactor_loop()

    pyg.quit()


 # Call the "main" function if running this script
if __name__ == '__main__': main()
