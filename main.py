# Import
import pygame as pyg
from pygame import Surface, joystick
from constants import *

def clear_callback(surf, rect):
    surf.fill(WHITE, rect)

# Main function
def main():
    # Init module
    pyg.init()
    joystick.init()
    # Imports
    from Map import Map
    # Init element, read the map, build the MapView
    m = Map("file.txt")
    Fps(clock)

    # Infinite loop
    while True:
        # Get input
        for ev in pyg.event.get():
            if ev.type == pyg.QUIT or \
                (ev.type == pyg.KEYDOWN and ev.key == pyg.K_ESCAPE):
                    pyg.quit()
                    return

        # Do something
        #next(iter(players)).set_input()
        
        ActionHandeler.pushInput(input);

        # Clear sprites from screen
        m.vue.all_sprites.clear(screen, background)

        # Update sprites
        m.vue.all_sprites.update()

        # Draw sprites on screen
        dirty = all_sprites.draw(screen)

        # Update display
        pyg.display.update(dirty)

        # Frame rate control
        clock.tick(30)


 # Call the "main" function if running this script
if __name__ == '__main__': main()
