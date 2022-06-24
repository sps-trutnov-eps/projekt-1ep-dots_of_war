# zkouska na vybirani objektu a presckavani mezi nimi
import pygame
import sys
from mapa import mapa

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 900, 900

BARVA_POZADI = 0, 0, 0
BARVA_OBJEKTU = 200, 30, 30
BARVA_OZNACENI_SEVER = 200, 200, 255
BARVA_OZNACENI_JIH = 255, 200, 200
CENA_VEZE = 15
HP_VEZE = 25
w = 50
h = 50
w2 = 18
h2 = 30
rozdil_ctverecku = 10

okno = pygame.display.set_mode(ROZLISENI_OKNA)

k_left = False
k_right = False
k_a = False
k_d = False
povoleni_l = False
povoleni_r = False
povoleni_a = False
povoleni_d = False
povoleni_prepnuti_s = True
povoleni_prepnuti_j = True
povoleni_prehozeni_s = True
povoleni_prehozeni_j = True
povoleni_brany_s = True
povoleni_brany_j = True
aktivni_s = mapa["vyhybky_s"]
aktivni_j = mapa["vyhybky_j"]

def oznac(mapa):
    global k_right
    global k_left
    global k_a
    global k_d
    global povoleni_r
    global povoleni_l
    global povoleni_a
    global povoleni_d
    global povoleni_prepnuti_s
    global povoleni_prepnuti_j
    global aktivni_s
    global aktivni_j
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
            
    # stisk klavesy A
    if k_a == False:
        if stisknuto[pygame.K_a]:
            povoleni_a = True
            k_a = True
            
    if k_a == True:
        if stisknuto[pygame.K_a] == False:
            k_a = False
            
    # stisk klavesy D
    if k_d == False:
        if stisknuto[pygame.K_d]:
            povoleni_d = True
            k_d = True
            
    if k_d == True:
        if stisknuto[pygame.K_d] == False:
            k_d = False
            
    # Přepínání mezi seznamy - Sever
    if stisknuto[pygame.K_UP] or stisknuto[pygame.K_DOWN]:
        if povoleni_prepnuti_s == True:
            povoleni_prepnuti_s = False
            if aktivni_s == mapa["vyhybky_s"]:
                aktivni_s = mapa["veze_s"]
            elif aktivni_s == mapa["veze_s"]:
                aktivni_s = mapa["vyhybky_s"]
    else:
        povoleni_prepnuti_s = True
        
    # Přepínání mezi seznamy - Jih
    if stisknuto[pygame.K_s] or stisknuto[pygame.K_w]:
        if povoleni_prepnuti_j == True:
            povoleni_prepnuti_j = False
            if aktivni_j == mapa["vyhybky_j"]:
                aktivni_j = mapa["veze_j"]
            elif aktivni_j == mapa["veze_j"]:
                aktivni_j = mapa["vyhybky_j"]
    else:
        povoleni_prepnuti_j = True
    
    # vybrani dalsiho objektu pri stisku klavesy RIGHT
    if povoleni_r == True:
        for i, objekt in enumerate(aktivni_s):
            if aktivni_s[i]['vybrano'] == True:
                aktivni_s[(i + 1) % len(aktivni_s)]['vybrano'] = True
                aktivni_s[i]['vybrano'] = False
                break
        povoleni_r = False
                    
    # vybrani dalsiho objektu pri stisku klavesy LEFT
    if povoleni_l == True:
        for i, objekt in enumerate(aktivni_s):
            if aktivni_s[i]['vybrano'] == True:
                aktivni_s[(i - 1) % len(aktivni_s)]['vybrano'] = True
                aktivni_s[i]['vybrano'] = False
                break
        povoleni_l = False
        
    # vybrani dalsiho objektu pri stisku klavesy A
    if povoleni_a == True:
        for i, objekt in enumerate(aktivni_j):
            if aktivni_j[i]['vybrano'] == True:
                aktivni_j[(i - 1) % len(aktivni_j)]['vybrano'] = True
                aktivni_j[i]['vybrano'] = False
                break
        povoleni_a = False
                    
    # vybrani dalsiho objektu pri stisku klavesy D
    if povoleni_d == True:
        for i, objekt in enumerate(aktivni_j):
            if aktivni_j[i]['vybrano'] == True:
                aktivni_j[(i + 1) % len(aktivni_j)]['vybrano'] = True
                aktivni_j[i]['vybrano'] = False
                break
        povoleni_d = False
    
    for objekt in mapa["vyhybky_s"]:
        
        if aktivni_s == mapa["vyhybky_s"]:
            if objekt['vybrano'] == True:
                pygame.draw.circle(okno, (BARVA_OZNACENI_SEVER), (objekt['pozice'][0] * 150, objekt['pozice'][1] * 150), 15)

    for objekt in mapa["veze_s"]:
        
        if aktivni_s == mapa["veze_s"]:
            if objekt['vybrano'] == True:
                pygame.draw.rect(okno, (BARVA_OZNACENI_SEVER), ((objekt['pozice'][0] * 150) -9, (objekt['pozice'][1] * 150) - 15, w2, h2))
                
    for objekt in mapa["vyhybky_j"]:
        
        if aktivni_j == mapa["vyhybky_j"]:
            if objekt['vybrano'] == True:
                pygame.draw.circle(okno, (BARVA_OZNACENI_JIH), (objekt['pozice'][0] * 150, objekt['pozice'][1] * 150), 15)

    for objekt in mapa["veze_j"]:
        
        if aktivni_j == mapa["veze_j"]:
            if objekt['vybrano'] == True:
                pygame.draw.rect(okno, (BARVA_OZNACENI_JIH), ((objekt['pozice'][0] * 150) -9, (objekt['pozice'][1] * 150) - 15, w2, h2))
                
    return mapa

