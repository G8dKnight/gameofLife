import pygame 
import sys
import time

"""
RULES:
    1.Any live cell with fewer than two live neighbors dies as if caused by underpopulation.
    2.Any live cell with two or three live neighbors lives on to the next generation.
    3.Any live cell with more than three live neighbors dies, as if by overpopulation.
    4.Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
"""

#----------------------------------------------------------------
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREY = (52,52,52)
RED = (255,0,0)

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

BLOCKSIZE = 20 #Set the size of the grid block
ALIVE = 1
DEAD  = 0
#ALIVE_CELLS = []
#---------------------------------------------------------------
def get_num_of_neighbours(x,y):
    count = 0
    for i in range(x-BLOCKSIZE,x+2*BLOCKSIZE,BLOCKSIZE):
        for j in range(y-1*BLOCKSIZE,y+2*BLOCKSIZE,BLOCKSIZE):
            if i == x and j == y:
                continue
            else:
                if (i,j) in ALIVE_CELLS:
                    count += 1
    
    return count


def drawGrid():
    for x in range(0, WINDOW_WIDTH, BLOCKSIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCKSIZE):
            rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(SCREEN, GREY, rect, 1 )


def get_block(pos):
    x = pos[0]
    y = pos[1]

    x = x - (x % BLOCKSIZE)
    y = y - (y % BLOCKSIZE)

    return [x,y]

def init():
    pygame.init()
    global SCREEN
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    SCREEN.fill(BLACK)
    drawGrid()


def reset():
    SCREEN.fill(BLACK)
    drawGrid()


def make_generation(ALIVE_CELLS):
    NEXT_GEN = ALIVE_CELLS 
    
    for x in range(0,WINDOW_WIDTH,BLOCKSIZE):
        for y in range(0,WINDOW_HEIGHT,BLOCKSIZE):
            num = get_num_of_neighbours(x,y)
            if num:
                print(num,end='')
                print(f" {int(x/20)},{int(y/20)}")

                # rect = pygame.Rect(x+2,y+2, BLOCKSIZE-4, BLOCKSIZE-4)
                # pygame.draw.rect(SCREEN, WHITE, rect)
                # pygame.display.update()


    # 1.Any live cell with fewer than two live neighbors dies as if caused by underpopulation.
            if num < 2:
                if (x,y) in ALIVE_CELLS:
                    NEXT_GEN.remove((x,y))
                    continue

    # 2.Any live cell with two or three live neighbors lives on to the next generation.
            if num == 2:
                continue

    # 3.Any live cell with more than three live neighbors dies, as if by overpopulation.
            if num == 3:
                if (x,y) not in ALIVE_CELLS:
                    NEXT_GEN.append((x,y))
                    continue

    # 4.Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
            if num > 3:
                if (x,y) in ALIVE_CELLS:
                    NEXT_GEN.remove((x,y))

    return NEXT_GEN
    

def main():
    
    init()
    global ALIVE_CELLS
    ALIVE_CELLS = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                [x,y] = get_block(pos)

                rect = pygame.Rect(x+2,y+2, BLOCKSIZE-4, BLOCKSIZE-4)
                
                if (x,y) in ALIVE_CELLS:
                    pygame.draw.rect(SCREEN, BLACK, rect)
                    ALIVE_CELLS.remove((x,y))
                else:
                    pygame.draw.rect(SCREEN, RED, rect)
                    ALIVE_CELLS.append((x,y))
                    
                pygame.display.update()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    while True:
                        time.sleep(0.5)
                        NEXT_GEN = make_generation(ALIVE_CELLS)

                        reset()

                        for xy in NEXT_GEN:
                            rect = pygame.Rect(xy[0]+2,xy[1]+2, BLOCKSIZE-4, BLOCKSIZE-4)
                            pygame.draw.rect(SCREEN, RED, rect)
                            pygame.display.update()

                        ALIVE_CELLS = NEXT_GEN

                elif event.key == pygame.K_r:
                    ALIVE_CELLS.clear()
                    reset()


            elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main()