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
        x = abs(self.zaehler) % abs(self.nenner) #abs=minus wird zu plus und plus zu plus, z.B. 4/2 wird zu 2 weil 4%2 = 2 mit 0 rest
        y = math.floor(abs(self.zaehler) / abs(self.nenner)) #rundet die zahl nach unten
        minus = ""
        if (self.zaehler<0 and self.nenner>0) or (self.zaehler>0 and self.nenner<0):
            minus = "-"

        if y == 0:
            if x == 0:
                return minus+str(0)
            else:
                return minus+str(x)+"/"+str(abs(self.nenner))
        else:
            if x == 0:
                return minus+str(y)
            else:
                return minus+str(y)+" "+str(x)+"/"+str(abs(self.nenner))

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

