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
        bod = (pozice_x, pozice_y)
        
        if vyhybka["hrac"] == "j":
            barva = 255,0,0
        else:
            barva = 0,0,255
        polomer = 10
        tloustka = 4
        
        if vyhybka["hrac"] == "j":
            if vyhybka["stav"] == False:
                if vyhybka["rozcesti"][0] == "S":
                    druhy_bod = (bod[0], bod[1]-20)
                elif vyhybka["rozcesti"][0] == "SV":
                    druhy_bod = (bod[0]+20, bod[1]-20)
            elif vyhybka["stav"] == True:
                if vyhybka["rozcesti"][1] == "SV":
                    druhy_bod = (bod[0]+20, bod[1]-20)
                elif vyhybka["rozcesti"][1] == "V":
                    druhy_bod = (bod[0]+20, bod[1])
        elif vyhybka["hrac"] == "s":
            if vyhybka["stav"] == False:
                if vyhybka["rozcesti"][0] == "Z":
                    druhy_bod = (bod[0]-20, bod[1])
                elif vyhybka["rozcesti"][0] == "JZ":
                    druhy_bod = (bod[0]-20, bod[1]+20)
            elif vyhybka["stav"] == True:
                if vyhybka["rozcesti"][1] == "JZ":
                    druhy_bod = (bod[0]-20, bod[1]+20)
                elif vyhybka["rozcesti"][1] == "J":
                    druhy_bod = (bod[0], bod[1]+20)
                
        
        pygame.draw.circle(okno, barva, bod, polomer)
        pygame.draw.line(okno, barva, bod, druhy_bod, tloustka)

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