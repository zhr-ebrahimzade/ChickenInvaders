import pygame


pygame.init()

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600

SPACE_WIDTH = 500
SPACE_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
space_surface= pygame.display.set_mode((SPACE_WIDTH,SPACE_HEIGHT))

clock=pygame.time.Clock()

# Load GIF frames
frames = []
for i in range(1,75): 
    frames.append(pygame.image.load(f"D:\\MyProjects\\chickenInvaders\\imgs\\frames_space\\{i}.gif"))

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

pygame.display.set_caption("Welcome to Chicken Invaders")

# creating Images

surface_img = pygame.image.load("D:\\MyProjects\\chickenInvaders\\imgs\\astronaut.jpg")
surface_img_rect = surface_img.get_rect()
surface_img_rect.topleft=(0,0)

ROCKET_SIZE=(60,80)
spaceShip_img=pygame.image.load("D:\\MyProjects\\chickenInvaders\\imgs\\rocket-7339372_1280.png")
spaceShip_img=pygame.transform.scale(spaceShip_img,ROCKET_SIZE)
spaceShip_img_rect = spaceShip_img.get_rect()
spaceShip_img_rect.centerx = SPACE_WIDTH // 2  # Center horizontally
spaceShip_img_rect.bottom = SPACE_HEIGHT       # Place at the bottom

print(f"Rect before scaling: {spaceShip_img.get_rect()}")
print(f"Rect after positioning: {spaceShip_img_rect}")


running = True
window=False
while (running):
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP or event.type==pygame.K_SPACE:
            window=True
    if window ==False:
        display_surface.blit(surface_img,surface_img_rect)



    if window:
        # Display current frame
        space_surface.blit(frames[frame_index], (0, 0))
        #updating frame index
        frame_index = (frame_index+1) % len(frames)

        clock.tick(10)  # Adjust speed (higher = slower animation)

        space_surface.blit(spaceShip_img, spaceShip_img_rect)


    # updating the dispaly
    pygame.display.flip()

pygame.quit()

