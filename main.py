import pygame
from Window import Windows
from game_objects import player

pygame.init()
clock = pygame.time.Clock()


running = True
window = False
game_window = Windows()

space_player = player.Player(game_window)

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
        space_player.blitting()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            space_player.move_right()

        if keys[pygame.K_LEFT]:
            space_player.move_left()

        if keys[pygame.K_UP]:
            space_player.move_up()

        if keys[pygame.K_DOWN]:
            space_player.move_down()

        space_player.clamping()
        game_window.fill_surface()
        space_player.blitting()
        clock.tick(60)

    pygame.display.flip()

pygame.quit()
