# zkouska na vybirani objektu a presckavani mezi nimi
import pygame
import sys

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 800, 600

BARVA_POZADI = 0, 0, 0
BARVA_OBJEKTU = 200, 30, 30
BARVA_OBJEKTU_ZVYRAZNENO = 255, 255, 255
BARVA_DRUHA = 0,255,0
w = 50
h = 50
w2 = 70
h2 = 70
rozdil_ctverecku = 10

k_left = False
k_right = False
povoleni_l = False
povoleni_r = False

pygame.init()

pygame.display.set_caption('Dots of War - ovládání')
okno = pygame.display.set_mode(ROZLISENI_OKNA)

seznam_objektu = [
                    {'pozice_x':150, 'pozice_y': 400, 'vybrano': True},
                    {'pozice_x':250, 'pozice_y': 400, 'vybrano': False},
                    {'pozice_x':350, 'pozice_y': 400, 'vybrano': False},
                    {'pozice_x':450, 'pozice_y': 400, 'vybrano': False},
                    {'pozice_x':550, 'pozice_y': 400, 'vybrano': False},
                    ]

sekundarni_seznam =[
                    {'pozice_x':150, 'pozice_y': 200, 'vybrano': True},
                    {'pozice_x':250, 'pozice_y': 200, 'vybrano': False},
                    {'pozice_x':350, 'pozice_y': 200, 'vybrano': False},
                    {'pozice_x':450, 'pozice_y': 200, 'vybrano': False},
                    {'pozice_x':550, 'pozice_y': 200, 'vybrano': False},
                   ]

aktivni = seznam_objektu
povoleni_a = True

def pohni():
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
            if aktivni == sekundarni_seznam:
                aktivni = seznam_objektu
            elif aktivni == seznam_objektu:
                aktivni = sekundarni_seznam
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
        
   
    okno.fill(BARVA_POZADI)        
           
    for objekt in seznam_objektu:
        
        if aktivni == seznam_objektu:
            if objekt['vybrano'] == True:
                pygame.draw.rect(okno, (BARVA_OBJEKTU_ZVYRAZNENO), (objekt['pozice_x'] - rozdil_ctverecku, objekt['pozice_y'] - rozdil_ctverecku, w2, h2))
                pygame.draw.rect(okno, (BARVA_OBJEKTU), (objekt['pozice_x'], objekt['pozice_y'], w, h))
            
        pygame.draw.rect(okno, (BARVA_OBJEKTU), (objekt['pozice_x'], objekt['pozice_y'], w, h))

    for objekt in sekundarni_seznam:
        
        if aktivni == sekundarni_seznam:
            if objekt['vybrano'] == True:
                pygame.draw.rect(okno, (BARVA_OBJEKTU_ZVYRAZNENO), (objekt['pozice_x'] - rozdil_ctverecku, objekt['pozice_y'] - rozdil_ctverecku, w2, h2))
                pygame.draw.rect(okno, (BARVA_DRUHA), (objekt['pozice_x'], objekt['pozice_y'], w, h))
            
        pygame.draw.rect(okno, (BARVA_DRUHA), (objekt['pozice_x'], objekt['pozice_y'], w, h))
    

    pygame.display.update()