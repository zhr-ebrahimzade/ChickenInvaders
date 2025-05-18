import pygame
from WindowDataClass import WindowDataClass
from Window import Windows

pygame.init()

# 2. CREATE A PYTHON FILE CONTAINING THE WINDOW CLASS AND USE IT IN UR MAIN SCRIPT

main_surface_dataclass = WindowDataClass(500, 600, "Welcome to Chicken Invaders", ".\\media\\imgs\\astronaut.jpg",
                                         (0, 0))
game_surface_dataclass = WindowDataClass(500, 600)

space_surface = pygame.display.set_mode((500, 600))

clock = pygame.time.Clock()

# Load GIF frames
frames = []
for i in range(1, 75):
    frames.append(pygame.image.load(f".\\media\\imgs\\frames_space\\{i}.gif"))
frame_index = 0

# USE SPACE BETWEEN VARNAME AND VARVALUE
# CREATE AN "ENTITIES" DIRECTORY. MOVE ALL IN GAME OBJECTS INTO SAID DIR.
ROCKET_SIZE = (60, 80)
space_ship_img = pygame.image.load(".\\media\\imgs\\rocket-7339372_1280.png")
space_ship_img = pygame.transform.scale(space_ship_img, ROCKET_SIZE)
space_ship_img_rect = space_ship_img.get_rect()
space_ship_img_rect.centerx = game_surface_dataclass.width // 2  # Center horizontally
space_ship_img_rect.bottom = game_surface_dataclass.height  # Place at the bottom

print(f"Rect before scaling: {space_ship_img.get_rect()}")
print(f"Rect after positioning: {space_ship_img_rect}")

# Moving the spaceship

player_pos = game_surface_dataclass

running = True
window = False

main_surface = Windows(main_surface_dataclass)
main_surface.new_window()

while running:
    for event in pygame.event.get():
        pygame.display.set_caption(main_surface_dataclass.title)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            window = True
    if not window:
        main_surface.blitting()

    if window:
        space_surface.fill((0, 0, 0))
        # # Display current frame
        # space_surface.blit(frames[frame_index], (0, 0))
        # # updating frame index
        # frame_index = (frame_index + 1) % len(frames)
        # # Adjust speed (higher = slower animation)
        # clock.tick(10)
        space_surface.blit(space_ship_img, space_ship_img_rect)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            space_ship_img_rect.x += 1
        if keys[pygame.K_LEFT]:
            space_ship_img_rect.x -= 1
        if keys[pygame.K_UP]:
            space_ship_img_rect.y -= 1
        if keys[pygame.K_DOWN]:
            space_ship_img_rect.y += 1
        space_ship_img_rect.clamp_ip(space_surface.get_rect())  # ensure player is inside screen
        space_surface.fill((0, 0, 0))
        space_surface.blit(space_ship_img, space_ship_img_rect)
        clock.tick(60)

    # updating the display
    pygame.display.flip()

pygame.quit()
