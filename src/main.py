import pygame
import sys
from map import mapa
from prepinani_mezi_objekty import *

pozadi = 20,150,20
rozliseni = rozliseni_x, rozliseni_y = 900, 900

import pygame
pygame.init()

pygame.display.set_caption("Dots of War")
okno = pygame.display.set_mode(rozliseni)
hodinky = pygame.time.Clock()
font = pygame.font.SysFont("oldenglishtext.ttf", 24)
    
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
            
    for vyhybky in mapa["vyhybky_s"],mapa["vyhybky_j"]:
        for vyhybka in vyhybky:
            pozice_x = vyhybka["pozice"][0] * 150
            pozice_y = vyhybka["pozice"][1] * 150
            bod = (pozice_x, pozice_y)
            
            if vyhybka["hrac"] == "j":
                barva = 255,0,0
            else:
                barva = 0,0,255
            polomer = 10
            tloustka = 6
            
            if vyhybka["hrac"] == "j":
                if vyhybka["stav"] == False:
                    if vyhybka["rozcesti"][0] == "S":
                        druhy_bod = (bod[0], bod[1]-21)
                    elif vyhybka["rozcesti"][0] == "SV":
                        druhy_bod = (bod[0]+15, bod[1]-15)
                elif vyhybka["stav"] == True:
                    if vyhybka["rozcesti"][1] == "SV":
                        druhy_bod = (bod[0]+15, bod[1]-15)
                    elif vyhybka["rozcesti"][1] == "V":
                        druhy_bod = (bod[0]+21, bod[1])
            elif vyhybka["hrac"] == "s":
                if vyhybka["stav"] == False:
                    if vyhybka["rozcesti"][0] == "Z":
                        druhy_bod = (bod[0]-21, bod[1])
                    elif vyhybka["rozcesti"][0] == "JZ":
                        druhy_bod = (bod[0]-15, bod[1]+15)
                elif vyhybka["stav"] == True:
                    if vyhybka["rozcesti"][1] == "JZ":
                        druhy_bod = (bod[0]-15, bod[1]+15)
                    elif vyhybka["rozcesti"][1] == "J":
                        druhy_bod = (bod[0], bod[1]+21)
                    
            
            pygame.draw.circle(okno, barva, bod, polomer)
            pygame.draw.line(okno, barva, bod, druhy_bod, tloustka)
        
    for veze in mapa["veze_s"],mapa["veze_j"]:
        for vez in veze:
            pozice_x = (vez["pozice"][0] * 150) - 6
            pozice_y = (vez["pozice"][1] * 150) - 10
            vyska = 20
            sirka = 12
            if vez["hp"] <= 0:
                barva = 0,0,0
            elif vez["hp"] > 0:
                if vez["hrac"] == "s":
                    barva = 0,0,255
                elif vez["hrac"] == "j":
                    barva = 255,0,0

            pygame.draw.rect(okno, barva, (pozice_x, pozice_y, sirka, vyska))
    
    body_s = []
    for bod in mapa["zakladna_s"]["body"]:
        body_s.append((bod[0] * 150, bod[1] * 150))
    pygame.draw.polygon(okno, pozadi, body_s)
    pygame.draw.polygon(okno, (0,0,255), body_s, 5)
    
    body_j = []
    for bod in mapa["zakladna_j"]["body"]:
        body_j.append((bod[0] * 150, bod[1] * 150))
    pygame.draw.polygon(okno, pozadi, body_j)
    pygame.draw.polygon(okno, (255,0,0), body_j, 5)
    
    for i, cislo in enumerate(mapa["cisla_s"]):
        if mapa["brany_s"][i]["stav"]:
            pygame.draw.circle(okno, BARVA_OZNACENI_SEVER, (mapa["brany_s"][i]["pozice"][0] * 150,mapa["brany_s"][i]["pozice"][1] * 150), 15)
        pygame.draw.circle(okno, (0,0,255), (mapa["brany_s"][i]["pozice"][0] * 150,mapa["brany_s"][i]["pozice"][1] * 150), 10)
        text = font.render(cislo["cislo"], True, (255,255,255), (0,0,255))
        napis = text.get_rect()
        napis.center = (cislo["pozice"][0] * 150, cislo["pozice"][1] * 150)
        okno.blit(text, napis)
    
    for i, cislo in enumerate(mapa["cisla_j"]):
        if mapa["brany_j"][i]["stav"]:
            pygame.draw.circle(okno, BARVA_OZNACENI_JIH, (mapa["brany_j"][i]["pozice"][0] * 150,mapa["brany_j"][i]["pozice"][1] * 150), 15)
        pygame.draw.circle(okno, (255,0,0), (mapa["brany_j"][i]["pozice"][0] * 150,mapa["brany_j"][i]["pozice"][1] * 150), 10)
        text = font.render(cislo["cislo"], True, (255,255,255), (255,0,0))
        napis = text.get_rect()
        napis.center = (cislo["pozice"][0] * 150, cislo["pozice"][1] * 150)
        okno.blit(text, napis)

while True:
    udalosti = pygame.event.get()
    for udalost in udalosti:
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    stisk = pygame.key.get_pressed()
    
    if stisk[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    
    okno.fill(pozadi)
    
    oznac(mapa)
    prehod(mapa)
    zobraz_mapu(mapa)
    
    pygame.display.update()
    hodinky.tick(60)