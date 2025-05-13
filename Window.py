from WindowDataClass import WindowDataClass
import pygame


class Windows:
    def __init__(self, data: WindowDataClass):
        self.data = data
        self.display_surface = pygame.display.set_mode((self.data.width, self.data.height))
        self.surface_img = pygame.image.load(self.data.location)
        self.surface_img_rect = self.surface_img.get_rect()

    def new_window(self):
        self.surface_img_rect.topleft = self.data.position

    def blitting(self):
        self.display_surface.blit(self.surface_img, self.surface_img_rect)
