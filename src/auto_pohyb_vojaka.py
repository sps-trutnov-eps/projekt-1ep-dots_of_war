import pygame
import sys
import random
import math

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1800,900
BARVA_POZADI = 255,255,255
cas = pygame.time.Clock()
bod_v_case = pygame.time.get_ticks()
souradnice_kasaren_x = 0
souradnice_kasaren_y = 650
souradnice_bileho_obdelniku_x = 10
souradnice_bileho_obdelniku_y = 660
velikost_bileho_obdelniku_x = 230
velikost_bileho_obdelniku_y = 230
velikost_kasaren_x = 250
velikost_kasaren_y = 250
startovni_pozice_cary_XY = 250, 775
konecna_pozice_cary_XY = 850, 775 

#Bod 1
vojaci_kasarny_levy_horni_bod_y = souradnice_bileho_obdelniku_y
vojaci_kasarny_levy_horni_bod_x = souradnice_bileho_obdelniku_x

#Bod 2
vojaci_kasarny_pravy_dolni_bod_y = souradnice_bileho_obdelniku_y + velikost_kasaren_y
vojaci_kasarny_pravy_dolni_bod_x = souradnice_bileho_obdelniku_x + velikost_kasaren_x



#Bod 3

a = math.atan2(vojaci_kasarny_pravy_dolni_bod_y - vojaci_kasarny_levy_horni_bod_y,vojaci_kasarny_pravy_dolni_bod_x - vojaci_kasarny_levy_horni_bod_x)


pocatecni_pocet_vojaku = 50 
seznam_vojaku = []
seznam_vojaku_na_ceste = []

for nabor in range(pocatecni_pocet_vojaku):
    vojak = [
        random.randint(vojaci_kasarny_levy_horni_bod_x, vojaci_kasarny_pravy_dolni_bod_x-26),
        random.randint(vojaci_kasarny_levy_horni_bod_y, vojaci_kasarny_pravy_dolni_bod_y-26),
        ]
    seznam_vojaku.append(vojak)

pygame.init()

pygame.display.set_caption('pozor chodec')
okno = pygame.display.set_mode(ROZLISENI_OKNA)
x = vojaci_kasarny_levy_horni_bod_x
y = vojaci_kasarny_levy_horni_bod_y
dvere_otevreny = False
while True:
    udalosti = pygame.event.get()
    for u in udalosti:
        if u.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if u.type == pygame.KEYDOWN and u.key == pygame.K_SPACE:
            dvere_otevreny = not dvere_otevreny
            
    cas_ted = pygame.time.get_ticks()
    od_minula_ms = cas_ted - bod_v_case
    
    if od_minula_ms > 1000:  
        vojak = [
             random.randint(vojaci_kasarny_levy_horni_bod_x, vojaci_kasarny_pravy_dolni_bod_x-26),
             random.randint(vojaci_kasarny_levy_horni_bod_y, vojaci_kasarny_pravy_dolni_bod_y-26),
            ]
        seznam_vojaku.append(vojak)
        
        bod_v_case = cas_ted
        
    if dvere_otevreny and seznam_vojaku:
        vojak_nove_na_ceste = seznam_vojaku.pop()
        seznam_vojaku_na_ceste.append(vojak_nove_na_ceste)
        vojak_nove_na_ceste[0], vojak_nove_na_ceste[1] = startovni_pozice_cary_XY
    for v in seznam_vojaku_na_ceste:
        v[0] = v[0] + 1
            
            
            
   
    
            
    okno.fill(BARVA_POZADI)
    
    pygame.draw.rect(okno, (0,0,0), ((souradnice_kasaren_x, souradnice_kasaren_y), (velikost_kasaren_x, velikost_kasaren_y)))
    pygame.draw.rect(okno, (255,255,255), ((souradnice_bileho_obdelniku_x, souradnice_bileho_obdelniku_y) , (velikost_bileho_obdelniku_x, velikost_bileho_obdelniku_y)))
    pygame.draw.line(okno, (0,0,0), (startovni_pozice_cary_XY), (konecna_pozice_cary_XY), 5)
    for v in seznam_vojaku:
        pygame.draw.circle(okno,(255,8,0),v,5)
    for v in seznam_vojaku_na_ceste:
        pygame.draw.circle(okno,(255,8,0),v,5)
        
    pygame.display.update()