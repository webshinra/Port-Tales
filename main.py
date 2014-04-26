# Import
import pygame as pyg
from pygame import Surface, joystick
from pygame.sprite import Sprite, LayeredDirty, Group, LayeredUpdates
from fps import Fps
from constants import *

def clear_callback(surf, rect):
    surf.fill(WHITE, rect)

# Main function
def main():
    # Init module
    pyg.init()
    joystick.init()

    # Get controller
##    joysticks = [joystick.Joystick(x) for x in range(joystick.get_count())]
##    try:
##        controller = next(js for js in joysticks if "XBOX 360" in js.get_name())
##    except StopIteration:
##        raise RuntimeError("No XBOX 360 Controller detected")
##    if not controller.get_init():
##        controller.init()

    # Init window
    size_window = WINDOW_WIDTH,WINDOW_HEIGHT
    screen = pyg.display.set_mode(size_window)#, FULLSCREEN)
    ico = Surface((32,32))
    pyg.display.set_icon(ico)
    pyg.display.set_caption('Test')
    background = pyg.image.load('background.jpg').convert()
    background = pyg.transform.smoothscale(background, WINDOW_SIZE)
    background.fill(WHITE)
    screen.blit(background, background.get_rect())
    pyg.display.flip()

    # Imports
    from stage import Stage
    from tiles import Tile
    from player import Player

    # Init clock
    clock = pyg.time.Clock()

    # Init groups
    all_sprites = LayeredDirty()
    players = Group()
    Player.containers += players,
    Fps.containers += all_sprites,
    Tile.layer_container = all_sprites

    # Init element
    Stage("file.txt")
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

        # Clear sprites from screen
        all_sprites.clear(screen, background)

        # Update sprites
        all_sprites.update()

        # Draw sprites on screen
        dirty = all_sprites.draw(screen)

        # Update display
        pyg.display.update(dirty)

        # Frame rate control
        clock.tick(30)


# Call the "main" function if running this script
if __name__ == '__main__': main()
