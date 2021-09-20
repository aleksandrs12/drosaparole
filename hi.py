import pygame
import keyboard
import time
import random


def onplat():
    global grav
    global pos
    global posplat
    for n in posplat:
        if pos[1]+40 < n[1]+20 and pos[1]+40 > n[1]-1 and pos[0] < n[0]+80 and pos[0] > n[0]-20:
            if grav < 0:
                grav = 0
            pos[1] = n[1] - 40
            return True
    return False

win = pygame.display.set_mode((400, 400))
run = True

hp = 12
up = 0

pos = [50, 300]
posplat = [[50, 301], [50, 200], [70, 100], [200, 0], [10, 380]]
grav = 0
while run:

    pygame.draw.rect(win, (150, 140, 130), (0, 0, 400, 400))
    pygame.draw.rect(win, (150, 70, 200), (pos[0], pos[1], 20, 40))
    pygame.draw.rect(win, (150, 50, 50), (pos[0]-20, pos[1]-20, hp*5, 10))
    for n in posplat:
        pygame.draw.rect(win, (150, 70, 200), (n[0], n[1], 80, 20))
    for n in range(len(posplat)):
        posplat[n][1] += grav

    for n in range(len(posplat)):
        if posplat[n][1] > 470:
            posplat[n][1] = -30
            posplat[n][0] = random.randint(10, 300)
    #if pos[1] >= 300:
     #   pos[1] = 300
      #  grav = 0
    if not onplat():
        grav -= 2
    if keyboard.is_pressed('a'):
        pos[0] -= 5
    if keyboard.is_pressed('d'):
        pos[0] += 5

    if keyboard.is_pressed('w') and onplat() and hp > 0 and grav == 0:
        grav = 27
        hp -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if pos[0] < 0:
        pos[0] = 0
    elif pos[0] > 380:
        pos[0] = 380

    if up == 1000:
        hp+= 1
        up = 0
    up+=1
    time.sleep(0.01)
    pygame.display.update()
pygame.quit