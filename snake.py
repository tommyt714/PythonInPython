import pygame
from random import random
from math import sqrt

def makeMouse():
    while True:
        firstMouse = [round(int(random()*(size[0]-mult)) / mult)*mult + body_rad, \
                      round(int(random()*(size[1]-mult)) / mult)*mult + body_rad]
        if firstMouse not in segLoc:
            break

    pygame.draw.circle(pit, RED, firstMouse, int(body_rad/2))

    return firstMouse

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = [800, 600]
pit = pygame.display.set_mode(size)

pygame.display.set_caption("Snake")

done = False
clock = pygame.time.Clock()

score = 0
scorFont = pygame.font.SysFont("impact", 48)

body_rad = 10
mult = 2*body_rad

initX = round(int(random()*(size[0]-mult)) / mult)*mult + body_rad
initY = round(int(random()*(size[1]-mult)) / mult)*mult + body_rad

snake_len = 7

dirVal = 1
dirDict = {1: [1,  0],
           2: [0, -1],
           3: [-1, 0],
           4: [0,  1]
           }

segLoc = []

d = 20
dx = d
dy = 0

while True:
    firstMouse = [round(int(random()*(size[0]-mult)) / mult)*mult + body_rad, \
                  round(int(random()*(size[1]-mult)) / mult)*mult + body_rad]
    if firstMouse[1] >= initY+body_rad or \
       firstMouse[1] <= initY-body_rad:
        break

pit.fill(WHITE)

for seg in range(snake_len):
    col = BLUE if seg == 0 else GREEN
    startX = initX - seg*body_rad*2*dirDict[dirVal][0]
    startY = initY - seg*body_rad*2*dirDict[dirVal][1]

    segLoc.append([startX, startY])
    
    pygame.draw.circle(pit, col, [startX, startY], body_rad)

while not done:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_DOWN and dirVal != 2:
                dx = 0
                dy = d
                dirVal = 4
                break
            elif event.key == pygame.K_LEFT and dirVal != 1:
                dx = -d
                dy = 0
                dirVal = 3
                break
            elif event.key == pygame.K_UP and dirVal != 4:
                dx = 0
                dy = -d
                dirVal = 2
                break
            elif event.key == pygame.K_RIGHT and dirVal != 3:
                dx = d
                dy = 0
                dirVal = 1
                break

    scoreDisp = scorFont.render(str(score), False, BLACK)
    pit.blit(scoreDisp, (740, 20))

    for seg in range(snake_len):
        col = BLUE if seg == 0 else GREEN
        pygame.draw.circle(pit, col, [segLoc[seg][0], segLoc[seg][1]], body_rad)

    if firstMouse in segLoc:
        firstMouse = makeMouse()
        score += 1
        snake_len += 1
        segLoc.append([0,0])
    else:
        pygame.draw.circle(pit, RED, firstMouse, int(body_rad/2))

    for coord in range(len(segLoc)-1, -1, -1):
        if coord == 0:
            segLoc[coord][0] += dx
            segLoc[coord][1] += dy
        else:
            segLoc[coord][0] = segLoc[coord-1][0]
            segLoc[coord][1] = segLoc[coord-1][1]
        
    if segLoc[0] in segLoc[1:]:
        done = True
    elif segLoc[0][0]+body_rad > size[0]:
        segLoc[0][0] -= size[0]
    elif segLoc[0][0]-body_rad < 0:
        segLoc[0][0] += size[0]
    elif segLoc[0][1]+body_rad > size[1]:
        segLoc[0][1] -= size[1]
    elif segLoc[0][1]-body_rad < 0:
        segLoc[0][1] += size[1]

    pygame.display.flip()

    pit.fill(WHITE)
pygame.quit()
