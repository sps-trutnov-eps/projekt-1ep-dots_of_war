# zkouska na vybirani objektu a presckavani mezi nimi
import pygame
import sys

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 800, 600

BARVA_POZADI = 0, 0, 0
BARVA_OBJEKTU = 200, 30, 30
BARVA_OBJEKTU_ZVYRAZNENO = 255, 255, 255
w = 50
h = 50
w2 = 70
h2 = 70
rozdil_ctverecku = 10


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


while True:
    udalosti = pygame.event.get()
    stisknuto = pygame.key.get_pressed()

    for u in udalosti:
        if u.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if stisknuto[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
            
        if stisknuto[pygame.K_RIGHT]:
            for i, objekt in enumerate(seznam_objektu):
                seznam_objektu[i + 1]['vybrano'] = True
                break
                    
                objekt['vybrano'] = False 
                    
                    
                    
            
        
    okno.fill(BARVA_POZADI)        
           
    for objekt in seznam_objektu:
        
        if objekt['vybrano'] == True:
            pygame.draw.rect(okno, (BARVA_OBJEKTU_ZVYRAZNENO), (objekt['pozice_x'] - rozdil_ctverecku, objekt['pozice_y'] - rozdil_ctverecku, w2, h2))
            pygame.draw.rect(okno, (BARVA_OBJEKTU), (objekt['pozice_x'], objekt['pozice_y'], w, h))
            
        pygame.draw.rect(okno, (BARVA_OBJEKTU), (objekt['pozice_x'], objekt['pozice_y'], w, h))

    

    pygame.display.update()