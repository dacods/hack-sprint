import pygame

# Start up
pygame.init()
screen_size = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen_size.get_width() / 2, screen_size.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen_size.fill("purple")

    pygame.draw.circle(screen_size, "red", player_pos, 40)

    # Moves the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()