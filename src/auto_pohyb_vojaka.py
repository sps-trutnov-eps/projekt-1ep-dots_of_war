import pygame
import sys
import random
import math

class Vojak:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.zije = True

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1800,900
BARVA_POZADI = 255,255,255

tloustka_cary = 3
r1 = 10
r2 = 8
v = 0.8


seda = (128, 128, 128)
cervena = (255,0,0)
modra = (0, 150, 255)

#cara rovne
x1_cary_rovne = 0 
y1_cary_rovne = ROZLISENI_Y - 100 
x2_cary_rovne = 100 
y2_cary_rovne = ROZLISENI_Y - 100

#cara dolu
x1_cary_dolu = 100 
y1_cary_dolu = ROZLISENI_Y - 100
x2_cary_dolu = 100
y2_cary_dolu = ROZLISENI_Y

x1_cary_sikmo = 100
y1_cary_sikmo = ROZLISENI_Y - 100
x2_cary_sikmo = 1600
y2_cary_sikmo = 100

cerveny = Vojak(100, ROZLISENI_Y - 100)
modry = Vojak(1600, 100)

vojaci_modry = [modry]
vojaci_cerveny = [cerveny]

#pohyb červeného míčku
uhel_micku_cerveneho = math.atan2(y2_cary_sikmo - y1_cary_sikmo, x2_cary_sikmo - x1_cary_sikmo)
dy = v * math.sin(uhel_micku_cerveneho)
dx = v * math.cos(uhel_micku_cerveneho)
pygame.init()
#pohyb modrého míčku
uhel_micku_modreho = math.atan2(y2_cary_sikmo - y1_cary_sikmo, x2_cary_sikmo - x1_cary_sikmo)
dy1 = v * math.sin(uhel_micku_modreho)
dx1 = v * math.cos(uhel_micku_modreho)

dostrel = 12

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
                
    for vojak in vojaci_modry:
        if vojak.zije:
            vojak.x -= dx1 * v
            vojak.y -= dy1 * v
    for vojak in vojaci_cerveny:
        if vojak.zije:
            vojak.x += dx * v
            vojak.y += dy * v
        
    vzdalenost_mezi_vojaky = ((cerveny.x - modry.x)**2 - (modry.y - cerveny.y)**2) ** (1/2) 
             
    if vzdalenost_mezi_vojaky < dostrel:
        cerveny.zije = False
        modry.zije = False
    
    okno.fill(BARVA_POZADI)
    
    pygame.draw.line(okno,(0,0,0),(x1_cary_sikmo, y1_cary_sikmo),(x2_cary_sikmo, y2_cary_sikmo),(tloustka_cary))
    pygame.draw.line(okno,(0,0,0),(x1_cary_rovne,y1_cary_rovne),(x2_cary_rovne,y2_cary_rovne),tloustka_cary) 
    pygame.draw.line(okno,(0,0,0),(x1_cary_dolu,y1_cary_dolu),(x2_cary_dolu,y2_cary_dolu),tloustka_cary)
    
    for vojak in vojaci_cerveny:
        if vojak.zije:
            pygame.draw.circle(okno, cervena,(vojak.x,vojak.y),r1)
        else:
            pygame.draw.circle(okno, seda,(vojak.x,vojak.y),r2)
            
    for vojak in vojaci_modry:
        if vojak.zije:
            pygame.draw.circle(okno, modra,(vojak.x,vojak.y),r1)
        else:
            pygame.draw.circle(okno, seda,(vojak.x,vojak.y),r2)
    
    pygame.display.update()
    