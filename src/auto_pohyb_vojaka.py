import pygame
import sys
import random
import math

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1800,900
BARVA_POZADI = 255,255,255

#Bod 1
bod1_y = random.randint(0,ROZLISENI_Y)
bod1_x = random.randint(0,ROZLISENI_X)

#Bod 2
bod2_y = random.randint(0,ROZLISENI_Y)
bod2_x = random.randint(0, ROZLISENI_X)

bod1_x, bod2_x = min(bod1_x, bod2_x), max(bod1_x, bod2_x)
bod1_y, bod2_y = min(bod1_y, bod2_y), max(bod1_y, bod2_y)

#Bod 3

a = math.atan2(bod2_y - bod1_y,bod2_x - bod1_x)


k = 100
seznam_vojaku = []

for nabor in range(k):
    vojak = (random.randint(bod1_x, bod2_x), random.randint(bod1_y, bod2_y))
    seznam_vojaku.append(vojak)

pygame.init()

pygame.display.set_caption('pozor chodec')
okno = pygame.display.set_mode(ROZLISENI_OKNA)
x = bod1_x
y = bod1_y
while True:
    udalosti = pygame.event.get()
    for u in udalosti:
        if u.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if u.type == pygame.MOUSEWHEEL:
            if u.y < 0:
                pygame.display.iconify()
    if x < bod2_x and bod2_x > bod1_x:
        x += 0.5 * math.cos(a)
        y += 0.5 * math.sin(a)
    if x > bod2_x and bod2_x < bod1_x:
        x += 0.5 * math.cos(a)
        y += 0.5 * math.sin(a)
            
    okno.fill(BARVA_POZADI)
    
    pygame.draw.circle(okno,(255,8,0),(x,y),5)
    for v in seznam_vojaku:
        pygame.draw.circle(okno,(255,8,0),v,5)
    
    pygame.display.update()