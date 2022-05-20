import pygame
import sys
import random
import math

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1800,900
BARVA_POZADI = 255,255,255

tloustka_cary = 3

#cara rovne
x1_cary_rovne = 0 
y1_cary_rovne = ROZLISENI_Y - 300 
x2_cary_rovne = 300 
y2_cary_rovne = ROZLISENI_Y - 300

#cara dolu
x1_cary_dolu = 300 
y1_cary_dolu = ROZLISENI_Y - 300 
x2_cary_dolu = 300
y2_cary_dolu = ROZLISENI_Y

#vojak cerveny
vojak_x = 300
vojak_y = ROZLISENI_Y - 300
#vojak modry
vojak_modry_x = 1800 - 5
vojak_modry_y = 0 

#sikma cara
x1_cary_sikmo = 300
y1_cary_sikmo = ROZLISENI_Y - 300
x2_cary_sikmo = 1800
y2_cary_sikmo = 0


#rychlosti
v = 0.1
#pohyb červeného míčku
uhel_micku_cerveneho= math.atan2(y2_cary_sikmo - y1_cary_sikmo, x2_cary_sikmo - x1_cary_sikmo)
dy = v * math.sin(uhel_micku_cerveneho)
dx = v * math.cos(uhel_micku_cerveneho)
pygame.init()
#pohyb modrého míčku


pygame.display.set_caption('Střet vojaku')
okno = pygame.display.set_mode(ROZLISENI_OKNA)

while True:
    udalosti = pygame.event.get()
    for u in udalosti:
        if u.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if u.type == pygame.KEYDOWN and u.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        if u.type == pygame.MOUSEWHEEL:
            if u.y < 0:
                pygame.display.iconify()
             
        
    vojak_x += dx
    vojak_y += dy
   
    
    
     
    okno.fill(BARVA_POZADI)
    
    pygame.draw.line(okno, (0,0,0), (x1_cary_sikmo, y1_cary_sikmo), (x2_cary_sikmo, y2_cary_sikmo), (tloustka_cary))
    pygame.draw.line(okno,(0,0,0),(x1_cary_rovne,y1_cary_rovne),(x2_cary_rovne,y2_cary_rovne),tloustka_cary) 
    pygame.draw.line(okno,(0,0,0),(x1_cary_dolu,y1_cary_dolu),(x2_cary_dolu,y2_cary_dolu),tloustka_cary)
    pygame.draw.circle(okno,(255,0,0),(vojak_x, vojak_y), 10)
    pygame.draw.circle(okno,(0, 150, 255),(vojak_modry_x, vojak_modry_y ), 10)
    
    
    pygame.display.update()