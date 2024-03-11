"""
Author: Emir Cajlakovic 4CN
12.02.2023
UE07
"""

import math
class Fraction:
    def __init__(self, zaehler=0, nenner=1):
        try:
            if nenner == 0:
                raise ArithmeticError("Denominator cant be zero!")
            self.zaehler = zaehler
            self.nenner = nenner
            self.kuerzen()
        except:
            raise

    def kuerzen(self):
        while 1: #solange bis sie nicht true ist
            i = 2
            while i*i <= max(self.zaehler, self.nenner): #überprüft, ob es Rest gibt
                if self.zaehler % i == 0 and self.nenner % i == 0: #Wenn i ein gemeinsamer Teiler ist, wird der Zähler durch i geteilt und auf den ganzzahligen Teil des Ergebnisses abgerundet, um ihn zu kürzen.
                    self.zaehler = math.floor(self.zaehler/i)
                    self.nenner = math.floor(self.nenner/i)
                    break
                i = i+1 #Falls kein gemeinsamer Teiler gefunden wurde
            if i*i > max(self.zaehler, self.nenner):
                break

    def __str__(self):
        rest = abs(self.zaehler) % abs(self.nenner) #abs=minus wird zu plus und plus zu plus, z.B. 4/2 wird zu 2 weil 4%2 = 2 mit 0 rest
        ganzteil = math.floor(abs(self.zaehler) / abs(self.nenner)) #rundet die zahl nach unten

        if ganzteil == 0:
            if rest == 0:
                return "-"+str(0)
            else:
                return "-"+str(rest)+"/"+str(abs(self.nenner))
        else:
            if rest == 0:
                return "-"+str(ganzteil)
            else:
                return "-"+str(ganzteil)+" "+str(rest)+"/"+str(abs(self.nenner))

    def __float__(self):
        return self.zaehler/self.nenner

    def __add__(self, b):
        a = b
        if isinstance(b, int):
            a = Fraction(b, 1)
        n = math.floor(self.nenner*a.nenner)
        z = math.floor(self.zaehler*(n/self.nenner)+a.zaehler*(n/a.nenner))
        F = Fraction(z, n)
        F.kuerzen()
        return F

    def __radd__(self, b):
        return self+b

    def __sub__(self, b):
        a = b
        if isinstance(b, int):
            a = Fraction(b, 1)
        n = math.floor(self.nenner*a.nenner)
        z = math.floor(self.zaehler*(n/self.nenner)-a.zaehler*(n/a.nenner))
        F = Fraction(z, n)
        F.kuerzen()
        return F

    def __rsub__(self, b):
        a = b
        if isinstance(b, int):
            a = Fraction(b, 1)
        return a-self

    def __mul__(self, b):
        a = b
        if isinstance(b, int):
            a = Fraction(b, 1)
        n = math.floor(self.nenner * a.nenner)
        z = math.floor(self.zaehler * a.zaehler)
        F = Fraction(z, n)
        F.kuerzen()
        return F

    def __rmul__(self, b):
        return self*b
    def __truediv__(self, b):
        a = b
        if isinstance(b, int):
            a = Fraction(b, 1)
        n = math.floor(self.nenner * a.zaehler)
        z = math.floor(self.zaehler * a.nenner)
        F = Fraction(z, n)
        F.kuerzen()
        return F

    def __rtruediv__(self, b):
        a = b
        if isinstance(b, int):
            a = Fraction(b, 1)
        return a/self

    def __lt__(self, b):
        return float(self) < float(b)

    def __gt__(self, b):
        return float(self) > float(b)

    def __le__(self, b):
        return float(self) <= float(b)

    def __ge__(self, b):
        return float(self) >= float(b)

    def __eq__(self, b):
        return self.zaehler == b.zaehler and self.nenner == b.nenner

    def __ne__(self, b):
        return self.zaehler != b.zaehler or self.nenner != b.nenner

    def __neg__(self):
        return Fraction(-self.zaehler, self.nenner)

    def __repr__(self):
        return "Fraction("+str(self.zaehler)+", "+str(self.nenner)+")"