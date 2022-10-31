#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in October 2022
# A file for the "Space Aliens" game for CiruitPython

import stage
import ugame


def game_scene():
    # A function for the Game Scene

    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    background = stage.Grid(image_bank_background, 10, 8)
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    game = stage.Stage(ugame.display, 60)
    game.layers = [ship] + [background]
    game.render_block()

    while True:
        # User inputs

        # Game logic

        # Redraw sprites
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()
