from window_data_class import WindowDataClass
import pygame


class Windows:
    def __init__(self):
        self.data = WindowDataClass(
            500,
            600,
            "Welcome to Chicken Invaders",
            "./media/imgs/astronaut.jpg",
            (0, 0),
        )

        self.display_surface = pygame.display.set_mode((self.data.width, self.data.height))
        self.surface_img = pygame.image.load(self.data.location)
        self.surface_img_rect = self.surface_img.get_rect()

    def blitting(self):
        self.display_surface.blit(self.surface_img, self.surface_img_rect)

    def fill_surface(self):
        self.display_surface.fill((0, 0, 0))
