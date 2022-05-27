import pygame
import sys
import random
import math


####### Parametry #######
ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1800,900
BARVA_POZADI = 255,255,255

cas_spawnu_posledniho_vojaka = pygame.time.get_ticks()
cas_odchodu_posledniho_vojaka_na_frontu = pygame.time.get_ticks()
cas_od_posledniho_pohybu_vojaku_na_ceste = pygame.time.get_ticks()

souradnice_kasaren_x = 0
souradnice_kasaren_y = 650
souradnice_bileho_obdelniku_x = 10
souradnice_bileho_obdelniku_y = 660

velikost_bileho_obdelniku_x = 230
velikost_bileho_obdelniku_y = 230
velikost_kasaren_x = 250
velikost_kasaren_y = 250

startovni_pozice_cary_XY = 250, 775
konecna_pozice_cary_XY = 850, 400

rychlost_vojaka = 0.5


####### Souřadnice kasáren levého horního bodu #######
vojaci_kasarny_levy_horni_bod_y = souradnice_bileho_obdelniku_y
vojaci_kasarny_levy_horni_bod_x = souradnice_bileho_obdelniku_x

####### Souřadnice kasáren pravého dolního bodu #######
vojaci_kasarny_pravy_dolni_bod_y = souradnice_bileho_obdelniku_y + velikost_kasaren_y
vojaci_kasarny_pravy_dolni_bod_x = souradnice_bileho_obdelniku_x + velikost_kasaren_x

####### Nábor vojáků #######
pocatecni_pocet_vojaku = 1 
seznam_vojaku = []
seznam_vojaku_na_ceste = []

def spawni(seznam_vojaku, mapa):
    if seznam_vojaku == seznam_vojaku_s:
        zakladna = mapa["zakladna_s"]
    elif seznam_vojaku == seznam_vojaku_j:
        zakladna = mapa["zakladna_j"]
    
    rameno = 75 + 7.07
    x = y = 0
    while (x + y) < rameno:
        x = random.randint(5, 220)
        y = random.randint(5, 220)
        
    vojak = [x, y]
    seznam_vojaku.append(vojak)
    return seznam_vojaku
    
def pust(mapa, seznam_vojaku, seznam_vojaku_na_ceste):
    if seznam_vojaku == seznam_vojaku_s:
        brany = mapa["brany_s"]
    elif seznam_vojaku == seznam_vojaku_j:
        brany = mapa["brany_j"]
        
    for brana in brany:
        if brana["stav"] == True:
            vojak_nove_na_ceste = seznam_vojaku.pop()
            seznam_vojaku_na_ceste.append(vojak_nove_na_ceste)
            vojak_nove_na_ceste[0], vojak_nove_na_ceste[1] = startovni_pozice_cary_XY
            return seznam_vojaku, seznam_vojaku_na_ceste
        else:
            pass
    
        ####### Pohyb vojáků #######
    if doba_od_posledniho_pohybu_vojaku_na_ceste > 5:
        for v in seznam_vojaku_na_ceste:
            uhel = math.atan2((konecna_pozice_cary_XY[1] - v[1]),(konecna_pozice_cary_XY[0] - v[0]))
            posun_x = math.cos(uhel) * 0.25
            posun_y = math.sin(uhel) * 0.25
            v[0] += posun_x
            v[1] += posun_y
            
 
        cas_od_posledniho_pohybu_vojaku_na_ceste = pygame.time.get_ticks()
            
   
    
          ####### Vykreslování tvarů #######   
    okno.fill(BARVA_POZADI)
    
    pygame.draw.rect(okno, (0,0,0), ((souradnice_kasaren_x, souradnice_kasaren_y), (velikost_kasaren_x, velikost_kasaren_y)))
    pygame.draw.rect(okno, (255,255,255), ((souradnice_bileho_obdelniku_x, souradnice_bileho_obdelniku_y), (velikost_bileho_obdelniku_x, velikost_bileho_obdelniku_y)))
    pygame.draw.line(okno, (0,0,0), (startovni_pozice_cary_XY), (konecna_pozice_cary_XY), 5) 
    for v in seznam_vojaku:
        pygame.draw.circle(okno,(255,8,0),v,5)
    for v in seznam_vojaku_na_ceste:
        pygame.draw.circle(okno,(255,8,0),v,5)
        
    pygame.display.update()