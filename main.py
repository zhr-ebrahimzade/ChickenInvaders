import pygame
from window_data_class import WindowDataClass
from window import Windows

pygame.init()# 2. CREATE A PYTHON FILE CONTAINING THE WINDOW CLASS AND USE IT IN UR MAIN SCRIPT
clock = pygame.time.Clock()


running = True
window = False
game_window = Windows()


ROCKET_SIZE = (60, 80)
space_ship_img = pygame.image.load("./media/imgs/rocket-7339372_1280.png")
space_ship_img = pygame.transform.scale(space_ship_img, ROCKET_SIZE)
space_ship_img_rect = space_ship_img.get_rect()
space_ship_img_rect.centerx = game_window.data.width // 2
space_ship_img_rect.bottom = game_window.data.height

while running:
    for event in pygame.event.get():
        pygame.display.set_caption(game_window.data.title)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            window = True
    if not window:
        game_window.blitting()

    if window:
        game_window.fill_surface()
        game_window.display_surface.blit(space_ship_img, space_ship_img_rect)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            space_ship_img_rect.x += 2
        if keys[pygame.K_LEFT]:
            space_ship_img_rect.x -= 2
        if keys[pygame.K_UP]:
            space_ship_img_rect.y -= 2
        if keys[pygame.K_DOWN]:
            space_ship_img_rect.y += 2
        space_ship_img_rect.clamp_ip(game_window.display_surface.get_rect())  # ensure player is inside screen
        game_window.fill_surface()
        game_window.display_surface.blit(space_ship_img, space_ship_img_rect)
        clock.tick(60)

    # updating the display
    pygame.display.flip()

pygame.quit()
