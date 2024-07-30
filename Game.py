import pygame
import pygame as py
from Player import player
CLOCK = pygame.time.Clock()
WIDTH = 1280
HEIGHT = 720
class game:
    def __init__(self):

        self.screen = py.display.set_mode((WIDTH, HEIGHT))
        self.player = player("GUSTAVE")
        self.background_image = py.image.load("images/mario_bg.jpg")
        self.background_image = py.transform.scale(self.background_image, (WIDTH, HEIGHT))
        py.display.set_caption("Jeu de fou dinguo")

    def run(self):
        freq = 60
        running = True
        while running:
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False
                if event.type == py.KEYDOWN:
                    if event.key == py.K_UP:
                        jumping = True
                        if jumping:
                            self.player.jump()
                        self.screen.blit(self.player.frame_0, (self.player.rect.x, self.player.rect.y))
            if self.player.rect.y < 540:
                self.player.jump()
                self.screen.blit(self.player.frame_0, (self.player.rect.x, self.player.rect.y))

            keys = py.key.get_pressed()
            if keys[py.K_RIGHT]:
                self.player.move_right()
            if keys[py.K_LEFT]:
                self.player.move_left()
            if keys[py.K_UP]:
                pass




            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.player.frame_0, (self.player.rect.x, self.player.rect.y))
            CLOCK.tick(freq)
            py.display.flip()
        py.quit()