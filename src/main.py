import sys

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

import pygame
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

from mapa import mapa
from ovladani import *
from automatizace import *

pozadi = 20,150,20
rozliseni = rozliseni_x, rozliseni_y = 900, 900

ikona = pygame.image.load(DATA_ROOT + "/data/Ikona.png")
pygame.display.set_caption("Dots of War")
okno = pygame.display.set_mode(rozliseni)
pygame.display.set_icon(ikona)
hodinky = pygame.time.Clock()
font = pygame.font.SysFont("oldenglishtext.ttf", 24)
font_vyhry = pygame.font.SysFont("oldenglishtext.ttf", 50)
konec = False
bila = (255,255,255)
cerna = (0,0,0)

spawn = pygame.USEREVENT+0
pustit = pygame.USEREVENT+1
pohyb = pygame.USEREVENT+2
casovac_spawn = pygame.time.set_timer(spawn,500)
casovac_pustit = pygame.time.set_timer(pustit,200)
casovac_pohyb = pygame.time.set_timer(pohyb,20)

seznam_vojaku_s = []
seznam_na_ceste_s = []
seznam_vojaku_j = []
seznam_na_ceste_j = []
spawni(seznam_vojaku_s, mapa, mapa["zakladna_s"])
spawni(seznam_vojaku_j, mapa, mapa["zakladna_j"])
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
            
            if vez["hrac"] == "s":
                okraj = 0,0,255
                barva = 0,0,255
            elif vez["hrac"] == "j":
                okraj = 255,0,0
                barva = 255,0,0
                    
            if vez["hp"] <= 0:
                barva = 0,0,0
                
            pygame.draw.rect(okno, okraj, (pozice_x-2, pozice_y-2, sirka+4, vyska+4))
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
    
    for vojak in seznam_vojaku_s:
        pygame.draw.circle(okno, (0,0,185), (vojak[0], vojak[1]), 5)
        
    for vojak in seznam_vojaku_j:
        pygame.draw.circle(okno, (185,0,0), (vojak[0], vojak[1]), 5)
    
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
        
    for vojak in seznam_na_ceste_s:
        pygame.draw.circle(okno, (0,0,185), (vojak[0]*150, vojak[1]*150), 5)
        
    for vojak in seznam_na_ceste_j:
        pygame.draw.circle(okno, (185,0,0), (vojak[0]*150, vojak[1]*150), 5)
        
zacatek = False

while True:
    udalosti = pygame.event.get()
    for udalost in udalosti:
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if udalost.type == spawn and not konec and zacatek:
            spawni(seznam_vojaku_s, mapa, mapa["zakladna_s"])
            spawni(seznam_vojaku_j, mapa, mapa["zakladna_j"])
        if udalost.type == pustit and not konec and zacatek:
            pust(mapa, seznam_vojaku_s, seznam_na_ceste_s, mapa["brany_s"])
            pust(mapa, seznam_vojaku_j, seznam_na_ceste_j, mapa["brany_j"])
        if udalost.type == pohyb and not konec and zacatek:
            pohni(mapa, seznam_na_ceste_s, "s")
            pohni(mapa, seznam_na_ceste_j, "j")
    
    stisk = pygame.key.get_pressed()
    
    if stisk[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    
    okno.fill(pozadi)
    if not konec and zacatek:
        oznac(mapa)
        prehod(mapa, seznam_vojaku_s, seznam_vojaku_j)
        brany(mapa)
    utok_na_vez(mapa, seznam_na_ceste_s, "s")
    utok_na_vez(mapa, seznam_na_ceste_j, "j")
    utok(seznam_na_ceste_s, seznam_na_ceste_j)
    zobraz_mapu(mapa)
    kontrola(mapa, seznam_na_ceste_s, "s", seznam_vojaku_j, konec)
    kontrola(mapa, seznam_na_ceste_j, "j", seznam_vojaku_s, konec)
    if seznam_vojaku_s == [] or seznam_vojaku_j == []:
        konec = True
    
    zobraz_mapu(mapa)
    
    if zacatek == False:
        text_z = font_vyhry.render("Započni hru stiskem Mezerníku", True, bila)
        misto_pro_text_z = text_z.get_rect(center=(rozliseni_x/2,rozliseni_y/2))
        pygame.draw.rect(okno, cerna, (100,100,700,700))
        okno.blit(text_z, misto_pro_text_z)
        if stisk[pygame.K_SPACE]:
            zacatek = True
    
    if konec:
        zobraz_mapu(mapa)
        if seznam_vojaku_s == []:
            barva = (230,100,100)
            text = font_vyhry.render("Jižní království vítězí", True, barva)
        elif seznam_vojaku_j == []:
            barva = (100,100,230)
            text = font_vyhry.render("Severní království vítězí", True, barva)
        text2 = font.render("Stiskni R pro restart", True, bila)
        misto_pro_text = text.get_rect(center=(rozliseni_x/2,rozliseni_y/2 - 50))
        misto_pro_text2 = text.get_rect(center=(rozliseni_x/2,rozliseni_y/2 + 50))
        pygame.draw.rect(okno, cerna, (100,100,700,700))
        okno.blit(text, misto_pro_text)
        okno.blit(text2, misto_pro_text2)
        if stisk[pygame.K_r]:
            konec = False
            seznam_na_ceste_s = []
            seznam_na_ceste_j = []
            seznam_vojaku_s = []
            seznam_vojaku_j = []
            spawni(seznam_vojaku_s, mapa, mapa["zakladna_s"])
            spawni(seznam_vojaku_j, mapa, mapa["zakladna_j"])
            for brana in mapa["brany_s"]:
                brana["stav"] = False
            for brana in mapa["brany_j"]:
                brana["stav"] = False
            for vez in mapa["veze_s"]:
                vez["hp"] = 0
                vez["vybrano"] = False
            mapa["veze_s"][0]["vybrano"] = True
            for vez in mapa["veze_j"]:
                vez["hp"] = 0
                vez["vybrano"] = False
            mapa["veze_j"][0]["vybrano"] = True
            for vyhybka in mapa["vyhybky_s"]:
                vyhybka["stav"] = False
                vyhybka["vybrano"] = False
            mapa["vyhybky_s"][0]["vybrano"] = True
            for vyhybka in mapa["vyhybky_j"]:
                vyhybka["stav"] = True
                vyhybka["vybrano"] = False
            mapa["vyhybky_j"][0]["vybrano"] = True
            aktivni_s = mapa["vyhybky_s"]
            aktivni_j = mapa["vyhybky_j"]
        
    pygame.display.update()
    hodinky.tick(144)
