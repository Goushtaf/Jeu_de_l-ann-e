import pygame as py
import Game
import Player
py.display.init()
sprite_sheet_image = py.image.load("images/DinoSprites - tard.png")
def get_image(sheet, frame, width, height, scale, colour):
    image = py.Surface((width, height))
    image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
    image = py.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(colour)

    return image

frame_0 = get_image(sprite_sheet_image, 0, 24, 24, 3, (0,0,0))

#aaaaaaaaaaa