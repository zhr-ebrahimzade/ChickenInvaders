import pygame

from .player_data_class import PlayerDataClass


class Player:
    def __init__(self, surface):
        self.data = PlayerDataClass(
            "./media/imgs/rocket-7339372_1280.png",
            (60, 80),
            (0, 0),
            2
        )
        self.surface = surface
        self.space_ship_img = pygame.image.load(self.data.image)
        self.space_ship_img = pygame.transform.scale(self.space_ship_img, self.data.rocket_size)
        self.space_ship_img_rect = self.space_ship_img.get_rect()
        self.space_ship_img_rect.centerx = surface.data.width // 2
        self.space_ship_img_rect.bottom = surface.data.height

    def blitting(self):
        self.surface.display_surface.blit(self.space_ship_img, self.space_ship_img_rect)

    def move_right(self):
        self.space_ship_img_rect.x += self.data.speed

    def move_left(self):
        self.space_ship_img_rect.x -= self.data.speed

    def move_up(self):
        self.space_ship_img_rect.y -= self.data.speed

    def move_down(self):
        self.space_ship_img_rect.y += self.data.speed

    def clamping(self):
        self.space_ship_img_rect.clamp_ip(self.surface.display_surface.get_rect())  # ensure player is inside screen

    # def move(self, direction):
    #     self.position += self.speed * direction
