import pygame
from Window import Window

pygame.init()

# 2. CREATE A PYTHON FILE CONTAINING THE WINDOW CLASS AND USE IT IN UR MAIN SCRIPT

window_surface = Window(500, 600, "Welcome to Chicken Invaders")

display_surface = pygame.display.set_mode((window_surface.width, window_surface.height))

space_surface = pygame.display.set_mode((window_surface.width, window_surface.height))

clock = pygame.time.Clock()

# Load GIF frames
frames = []
for i in range(1, 75):
    # 3. change this so it can be run from any computer
    frames.append(pygame.image.load(f".\\imgs\\frames_space\\{i}.gif"))
frame_index = 0

# defining colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# creating Images
surface_img = pygame.image.load(".\\imgs\\astronaut.jpg")
surface_img_rect = surface_img.get_rect()
surface_img_rect.topleft = (0, 0)

# USE SPACE BETWEEN VARNAME AND VARVALUE
# CREATE AN "ENTITIES" DIRECTORY. MOVE ALL IN GAME OBJECTS INTO SAID DIR.
ROCKET_SIZE = (60, 80)
space_ship_img = pygame.image.load(".\\imgs\\rocket-7339372_1280.png")
space_ship_img = pygame.transform.scale(space_ship_img, ROCKET_SIZE)
space_ship_img_rect = space_ship_img.get_rect()
space_ship_img_rect.centerx = window_surface.width // 2  # Center horizontally
space_ship_img_rect.bottom = window_surface.height  # Place at the bottom

print(f"Rect before scaling: {space_ship_img.get_rect()}")
print(f"Rect after positioning: {space_ship_img_rect}")

running = True
window = False


while running:
    for event in pygame.event.get():
        pygame.display.set_caption(window_surface.title)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP or event.type == pygame.K_SPACE:
            window = True
    if not window:
        display_surface.blit(surface_img, surface_img_rect)

    if window:
        # Display current frame
        space_surface.blit(frames[frame_index], (0, 0))
        # updating frame index
        frame_index = (frame_index + 1) % len(frames)
        # Adjust speed (higher = slower animation)
        clock.tick(10)
        space_surface.blit(space_ship_img, space_ship_img_rect)

    # updating the display
    pygame.display.flip()

pygame.quit()
