import pygame
import sys
import random
import math

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1800,900
BARVA_POZADI = 255,255,255
#cara
zacatek_cary = 100, ROZLISENI_Y/2
konec_cary = ROZLISENI_X - 100, ROZLISENI_Y/2


#cara rovne
x_cary = 0 
y_cary = ROZLISENI_Y - 300 
x1_cary = 300 
y1_cary = ROZLISENI_Y - 300
tloustka_cary = 3
#cara dolu
x_cary1 = 300 
y_cary1 = ROZLISENI_Y - 300 
x1_cary1 = 300 
y1_cary1 = ROZLISENI_Y

#Bod 1
bod_x1 = 300
bod_y1 = ROZLISENI_Y - 300

#Bod 2
bod_x2 = 1800
bod_y2 = 0

#rychlosti
d = 5
#pohyb micku
uhel_micku= math.atan2(bod_y2 - bod_y1, bod_x2 - bod_x1)
dy = d * math.sin(uhel_micku)
dx = d * math.cos(uhel_micku)



pygame.init()

pygame.display.set_caption('Střet vojáků')
okno = pygame.display.set_mode(ROZLISENI_OKNA)

while True:
    udalosti = pygame.event.get()
    for u in udalosti:
        if u.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if u.type == pygame.MOUSEWHEEL:
            if u.y < 0:
                pygame.display.iconify()
              
        
    okno.fill(BARVA_POZADI)
    
    pygame.draw.line(okno, (0,0,0), (300, ROZLISENI_Y - 300), (1800,0), (tloustka_cary))
    pygame.draw.line(okno,(0,0,0),(x_cary,y_cary),(x1_cary,y1_cary),tloustka_cary) 
    pygame.draw.line(okno,(0,0,0),(x_cary1,y_cary1),(x1_cary1,y1_cary1),tloustka_cary)
    vojak = pygame.draw.circle(okno,(255,0,0),(bod_x1, bod_y1), 5)
    
    
    pygame.display.update()