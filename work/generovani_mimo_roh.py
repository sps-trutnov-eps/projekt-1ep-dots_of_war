import sys
import random
import pygame
pygame.init()

ROZLISENI = ROZLISENI_X, ROZLISENI_Y = 600, 600
RAMENO_VYREZU = 200

okno = pygame.display.set_mode(ROZLISENI)
pygame.display.set_caption('Generování mimo roh')

def nevyhovujici_souradnice(x, y):
    return x + y < RAMENO_VYREZU

def vygenerovat_krouzek():
    global krouzky
    
    x = y = 0
    
    while nevyhovujici_souradnice(x, y):
        x = random.randint(0, ROZLISENI_X)
        y = random.randint(0, ROZLISENI_Y)
    
    krouzky.append([x, y])
    if len(krouzky) > 5e3:
        krouzky = []

krouzky = []

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if udalost.type == pygame.KEYDOWN and udalost.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

    vygenerovat_krouzek()

    okno.fill((255, 255, 255))
    for krouzek in krouzky:
        pygame.draw.circle(okno, (255, 0, 0), krouzek, 5)
    pygame.display.update()
