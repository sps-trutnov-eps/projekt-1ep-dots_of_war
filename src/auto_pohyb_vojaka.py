import pygame
import sys
import random
import math

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1800,900
BARVA_POZADI = 255,255,255
#cara
zacatek_cary = 100, ROZLISENI_Y/2
konec_cary = ROZLISENI_X - 100, ROZLISENI_Y/2
tloustka_cary = 3

#vojak

#Bod 1
bod_xy = zacatek_cary

#Bod 2
bod_xy2 = konec_cary

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
    
    pygame.draw.line(okno, (0,0,0), (zacatek_cary), (konec_cary), (tloustka_cary))
    pygame.draw.ellipse(okno,(255,0,0),(bod_xy),5)
    
    
    
    pygame.display.update()