def prehod(mapa, seznam_vojaku_s, seznam_vojaku_j):
    global povoleni_prehozeni_s
    global povoleni_prehozeni_j
    
    stisk = pygame.key.get_pressed()
    
    if stisk[pygame.K_RCTRL]:
        if povoleni_prehozeni_s:
            povoleni_prehozeni_s = False
            for vec in aktivni_s:
                if aktivni_s == mapa["vyhybky_s"]:
                    if vec["vybrano"]:
                        if vec["stav"] == True:
                            vec["stav"] = False
                        elif vec["stav"] == False:
                            vec["stav"] = True
                else:
                    if vec["vybrano"]:
                        if len(seznam_vojaku_s) > CENA_VEZE and not vec["hp"] == HP_VEZE:
                            for i in range(CENA_VEZE):
                                seznam_vojaku_s.pop()
                            vec["hp"] = HP_VEZE
                        else:
                            pass          
    else:
        povoleni_prehozeni_s = True
        
    if stisk[pygame.K_SPACE]:
        if povoleni_prehozeni_j:
            povoleni_prehozeni_j = False
            for vec in aktivni_j:
                if aktivni_j == mapa["vyhybky_j"]:
                    if vec["vybrano"]:
                        if vec["stav"] == True:
                            vec["stav"] = False
                        elif vec["stav"] == False:
                            vec["stav"] = True
                else:
                    if vec["vybrano"]:
                        if len(seznam_vojaku_j) > CENA_VEZE and not vec["hp"] == HP_VEZE:
                            for i in range(CENA_VEZE):
                                seznam_vojaku_j.pop()
                            vec["hp"] = HP_VEZE
                        else:
                            pass
    else:
        povoleni_prehozeni_j = True
        
def brany(mapa):
    global povoleni_brany_s
    global povoleni_brany_j
    stisk = pygame.key.get_pressed()
    #Sever
    if stisk[pygame.K_KP0] and povoleni_brany_s:
        for x in mapa["brany_s"]:
            x["stav"] = False
    
    if stisk[pygame.K_KP1] and povoleni_brany_s:
        povoleni_brany_s = False
        if mapa["brany_s"][0]["stav"] == True:
            for x in mapa["brany_s"]:
                x["stav"] = False
        else:
            for x in mapa["brany_s"]:
                x["stav"] = False
            mapa["brany_s"][0]["stav"] = True

    if stisk[pygame.K_KP2] and povoleni_brany_s:
        povoleni_brany_s = False
        if mapa["brany_s"][1]["stav"] == True:
            for x in mapa["brany_s"]:
                x["stav"] = False
        else:
            for x in mapa["brany_s"]:
                x["stav"] = False
            mapa["brany_s"][1]["stav"] = True
            
    if stisk[pygame.K_KP3] and povoleni_brany_s:
        povoleni_brany_s = False
        if mapa["brany_s"][2]["stav"] == True:
            for x in mapa["brany_s"]:
                x["stav"] = False
        else:
            for x in mapa["brany_s"]:
                x["stav"] = False
            mapa["brany_s"][2]["stav"] = True
    
    if not stisk[pygame.K_KP1] and not stisk[pygame.K_KP2] and not stisk[pygame.K_KP3] and not sitsk[pygame.K_KP0]:
        povoleni_brany_s = True
    
    #Jih
    if stisk[pygame.K_SEMICOLON] andpovoleni_brany_j:
        for x in mapa["brany_j"]:
                x["stav"] = False
        
    if stisk[pygame.K_1] and povoleni_brany_j:
        povoleni_brany_j = False
        if mapa["brany_j"][0]["stav"] == True:
            for x in mapa["brany_j"]:
                x["stav"] = False
        else:
            for x in mapa["brany_j"]:
                x["stav"] = False
            mapa["brany_j"][0]["stav"] = True
            
    if stisk[pygame.K_2] and povoleni_brany_j:
        povoleni_brany_j = False
        if mapa["brany_j"][1]["stav"] == True:
            for x in mapa["brany_j"]:
                x["stav"] = False
        else:
            for x in mapa["brany_j"]:
                x["stav"] = False
            mapa["brany_j"][1]["stav"] = True
            
    if stisk[pygame.K_3] and povoleni_brany_j:
        povoleni_brany_j = False
        if mapa["brany_j"][2]["stav"] == True:
            for x in mapa["brany_j"]:
                x["stav"] = False
        else:
            for x in mapa["brany_j"]:
                x["stav"] = False
            mapa["brany_j"][2]["stav"] = True
            
    if not stisk[pygame.K_1] and not stisk[pygame.K_2] and not stisk[pygame.K_3] and not stisk[pygame.K_SEMICOLON]:
        povoleni_brany_j = True