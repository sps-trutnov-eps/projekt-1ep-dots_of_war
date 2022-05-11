import pygame
import sys
import random
import math

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1800,900
BARVA_POZADI = 255,255,255

#hodnota pro čas, nepřepisovat.
bod_v_case = pygame.time.get_ticks()

#velikost míčků == rad, velikost čár == w.
rad = 5
w = 5

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

#začáteční hodnoty pro spawn vojáků. nepřepisovat, pokud tomu nerozumíš.
pocatecni_pocet_vojaku = 1
seznam_vojaku = []


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
                       if chozeni_x < len(seznam_vojaku):
                            chozeni_x += 1
                            hledani_x.append(chozeni_x)
                        
                       else:
                            chozeni_x = chozeni_x
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                       if chozeni_x + 30 < len(seznam_vojaku):
                         for i in range(30):
                            chozeni_x += 1
                            hledani_x.append(chozeni_x)        
                       else:
                            chozeni_x = chozeni_x
    #hodnoty, které se tu potřebují načíst, aby fungoval časovač a pod.                              
    cas_ted = pygame.time.get_ticks()
    od_minula_ms = cas_ted - bod_v_case
    #spawn vojáků, taky se potřebuje načíst, aby fungoval spawn jak má. 
    vojak_x = random.randint(bod3_x,bod4_x-rad)
    vojak_y = random.randint(bod3_y+rad,bod4_y)
    #přidávání vojáků do seznam_vojaku, aby se na konci kódu mohli vykreslit.
    if od_minula_ms > 700:
        vojak = [vojak_x, vojak_y]
        seznam_vojaku.append(vojak)
        bod_v_case = cas_ted
        
    
      
        
    okno.fill(BARVA_POZADI)
    
    #vykreslovani vojaků v základně.
    for v in seznam_vojaku:
        pygame.draw.circle(okno,(255,8,0),v,rad)
    
    #pohyb ze spawnu do 1 bodu, a následně do bodu dalšího.
    for x_1 in hledani_x:
     #pohyb_x prvniho vojaka, a následně následujícího.
        if chozeni_x < len(seznam_vojaku):
            a = math.atan2(bod2_y - seznam_vojaku[x_1][1],bod2_x - seznam_vojaku[x_1][0])
            b = math.atan2( bod1_y - seznam_vojaku[x_1][1], bod1_x - seznam_vojaku[x_1][0]) 
            if seznam_vojaku[x_1][0] <= bod1_x and seznam_vojaku[x_1][1] >= bod1_y:
                seznam_vojaku[x_1][0] += 0.5 * math.cos(b)
                seznam_vojaku[x_1][1] += 0.5 * math.sin(b)
            else:
                seznam_vojaku[x_1][0] += 0.5 * math.cos(a)
                seznam_vojaku[x_1][1] += 0.5 * math.sin(a)
            
                
                
        else:
            chozeni_x = chozeni_x
    
    #jen text, do def se mi nechtěl dávat, jelikož by to bylo více nepřehledné nahoře.
    font = pygame.font.Font('freesansbold.ttf', 25)
    pocet_vojaku_na_ceste = font.render('útočící_vojáci: ' + str(len(hledani_x)), True, (0,0,8))
    okno.blit(pocet_vojaku_na_ceste, (10, 50))
    
    pocet_vojaku_k_dispozici = int(len(seznam_vojaku) - int(len(hledani_x)))
    pocet_vojaku = font.render('vojáci_k_dispozici: ' + str(pocet_vojaku_k_dispozici), True, (0,0,8))
    okno.blit(pocet_vojaku, (10, 10))
    
    #vykreslovani základny a pod.
    pygame.draw.line(okno,(0,0,0),(0,bod3_y),(bod4_x,bod3_y),w)
    pygame.draw.line(okno,(0,0,0),(bod4_x,bod3_y),(bod4_x,ROZLISENI_Y),w)
    pygame.draw.line(okno,(0,0,0),(bod1_x,bod1_y),(bod2_x,bod2_y),w)  
    
    #display update :D
    pygame.display.update()