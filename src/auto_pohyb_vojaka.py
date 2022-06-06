import pygame
import sys
import random
import math

def spawni(seznam_vojaku, mapa, zakladna):
    rameno = 75 + 7.07
    x = y = 0
    while (x + y) < rameno:
        x = random.randint(5, 220)
        y = random.randint(5, 220)
        
    if zakladna == mapa["zakladna_s"]:
        x += 675
        y = (75 - y) + 150
    elif zakladna == mapa["zakladna_j"]:
        y += 675
        x = (75 - x) + 150
        
    vojak = [x, y]
    seznam_vojaku.append(vojak)
    return seznam_vojaku
    
def pust(mapa, seznam_vojaku, seznam_vojaku_na_ceste, brany):
    for brana in brany:
        if brana["stav"] == True:
            if seznam_vojaku != []:
                vojak_nove_na_ceste = seznam_vojaku[0]
                seznam_vojaku.remove(seznam_vojaku[0])
                seznam_vojaku_na_ceste.append(vojak_nove_na_ceste)
                vojak_nove_na_ceste[0], vojak_nove_na_ceste[1] = brana["pozice"][0], brana["pozice"][1]
                if brana == mapa["brany_j"][0]:
                    vojak_nove_na_ceste.append(mapa["body"][22])
                elif brana == mapa["brany_j"][1]:
                    vojak_nove_na_ceste.append(mapa["body"][30])
                elif brana == mapa["brany_j"][2]:
                    vojak_nove_na_ceste.append(mapa["body"][38])
                elif brana == mapa["brany_s"][0]:
                    vojak_nove_na_ceste.append(mapa["body"][10])
                elif brana == mapa["brany_s"][1]:
                    vojak_nove_na_ceste.append(mapa["body"][18])
                elif brana == mapa["brany_s"][2]:
                    vojak_nove_na_ceste.append(mapa["body"][26])
            else:
                pass
            return seznam_vojaku, seznam_vojaku_na_ceste
        else:
            pass

def pohni(seznam_vojaku_na_ceste):
    for v in seznam_vojaku_na_ceste:
        uhel = math.atan2((v[2][1] - v[1]),(v[2][0] - v[0]))
        posun_x = math.cos(uhel) * 0.25
        posun_y = math.sin(uhel) * 0.25
        v[0] += posun_x
        v[1] += posun_y
    return seznam_vojaku_na_ceste