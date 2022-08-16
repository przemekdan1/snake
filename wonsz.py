class Segment:
    def __init__(self,x,y):
        self.wspolrzedne = (x,y)
        self.nastepna = None

    def __str__(self):
        return f'{self.wspolrzedne}'

x = Segment(5,7)
print(x)

class Wonsz:
    def __init__(self,x,y):
        self.glowa = Segment(x,y)

    def __str__(self):
        obecna = self.glowa
        wynik = '>~'
        while(obecna != None):
            wynik += str(obecna)
            obecna = obecna.nastepna
        return wynik

    def __len__(self):
        obecna = self.glowa
        licznik = 0
        while(obecna != None):
            licznik += 1
            obecna = obecna.nastepna
        return licznik

    def wrzuc_na_poczatek(self, segment):
        segment.nastepna = self.glowa
        self.glowa = segment

    def usun_ogon(self):
        obecna = self.glowa
        poprzednia = None

        while(obecna.nastepna != None):
            poprzednia = obecna
            obecna = obecna.nastepna
        if(poprzednia == None):
            return
        poprzednia.nastepna = None

    def __contains__(self, item):
        obecna = self.glowa

        while(obecna != None):
            if(obecna.wspolrzedne == item):
                return True
            obecna = obecna.nastepna
        return False


kuba = Wonsz(5,7)
print(kuba)
kuba.wrzuc_na_poczatek(x)
print(kuba)
print(len(kuba))

print((5,3) in kuba)
print((5,7) in kuba)
