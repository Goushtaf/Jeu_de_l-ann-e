import pygame as py

PLAYER_HEIGHT = 100
PLAYER_WIDTH = 100
from Sprites import get_image
class player:
    def __init__(self, name:str = 'Maman'):
        self.name = name
        self.sprite_sheet = py.image.load("images/DinoSprites - tard.png")
        self.frame_0 = get_image(self.sprite_sheet, 5, 24, 24, 3, (0,0,0))
        self.rect = self.frame_0.get_rect()
        self.rect.y = 540
        self.velocity = 5
        self.gravity = 1
        self.jump_height = 20
        self.y_velocity = self.jump_height

    def move_right(self):
        self.rect.x += self.velocity
        print(self.rect.x)
    def move_left(self):
        self.rect.x -= self.velocity
        print(self.rect.x)
    def revert_image(self):
        self.image = py.transform.flip(self.image, 1, 0)

    def jump(self):
        self.rect.y -= self.y_velocity
        self.y_velocity -= self.gravity
        if self.y_velocity < -self.jump_height:
            self.y_velocity = self.jump_height

    # aaaaaaaaaaazug8uzb