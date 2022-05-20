import pygame
import sys
import random


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
konecna_pozice_cary_XY = 850, 775

souradnice_dveri_otevrenych_x = 250
souradnice_dveri_otevrenych_y = 785
velikost_dveri_otevrenych_x = 100
velikost_dveri_otevrenych_y = 15

souradnice_dveri_zavrenych_x = 250
souradnice_dveri_zavrenych_y = 725
velikost_dveri_zavrenych_x = 15
velikost_dveri_zavrenych_y = 100

rychlost_vojaka = 0.5


####### Souřadnice kasáren levého horního bodu #######
vojaci_kasarny_levy_horni_bod_y = souradnice_bileho_obdelniku_y
vojaci_kasarny_levy_horni_bod_x = souradnice_bileho_obdelniku_x

####### Souřadnice kasáren pravého dolního bodu #######
vojaci_kasarny_pravy_dolni_bod_y = souradnice_bileho_obdelniku_y + velikost_kasaren_y
vojaci_kasarny_pravy_dolni_bod_x = souradnice_bileho_obdelniku_x + velikost_kasaren_x

####### Nábor vojáků #######
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

pygame.display.set_caption('spawn vojáků')
okno = pygame.display.set_mode(ROZLISENI_OKNA)
dvere_otevreny = False
while True:
    udalosti = pygame.event.get()
    for u in udalosti:
        if u.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if u.type == pygame.KEYDOWN and u.key == pygame.K_SPACE:
            dvere_otevreny = not dvere_otevreny
        if u.type == pygame.KEYDOWN and u.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
            
            
        ####### Spawnování vojáků #######  
    doba_od_uplynuti_spawnu_vojaka  = pygame.time.get_ticks() - cas_spawnu_posledniho_vojaka
    
    if doba_od_uplynuti_spawnu_vojaka > 1000:
        vojak = [
             random.randint(vojaci_kasarny_levy_horni_bod_x, vojaci_kasarny_pravy_dolni_bod_x-26),
             random.randint(vojaci_kasarny_levy_horni_bod_y, vojaci_kasarny_pravy_dolni_bod_y-26),
            ]
        seznam_vojaku.append(vojak)
        
        cas_spawnu_posledniho_vojaka = pygame.time.get_ticks()
        
         ####### Otevření dveří #######
    doba_od_odchodu_posledniho_vojaka_na_frontu = pygame.time.get_ticks() - cas_odchodu_posledniho_vojaka_na_frontu
    
    if doba_od_odchodu_posledniho_vojaka_na_frontu > 500:
        if dvere_otevreny and seznam_vojaku:
            vojak_nove_na_ceste = seznam_vojaku.pop()
            seznam_vojaku_na_ceste.append(vojak_nove_na_ceste)
            vojak_nove_na_ceste[0], vojak_nove_na_ceste[1] = startovni_pozice_cary_XY
            cas_odchodu_posledniho_vojaka_na_frontu = pygame.time.get_ticks()
        
            
    doba_od_posledniho_pohybu_vojaku_na_ceste = pygame.time.get_ticks() - cas_od_posledniho_pohybu_vojaku_na_ceste
    
    if doba_od_posledniho_pohybu_vojaku_na_ceste > 500:
        for v in seznam_vojaku_na_ceste:
            v[0] += 25
            
 
        cas_od_posledniho_pohybu_vojaku_na_ceste = pygame.time.get_ticks()
            
   
    
          ####### Vykreslování tvarů #######   
    okno.fill(BARVA_POZADI)
    
    pygame.draw.rect(okno, (0,0,0), ((souradnice_kasaren_x, souradnice_kasaren_y), (velikost_kasaren_x, velikost_kasaren_y)))
    pygame.draw.rect(okno, (255,255,255), ((souradnice_bileho_obdelniku_x, souradnice_bileho_obdelniku_y), (velikost_bileho_obdelniku_x, velikost_bileho_obdelniku_y)))
    pygame.draw.line(okno, (0,0,0), (startovni_pozice_cary_XY), (konecna_pozice_cary_XY), 5)
    if dvere_otevreny == False:
        pygame.draw.rect(okno, (0,255,0), ((souradnice_dveri_zavrenych_x, souradnice_dveri_zavrenych_y), (velikost_dveri_zavrenych_x, velikost_dveri_zavrenych_y)))
    if dvere_otevreny == True:
        pygame.draw.rect(okno, (0,255,0), ((souradnice_dveri_otevrenych_x, souradnice_dveri_otevrenych_y), (velikost_dveri_otevrenych_x, velikost_dveri_otevrenych_y)))  
    for v in seznam_vojaku:
        pygame.draw.circle(okno,(255,8,0),v,5)
    for v in seznam_vojaku_na_ceste:
        pygame.draw.circle(okno,(255,8,0),v,5)
        
    pygame.display.update()