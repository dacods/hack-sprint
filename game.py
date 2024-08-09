import pygame

# Start up
pygame.init()
screen_size = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# tile assets
grass_tile = pygame.image.load('sprites/tilesets/floors/grass.png').convert()
path_tile = pygame.image.load('sprites/tilesets/floors/wooden.png').convert()
floor_tile = pygame.image.load('sprites/tilesets/floors/plains.png').convert_alpha()

tile_size = 16

tile_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# mapping tile assets
tile_dict = {
    0: grass_tile,
    1: path_tile,
    2: floor_tile
}

object_sheet = pygame.image.load('sprites/objects/objects.png').convert_alpha()

# position and size of the object to extract
object_x = 46  # x-coordinate on the sprite sheet
object_y = 67  # y-coordinate on the sprite sheet
object_width = 50  # width of the object
object_height = 78  # height of the object

# extract the object
object_rect = pygame.Rect(object_x, object_y, object_width, object_height)
object_image = object_sheet.subsurface(object_rect).copy()

sprite_sheet = pygame.image.load('sprites/characters/player.png').convert_alpha()

frame_width = 64
frame_height = 64

def get_frame(sprite_sheet, frame_rect):
    return sprite_sheet.subsurface(frame_rect).copy()

#extract first frame of character
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

# draw the map
def draw_map(screen, camera):
    for y, row in enumerate(tile_map):
        for x, tile in enumerate(row):
            if tile in tile_dict:
                screen.blit(tile_dict[tile], (x * tile_size - camera.x, y * tile_size - camera.y))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen_size.fill("purple")

    # in the main loop, before drawing the player, add:
    draw_map(screen_size, camera)

    # blit extracted obj, might need adjusting
    screen_size.blit(object_image, (300 - camera.x, 200 - camera.y))

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