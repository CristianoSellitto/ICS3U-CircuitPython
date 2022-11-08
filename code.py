#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in October 2022
# A file for the "Space Aliens" game for CiruitPython

import stage
import ugame
import constants


def game_scene():
    # A function for the Game Scene

    # Image Banks
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Static buttons
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # Sprites Variables
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))
    alien = stage.Sprite(
        image_bank_sprites,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )

    # Sound
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [ship] + [alien] + [background]
    game.render_block()

    while True:
        # User inputs
        keys = ugame.buttons.get_pressed()

        # A Button
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        # B Button
        if keys & ugame.K_X != 0:
            pass
        # Start Button
        if keys & ugame.K_START != 0:
            print("Start")
        # Select Button
        if keys & ugame.K_SELECT != 0:
            print("Select")
        # Right D-Pad
        if keys & ugame.K_RIGHT != 0:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move((ship.x + constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        # Left D-Pad
        if keys & ugame.K_LEFT != 0:
            if ship.x >= 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(0, ship.y)
        # Up D-Pad
        if keys & ugame.K_UP != 0:
            pass
        # Down D-Pad
        if keys & ugame.K_DOWN != 0:
            pass

        # Game logic
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # Redraw sprites
        game.render_sprites([ship] + [alien])
        game.tick()


if __name__ == "__main__":
    game_scene()
