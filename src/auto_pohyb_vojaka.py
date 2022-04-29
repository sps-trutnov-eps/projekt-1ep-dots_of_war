import pygame
import sys
import random
import math

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1800,900
BARVA_POZADI = 255,255,255
cas = pygame.time.Clock()
bod_v_case = pygame.time.get_ticks()



#Bod 1
bod1_y = random.randint(0,ROZLISENI_Y)
bod1_x = random.randint(0,ROZLISENI_X)

#Bod 2
bod2_y = random.randint(0,ROZLISENI_Y)
bod2_x = random.randint(0, ROZLISENI_X)

#bod 3
bod3_x = 100
bod3_y = 100

#bod 4
bod4_x = ROZLISENI_X - 100
bod4_y = ROZLISENI_Y -100

bod3_x, bod4_x = min(bod3_x, bod4_x), max(bod3_x, bod4_x)
bod3_y, bod4_y = min(bod3_y, bod4_y), max(bod3_y, bod4_y)



a = math.atan2(bod2_y - bod1_y,bod2_x - bod1_x)


pocatecni_pocet_vojaku = 100
seznam_vojaku = []

for nabor in range(pocatecni_pocet_vojaku):
    vojak = (random.randint(bod3_x, bod4_x), random.randint(bod3_y, bod4_y))
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
    cas_ted = pygame.time.get_ticks()
    od_minula_ms = cas_ted - bod_v_case
    
    if od_minula_ms > 1000:
        vojak = (random.randint(bod3_x, bod4_x), random.randint(bod3_y, bod4_y))
        seznam_vojaku.append(vojak)
        
        bod_v_case = cas_ted 
    okno.fill(BARVA_POZADI)
    
    # pozůstatek jezdícího míčku: pygame.draw.circle(okno,(255,8,0),(x,y),5)
    for v in seznam_vojaku:
        pygame.draw.circle(okno,(255,8,0),v,5)
    
    pygame.display.update()