# zkouska na vybirani objektu a presckavani mezi nimi
import pygame
import sys
from map import mapa

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 800, 600

BARVA_POZADI = 0, 0, 0
BARVA_OBJEKTU = 200, 30, 30
BARVA_OBJEKTU_ZVYRAZNENO = 255, 255, 255
BARVA_DRUHA = 0,255,0
w = 50
h = 50
w2 = 18
h2 = 30
rozdil_ctverecku = 10

pygame.init()

pygame.display.set_caption('Dots of War - ovládání')
okno = pygame.display.set_mode(ROZLISENI_OKNA)

k_left = False
k_right = False
povoleni_l = False
povoleni_r = False
povoleni_a = True
aktivni = mapa["vyhybky_s"]

def pohni(mapa):
    global k_right
    global k_left
    global povoleni_r
    global povoleni_l
    global povoleni_a
    global aktivni
    udalosti = pygame.event.get()
    stisknuto = pygame.key.get_pressed()
    
    # vypnuti aplikace
    for u in udalosti:
        if u.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if stisknuto[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
    
    # stisk klavesy RIGHT
    if k_right == False:
        if stisknuto[pygame.K_RIGHT]:
            povoleni_r = True
            k_right = True
            
    if k_right == True:
        if stisknuto[pygame.K_RIGHT] == False:
            k_right = False
            
    # stisk klavesy LEFT
    if k_left == False:
        if stisknuto[pygame.K_LEFT]:
            povoleni_l = True
            k_left = True
            
    if k_left == True:
        if stisknuto[pygame.K_LEFT] == False:
            k_left = False
            
    # Přepínání mezi seznamy
    if stisknuto[pygame.K_UP] or stisknuto[pygame.K_DOWN]:
        if povoleni_a == True:
            povoleni_a = False
            if aktivni == mapa["vyhybky_s"]:
                aktivni = mapa["veze_s"]
            elif aktivni == mapa["veze_s"]:
                aktivni = mapa["vyhybky_s"]
    else:
        povoleni_a = True
    
    # vybrani dalsiho objektu pri stisku klavesy RIGHT
    if povoleni_r == True:
        for i, objekt in enumerate(aktivni):
            if aktivni[i]['vybrano'] == True:
                aktivni[(i + 1) % len(aktivni)]['vybrano'] = True
                aktivni[i]['vybrano'] = False
                break
        povoleni_r = False
                    
    # vybrani dalsiho objektu pri stisku klavesy LEFT
    if povoleni_l == True:
        for i, objekt in enumerate(aktivni):
            if aktivni[i]['vybrano'] == True:
                aktivni[(i - 1) % len(aktivni)]['vybrano'] = True
                aktivni[i]['vybrano'] = False
                break
        povoleni_l = False         
    
    for objekt in mapa["vyhybky_s"]:
        
        if aktivni == mapa["vyhybky_s"]:
            if objekt['vybrano'] == True:
                pygame.draw.circle(okno, (BARVA_OBJEKTU_ZVYRAZNENO), (objekt['pozice'][0] * 150, objekt['pozice'][1] * 150), 15)
                print("kreslím")

    for objekt in mapa["veze_s"]:
        
        if aktivni == mapa["veze_s"]:
            if objekt['vybrano'] == True:
                pygame.draw.rect(okno, (BARVA_OBJEKTU_ZVYRAZNENO), ((objekt['pozice'][0] * 150) -9, (objekt['pozice'][1] * 150) - 15, w2, h2))
                
    return mapa