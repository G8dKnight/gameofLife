import pygame

screen_width    = 400
screen_height   = 300
block_size      = 10


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def main():
    pygame.init()

    global screen

    screen = pygame.display.set_mode((screen_width,screen_height))
    screen.fill(BLACK)

    while True:
        draw_grid()
        pygame.display.update()


def draw_grid():

    for x in range(screen_width,block_size):
        for y in range(screen_height,block_size):
            rect = pygame.Rect(x,y,block_size,block_size)
            pygame.draw.rect(screen, WHITE ,rect)


main()
