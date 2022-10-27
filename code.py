#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in October 2022
# A file for the "Space Aliens" game for CiruitPython


import ugame
import stage

def game_scene():
    # Finds if a number is associated with a month

    image_blank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    background = stage.Grid("image_blank_background, 10, 8")
    game = stage.Stage(ugame.display, 60)
    game.layers = [background]
    game.render_block()


if __name__ == "__main__":
    game_scene()
