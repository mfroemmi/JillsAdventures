from random import randint
import pygame

class Objects():
    def __init__(self, set, screen, image):
        self.set = set
        self.screen = screen
        self.image = image

        self.image = pygame.image.load(image)
        self.rect_image = self.image.get_rect()
        self.rect_image.x = randint(150, 450)
        self.rect_image.y = randint(110, 550)

    def blit(self):
        self.screen.blit(self.image, self.rect_image)