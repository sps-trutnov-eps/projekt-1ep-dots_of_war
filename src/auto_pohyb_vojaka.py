import pygame
import sys
import random
import math

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1800,900
BARVA_POZADI = 255,255,255

#hodnota pro čas, nepřepisovat.
bod_v_case = pygame.time.get_ticks()
bod2_v_case = pygame.time.get_ticks()
#velikost míčků == rad, velikost čár == w.
rad = 5
w = 5
w1 = 15

#Bod 1 bod, kam míček jde jako první.
bod1_y = ROZLISENI_Y - ROZLISENI_Y/3
bod1_x = 300

#Bod 2, bod kam vojáci chodí.
bod2_y = random.randint(0 + rad,ROZLISENI_Y/2 - rad)
bod2_x = random.randint(300 + rad,ROZLISENI_X - rad)

#bod 3, bod začáku základny.
bod3_x = rad
bod3_y = ROZLISENI_Y - ROZLISENI_Y/3

#bod 4, bod konce základny.
bod4_x = bod1_x
bod4_y = ROZLISENI_Y - rad

#zadání hodnot x a y, aby fungovali při randint vybírání.
bod3_x, bod4_x = min(bod3_x, bod4_x), max(bod3_x, bod4_x)
bod3_y, bod4_y = min(bod3_y, bod4_y), max(bod3_y, bod4_y)

#pohyb, neboli základní hodnoty pro pohyb. nepřepisovat, pokud tomu nerozumíš.
hledani_x = []
chozeni_x = -1
chodici_vojaci = []
chozeni = True

#začáteční hodnoty pro spawn vojáků. nepřepisovat, pokud tomu nerozumíš.
pocatecni_pocet_vojaku = 1
seznam_vojaku = []

#brána, která se otevírá
brana = False
x1 = bod4_x-100
y1 = bod3_y-12
h1 = 14
w1 = 100

x2 = bod1_x -2
y2 = bod1_y
h2 = 100
w2 = 14
#spawn prvního vojáka. nepřepisovat, pokud tomu nerozumíš.
for nabor in range(pocatecni_pocet_vojaku):
    vojak = [random.randint(bod3_x,bod4_x),random.randint(bod3_y,bod4_y)]
    seznam_vojaku.append(vojak)

pygame.init()

#název hry, a velikost okna.
pygame.display.set_caption('vojáci :D.')
okno = pygame.display.set_mode(ROZLISENI_OKNA)

#herní loop
while True:
    #mačkání tlačítek, a jejich akce.
    for event in  pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                       if brana == True:
                           brana = False
                       elif brana == False:
                           brana = True 
                       else:
                            chozeni_x = chozeni_x
    #hodnoty, které se tu potřebují načíst, aby fungoval časovač a pod.                              
    cas_ted = pygame.time.get_ticks()
    od_minula_ms = cas_ted - bod_v_case
    od_minula2_ms = cas_ted - bod2_v_case
    #spawn vojáků, taky se potřebuje načíst, aby fungoval spawn jak má. 
    vojak_x = random.randint(bod3_x,bod4_x-rad)
    vojak_y = random.randint(bod3_y+rad,bod4_y)
    #přidávání vojáků do seznam_vojaku, aby se na konci kódu mohli vykreslit.
    if od_minula_ms > 700:
        vojak = [vojak_x, vojak_y]
        seznam_vojaku.append(vojak)
        bod_v_case = cas_ted
        
    if od_minula2_ms > 800 and brana == True:
            chozeni_x += 1
            hledani_x.append(chozeni_x)
            seznam_vojaku = seznam_vojaku[1:]
            vojak_pochodovy = [bod1_x, bod3_y]
            chodici_vojaci.append(vojak_pochodovy)
            bod2_v_case = cas_ted
           
    elif od_minula2_ms > 800 and brana == False:
         bod2_v_case = cas_ted
        
    okno.fill(BARVA_POZADI)
    
    #vykreslovani vojaků v základně.
    for v in seznam_vojaku:
        pygame.draw.circle(okno,(255,8,0),v,rad)
    
    for v_p in chodici_vojaci:
        pygame.draw.circle(okno,(255,8,0),v_p,rad)
    
    #pohyb ze spawnu do 1 bodu, a následně do bodu dalšího.
    for x_1 in hledani_x:
     #pohyb_x prvniho vojaka, a následně následujícího.
        
        if chozeni:
            a = math.atan2(bod2_y - chodici_vojaci[x_1][1],bod2_x - chodici_vojaci[x_1][0])
            b = math.atan2( bod1_y - chodici_vojaci[x_1][1], bod1_x - chodici_vojaci[x_1][0]) 
            chodici_vojaci[x_1][0] += 0.5 *math.cos(a)
            chodici_vojaci[x_1][1] += 0.5 *math.sin(a)
                
                
        else:
            chozeni_x = chozeni_x
    
    if brana == True:
        if x1 < bod1_x - 99 and x1 > bod1_x - 198 :
            x1 -= 0.2
            y2 += 0.2
    if brana == False:
        if x1 < bod1_x - 101 and x1 > bod1_x - 199:
            x1 += 0.2
            y2 -= 0.2
    
    
    #vykreslovani základny a pod.
    pygame.draw.line(okno,(0,0,0),(0,bod3_y-1),(bod4_x-100,bod3_y-1),w)
    pygame.draw.line(okno,(0,0,0),(bod4_x,bod3_y+100),(bod4_x,ROZLISENI_Y),w)
    pygame.draw.line(okno,(0,0,0),(bod1_x,bod1_y),(bod2_x,bod2_y),w)  
    pygame.draw.rect(okno, (0,0,0), (x1, y1, w1, h1))
    pygame.draw.rect(okno, (0,0,0), (x2, y2, w2, h2))
    #display update :D
    pygame.display.update()
    