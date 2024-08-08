import pygame

# Start up
pygame.init()
screen_size = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

sprite_sheet = pygame.image.load('sprites/characters/player.png').convert_alpha()

frame_width = 64
frame_height = 64

def get_frame(sprite_sheet, frame_rect):
    return sprite_sheet.subsurface(frame_rect).copy()

#extract first frame
frame_rect = pygame.Rect(0, 0, frame_width, frame_height)
character_frame = get_frame(sprite_sheet, frame_rect)

#character size
scale_factor = 2

character_frame = pygame.transform.scale(character_frame, (frame_width * scale_factor, frame_height * scale_factor))

world_size = pygame.Vector2(2000, 2000)
world_rect = pygame.Rect(0, 0, world_size.x, world_size.y)

player_pos = pygame.Vector2(screen_size.get_width() / 2, screen_size.get_height() / 2)
camera = pygame.Vector2(0, 0)

threshhold_x = 200
threshhold_y = 150

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen_size.fill("purple")


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

    player_pos.x = max(0, min(world_size.x, player_pos.x))
    player_pos.y = max(0, min(world_size.y, player_pos.y))

    if player_pos.x - camera.x < threshhold_x:
        camera.x = max(0, player_pos.x - threshhold_x)
    elif player_pos.x - camera.x > screen_size.get_width() - threshhold_x:
        camera.x = min(world_size.x - screen_size.get_width(), player_pos.x - (screen_size.get_width() - threshhold_x)) 
    
    if player_pos.y - camera.y < threshhold_y:
        camera.y = max(0, player_pos.y - threshhold_y)
    elif player_pos.y - camera.y > screen_size.get_height() - threshhold_y:
        camera.y = min(world_size.y - screen_size.get_height(), player_pos.y - (screen_size.get_height() - threshhold_y))
    
    player_screen_pos = player_pos - camera
    screen_size.blit(character_frame, player_screen_pos)
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()