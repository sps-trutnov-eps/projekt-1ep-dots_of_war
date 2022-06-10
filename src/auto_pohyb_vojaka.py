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

def rozhodni_cestu(mapa, vojak, strana):
    if strana == "s":
        trasa = None
        for vyhybka in mapa["vyhybky_s"]:
            if round(vojak[0]) == vyhybka["pozice"][0] and round(vojak[1]) == vyhybka["pozice"][1]:
                if vyhybka["stav"] == True:
                    smer = vyhybka["rozcesti"][1]
                else:
                    smer = vyhybka["rozcesti"][0]
                 
                for i, bod in enumerate(mapa["body"]):
                    if bod == vojak[2]:
                       momentalni_bod = i
                       break
                
                if smer == "Z":
                   vojak[2] = mapa["body"][momentalni_bod-1]
                elif smer == "JZ":
                   vojak[2] = mapa["body"][momentalni_bod+6]
                elif smer == "J":
                   vojak[2] = mapa["body"][momentalni_bod+7]
                
                trasa = "mám"
                return vojak
            
        for vyhybka in mapa["vyhybky_j"]:
            if round(vojak[0]) == vyhybka["pozice"][0] and round(vojak[1]) == vyhybka["pozice"][1]:
                cesta1 = None
                cesta2 = None
                cesta3 = None
                for cesta in mapa["cesty"]:
                    if vyhybka["pozice"] in cesta:
                        if cesta1 == None:
                            cesta1 = cesta
                        elif cesta1 != None and cesta2 == None:
                            cesta2 = cesta
                        elif cesta1 != None and cesta2 != None and cesta3 == None:
                            cesta3 = cesta
                            break
                
                cislovane_cesty = [cesta1, cesta2, cesta3]
                
                cislo_vyhybky = None
                
                for i, bod in enumerate(mapa["body"]):
                    if bod == vyhybka["pozice"]:
                        cislo_vyhybky = i
                        break
                
                for cesta in cislovane_cesty:
                    for bod in cesta:
                        if bod == mapa["body"][cislo_vyhybky-1] or bod == mapa["body"][cislo_vyhybky+6] or bod == mapa["body"][cislo_vyhybky+7]:
                            vojak[2] = bod
                            break
                        
                trasa = "mám"
                return vojak
        
        if trasa == None:
            vojakova_cesta = "není"
            for bod in mapa["body"]:
                if round(vojak[0]) == bod[0] and round(vojak[1]) == bod[1]:
                    for cesta in mapa["cesty"]:
                        if bod in cesta:
                            vojakova_cesta = cesta
                            break
                    for i, kus in enumerate(vojakova_cesta):
                        if kus == bod:
                            break
                    if i == 0 or i == len(vojakova_cesta):
                        pocitani = 0
                        for i, cesta in enumerate(mapa["cesty"]):
                            if pozice_vojaka in cesta:
                                if pocitani < 1:
                                    pocitani += 1
                                else:
                                    vojakova_cesta = cesta
                                    bod_cesty = i
                else:
                    if vojakova_cesta == "není":
                        pass
                    else:
                        vojak[2] = (vojakova_cesta[i-1][0], vojakova_cesta[i-1][1])

def pohni(mapa, seznam_vojaku_na_ceste, strana):
    for v in seznam_vojaku_na_ceste:
        if v[2][0] == round(v[0], 2) and v[2][1] == round(v[1], 2):
            rozhodni_cestu(mapa, v, strana)
        else:
            uhel = math.atan2((v[2][1] - v[1]),(v[2][0] - v[0]))
            posun_x = math.cos(uhel) * 0.01
            posun_y = math.sin(uhel) * 0.01
            v[0] += posun_x
            v[1] += posun_y
    return seznam_vojaku_na_ceste
