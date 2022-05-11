import pygame
import sys
import random
import math

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1800,900
BARVA_POZADI = 255,255,255
cas = pygame.time.Clock()
bod_v_case = pygame.time.get_ticks()
bod2_v_case = pygame.time.get_ticks()
rad = 5
# vodorovná čára základny
x_cary = 0
y_cary = ROZLISENI_Y - 300
x1_cary = 300
y1_cary = ROZLISENI_Y - 300
w = 5
# cara dolu
x_cary1 = 300
y_cary1 = ROZLISENI_Y - 300
x1_cary1 = 300
y1_cary1 = ROZLISENI_Y

#Bod 1 bod spawnu míčku, který leze
bod1_y = ROZLISENI_Y - ROZLISENI_Y/3
bod1_x = 300

#Bod 2, bod 
bod2_y = 200
bod2_x = ROZLISENI_X - 300

#bod 3, bod začáku základny
bod3_x = rad
bod3_y = ROZLISENI_Y - ROZLISENI_Y/3

#bod 4, bod konce základny 
bod4_x = bod1_x
bod4_y = ROZLISENI_Y - rad

bod3_x, bod4_x = min(bod3_x, bod4_x), max(bod3_x, bod4_x)
bod3_y, bod4_y = min(bod3_y, bod4_y), max(bod3_y, bod4_y)
 
#spawn vojáků
vojak_x = random.randint(0,300)
vojak_y = random.randint(ROZLISENI_Y - 300,ROZLISENI_Y)

#pohyb
hledani_x = []
chozeni_x = -1

a = math.atan2(bod2_y - bod1_y,bod2_x - bod1_x)

v_vojaka = 40
pocatecni_pocet_vojaku = 1
seznam_vojaku = []
seznam_vojaku_na_pochodu = []
x_pohybujici = []

for nabor in range(pocatecni_pocet_vojaku):
    vojak = [vojak_x,vojak_y]
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
    stisknuto = pygame.key.get_pressed()
    vojak_x = random.randint(0,300)
    vojak_y = random.randint(ROZLISENI_Y - 300,ROZLISENI_Y)       
    cas_ted = pygame.time.get_ticks()
    od_minula_ms = cas_ted - bod_v_case
    od_minula2_ms = cas_ted - bod2_v_case
    if od_minula_ms > 700:
        
        hledani_x.append(chozeni_x + 1)
        chozeni_x += 1
        
        vojak = [vojak_x, vojak_y]
        seznam_vojaku.append(vojak)
        
        for x_1 in hledani_x:
        #pohyb_x prvniho vojaka
            seznam_vojaku[x_1][0] += 40
    
        bod_v_case = cas_ted
        
    okno.fill(BARVA_POZADI)
    
    # pozůstatek jezdícího míčku: pygame.draw.circle(okno,(255,8,0),(x,y),5)
    for v in seznam_vojaku:
        pygame.draw.circle(okno,(255,8,0),v,rad)
    for p_v in seznam_vojaku_na_pochodu:
        pygame.draw.circle(okno,(255,8,0),(p_v),rad)
    pygame.draw.line(okno,(0,0,0),(x_cary,y_cary),(x1_cary,y1_cary),w)
    pygame.draw.line(okno,(0,0,0),(x_cary1,y_cary1),(x1_cary1,y1_cary1),w)
    
        
    pygame.display.update()