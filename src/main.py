from map import mapa
import pygame
import sys

pozadi = 20,150,20
rozliseni = rozliseni_x, rozliseni_y = 900, 900

import pygame
pygame.init()

pygame.display.set_caption("Dots of War")
okno = pygame.display.set_mode(rozliseni)
hodinky = pygame.time.Clock()

def zobraz_mapu(mapa):
    for cesta in mapa["cesty"]:
        hotove_body = []
        for bod in cesta:
            pozice_x = bod[0] * 150
            pozice_y = bod[1] * 150
            hotove_body.append((pozice_x, pozice_y))
        barva = 0,0,0
        sirka = 2

        pygame.draw.lines(okno, barva, False, hotove_body, sirka)
            
    for vyhybka in mapa["vyhybky"]:
        pozice_x = vyhybka["pozice"][0] * 150
        pozice_y = vyhybka["pozice"][1] * 150
        if vyhybka["hrac"] == "j":
            barva = 255,0,0
        else:
            barva = 0,0,255
        polomer = 10
        
        pygame.draw.circle(okno, barva, (pozice_x, pozice_y), polomer)

while True:
    udalosti = pygame.event.get()
    for udalost in udalosti:
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    okno.fill(pozadi)
    
    zobraz_mapu(mapa)
    
    pygame.display.update()
    hodinky.tick(60)