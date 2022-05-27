import pygame
import sys
import random
import math
pygame.init()

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1800,900
BARVA_POZADI = 255,255,255

tloustka_cary = 3
r = 10


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

#sikma cara
x1_cary_sikmo = 100
y1_cary_sikmo = ROZLISENI_Y - 100
x2_cary_sikmo = 1600
y2_cary_sikmo = 100


#rychlosti
v = 0.3

#spawn wojaka
def spawn(color):
    vojak = []
    if color == "red":
        vojak.append([100,ROZLISENI_Y - 100])
    else:
        vojak.append([1600,100])
    vojak.append(color)
    return(vojak)

#seznamy
ruda_armada = []
US_Army = []

#přidání wojáků
ruda_armada.append(spawn("red"))
US_Army.append(spawn("blue"))

#pohyb červeného míčku

uhel_micku_cerveneho = math.atan2(y2_cary_sikmo - y1_cary_sikmo, x2_cary_sikmo - x1_cary_sikmo)
dy = v * math.sin(uhel_micku_cerveneho)
dx = v * math.cos(uhel_micku_cerveneho)

#pohyb modrého míčku

uhel_micku_modreho = math.atan2(x1_cary_sikmo - x2_cary_sikmo, y1_cary_sikmo - y2_cary_sikmo)
dx1 = v * math.sin(uhel_micku_modreho)
dy1 = v * math.cos(uhel_micku_modreho)

dostrel = 12

pygame.display.set_caption('Střet vojaku')
okno = pygame.display.set_mode(ROZLISENI_OKNA)

zije = True
#zije = pygame.draw.circle(okno,(255,0,0),(vojak_x, vojak_y), 10), pygame.draw.circle(okno,(0, 150, 255),(vojak_modry_x, vojak_modry_y ), 10)
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
             
    #pohyb cerveny
    for wojak in ruda_armada:
        if wojak[1] != "gray":
            wojak[0][0] += dx
            wojak[0][1] += dy

    #pohyb modry
    for wojak in US_Army:
        if wojak[1] != "gray":
            wojak[0][0] -= dx
            wojak[0][1] -= dy
    
    #kolize s vojaky
#     c = ((vojak_x - vojak_modry_x)**2 - (vojak_modry_y - vojak_y)**2) ** (1/2)
#     if c < dostrel:
#         zije = False
#         modra = seda
#         cervena = seda
#         r = 8
        
    okno.fill(BARVA_POZADI)
    
    pygame.draw.line(okno, (0,0,0), (x1_cary_sikmo, y1_cary_sikmo), (x2_cary_sikmo, y2_cary_sikmo), (tloustka_cary))
    pygame.draw.line(okno,(0,0,0),(x1_cary_rovne,y1_cary_rovne),(x2_cary_rovne,y2_cary_rovne),tloustka_cary) 
    pygame.draw.line(okno,(0,0,0),(x1_cary_dolu,y1_cary_dolu),(x2_cary_dolu,y2_cary_dolu),tloustka_cary)
    for wojak in ruda_armada:
        pygame.draw.circle(okno,wojak[1],(wojak[0][0], wojak[0][1]), r)
    for wojak in US_Army:
        pygame.draw.circle(okno,wojak[1],(wojak[0][0], wojak[0][1]), r)
    
    
    pygame.display.update()