body = [
    (0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), 
    (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), #7
    (0,2), (1,2), (2,2), (3,2), (4,2), (5,2), (6,2), #14
    (0,3), (1,3), (2,3), (3,3), (4,3), (5,3), (6,3), #21
    (0,4), (1,4), (2,4), (3,4), (4,4), (5,4), (6,4), #28
    (0,5), (1,5), (2,5), (3,5), (4,5), (5,5), (6,5), #35
    (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6),
        ]

vyhybky = [
    {"pozice":body[10],"stav":False ,"hrac":"s"},
    {"pozice":body[16],"stav":False ,"hrac":"s"}, {"pozice":body[18],"stav":False ,"hrac":"s"},
    {"pozice":body[22],"stav":False ,"hrac":"j"}, {"pozice":body[23],"stav":False ,"hrac":"j"}, {"pozice":body[25],"stav":False ,"hrac":"s"}, {"pozice":body[26],"stav":False ,"hrac":"s"},
    {"pozice":body[30],"stav":False ,"hrac":"j"}, {"pozice":body[32],"stav":False ,"hrac":"j"},
    {"pozice":body[38],"stav":False ,"hrac":"j"},
          ]

cesty = [
    (body[22], body[15], body[9], body[10]), (body[10], body[12]), #A, B
    (body[16], body[10]), (body[18], body[12]), #C, D
    (body[22], body[16]), (body[23], body[16]), (body[23], body[17], body[18]), (body[25], body[18]), (body[26], body[12]), #E, F, G, H, R
    (body[30], body[23]), (body[30], body[31], body[25]), (body[32], body[25]), (body[32], body[26]), #I, J, K, L
    (body[36], body[22]), (body[36], body[30]), (body[36], body[38]), (body[38], body[32]), (body[38], body[39], body[33], body[26]) #M, N, O, P, Q
        ]

mapa = {"body":body,"vyhybky":vyhybky,"cesty":cesty}
