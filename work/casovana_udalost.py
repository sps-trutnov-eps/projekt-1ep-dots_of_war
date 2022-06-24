import sys
import random
import pygame
pygame.init()

ROZLISENI = ROZLISENI_X, ROZLISENI_Y = 400, 600
INTERVAL_UDALOSTI_1_MS = 1000
INTERVAL_UDALOSTI_2_MS = 300

def nastal_cas_1():
    global x, y
    
    x = random.randint(0, ROZLISENI_X)
    y = random.randint(0, ROZLISENI_Y)
    
def nastal_cas_2():
    global r, g, b
    
    r = random.randint(10, 240)
    g = random.randint(10, 240)
    b = random.randint(10, 240)

okno = pygame.display.set_mode(ROZLISENI)
pygame.display.set_caption('Časovaná událost')

nastal_cas_1()
nastal_cas_2()
casovana_udalost_1 = pygame.USEREVENT + 0
casovana_udalost_2 = pygame.USEREVENT + 1
pygame.time.set_timer(casovana_udalost_1, INTERVAL_UDALOSTI_1_MS)
pygame.time.set_timer(casovana_udalost_2, INTERVAL_UDALOSTI_2_MS)

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if udalost.type == casovana_udalost_1:
            nastal_cas_1()
        if udalost.type == casovana_udalost_2:
            nastal_cas_2()
    
    okno.fill((255, 255, 255))
    pygame.draw.circle(okno, (r, g, b), (x, y), 20)
    pygame.display.update()
