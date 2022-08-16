import pgzrun
import wonsz
import random

WIERSZE = 10
KOLUMNY = 10
ROZMIAR_POLA = 64
WIDTH = KOLUMNY*ROZMIAR_POLA
HEIGHT = WIERSZE*ROZMIAR_POLA
KIERUNKI = {
    'lewo' : (-1,0),
    'prawo': (+1,0),
    'gora' : (0,-1),
    'dol'  : (0,+1),
}
suma_t = 0
punkty = 0

glowa = Actor('glowa')
ogon = Actor('ogon')
brzuch = Actor('brzuch')
zakret = Actor('zakret')
jabuszko = Actor('japko')
wsp_jablko = (2,2)

kuba = wonsz.Wonsz(5,5)

kierunek = 'gora'

def jaki_kierunek(segment1,segment2):
    x1,y1 = segment1.wspolrzedne
    x2,y2 = segment2.wspolrzedne

    if(x1==x2 and y1>y2):
        return "gora"
    if(x1==x2 and y1<y2):
        return "dol"
    if(x1>x2 and y1==y2):
        return "lewo"
    if(x1<x2 and y1==y2):
        return "prawo"


def narysuj_wonsza(w):
    obecna = w.glowa
    poprzednia = None
    while(obecna != None):
        obrazek = None
        kat = 0
        if(obecna == w.glowa):
            if(obecna.nastepna != None):
                kierunek = jaki_kierunek(obecna,obecna.nastepna)
                if(kierunek == "prawo"):
                    kat = 0
                if (kierunek == "dol"):
                    kat = 270
                if (kierunek == "lewo"):
                    kat = 180
                if (kierunek == "gora"):
                    kat = 90
                print(kierunek)
            obrazek = glowa
        elif(obecna.nastepna == None):
            kierunek = jaki_kierunek(obecna,poprzednia)
            if (kierunek == "prawo"):
                kat = 0
            if (kierunek == "dol"):
                kat = 270
            if (kierunek == "lewo"):
                kat = 180
            if (kierunek == "gora"):
                kat = 90
            print(kierunek)
            obrazek = ogon
        else:
            kierunek1 = jaki_kierunek(poprzednia,obecna)
            kierunek2 = jaki_kierunek(obecna,obecna.nastepna)
            if(kierunek1==kierunek2):
                obrazek = brzuch
            else:
                obrazek = zakret
        obrazek.topleft = obecna.wspolrzedne[0] * ROZMIAR_POLA, obecna.wspolrzedne[1] * ROZMIAR_POLA
        obrazek.angle = kat
        obrazek.draw()
        poprzednia = obecna
        obecna = obecna.nastepna

def draw():
    screen.fill((132,92,230))
    narysuj_wonsza(kuba)
    jabuszko.topleft = wsp_jablko[0] * ROZMIAR_POLA, wsp_jablko[1] * ROZMIAR_POLA
    jabuszko.draw()
    screen.draw.text(str(punkty).zfill(4), (10, 10), fontsize=60)

def update(t):
    x,y=kuba.glowa.wspolrzedne
    global suma_t,kierunek, wsp_jablko, punkty
    suma_t += t
    if(keyboard.left):
        kierunek = 'lewo'
    if (keyboard.right):
        # x = x + 1
        kierunek = 'prawo'
    if (keyboard.up):
        # y = y-1
        kierunek = 'gora'
    if (keyboard.down):
        # y = y + 1
        kierunek = 'dol'

    if(suma_t > 0.25):
        dx,dy = KIERUNKI[kierunek]
        x = (x+dx)%KOLUMNY
        y = (y+dy)%WIERSZE
        if ((x,y) in kuba):
            print('koniec')
            exit()
        kuba.wrzuc_na_poczatek(wonsz.Segment(x,y))
        if(kuba.glowa.wspolrzedne == wsp_jablko):
            while(True):
                wsp_jablko = (random.randint(0,KOLUMNY-1),random.randint(0,WIERSZE-1))
                if(wsp_jablko not in kuba):
                    break
            punkty += 1
        else:
            kuba.usun_ogon()
        print(len(kuba))
        suma_t = 0

pgzrun.go()