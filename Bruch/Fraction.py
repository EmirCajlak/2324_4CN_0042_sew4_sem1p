"""
Author: Emir Cajlakovic 4CN
12.02.2023
UE07
"""

import math
class Fraction:
    """
        >>> Fraction()
        Fraction(0, 1)

        >>> Fraction(1)
        Fraction(1, 1)

        >>> print(Fraction(1, 2))
        1/2

        >>> print(Fraction(-1, 2))
        -1/2

        >>> print(Fraction(2, 4))
        1/2

        >>> print(Fraction(3, 2))
        1 1/2

        >>> print(Fraction(1, 2)-Fraction(1, 3))
        1/6

        >>> print(1+Fraction(2, 3))
        1 2/3

        >>> print(2*Fraction(4, 5))
        1 3/5

        >>> print(Fraction(1, 2)==Fraction(2, 4))
        True

        >>> print(Fraction(1, 2)<Fraction(1, 3))
        False

        >>> print(Fraction(-1, 2)/Fraction(1, 2))
        -1

        >>> print(Fraction(1, 2)+Fraction(-1, 2))
        0

        >>> print(Fraction(1, 2)+Fraction(1, 2))
        1

        >>> print(float(Fraction(1, 3)))
        0.3333333333333333

        >>> Fraction(0, 0)
        Traceback (most recent call last):
        ...
        ArithmeticError: Denominator cant be zero!

        >>> Fraction(11, 0)
        Traceback (most recent call last):
        ...
        ArithmeticError: Denominator cant be zero!

        >>> Fraction(1, 2) != Fraction(2, 3)
        True

        >>> print(3 + Fraction(1, 2))
        3 1/2

        >>> print(Fraction(3, 4) * Fraction(2, 3))
        3/6

        >>> print(Fraction(-3, 4) / Fraction(2, 3))
        -1 1/8

        >>> print(Fraction(3, 4) > Fraction(1, 2))
        True

        >>> print(Fraction(1, 4) < Fraction(1, 2))
        True

        >>> print(Fraction(5, 6) >= Fraction(1, 2))
        True

        >>> print(Fraction(5, 6) >= Fraction(1, 2))
        True

        >>> print(Fraction(1, 2) <= Fraction(1, 2))
        True

        >>> print(Fraction(3, 4) == Fraction(6, 8))
        True

        >>> print(Fraction(-3, 4) != Fraction(3, 4))
        True

        >>> Fraction(2)
        Fraction(2, 1)

        >>> print(Fraction(3, 4) < Fraction(1, 2))
        False

        >>> print(Fraction(5, 6) > Fraction(1, 2))
        True

        >>> print(Fraction(1, 4) <= Fraction(1, 2))
        True

        >>> print(Fraction(1, 2) >= Fraction(1, 2))
        True

        >>> print(Fraction(3, 4) == Fraction(6, 8))
        True

        >>> print(Fraction(-3, 4) != Fraction(3, 4))
        True

        >>> print(-Fraction(3, 4))
        -3/4

        >>> Fraction(3, 4)
        Fraction(3, 4)

        >>> print(Fraction(2, 3) < Fraction(3, 4))
        True

        >>> print(Fraction(5, 6) > Fraction(1, 3))
        True

        >>> print(Fraction(1, 5) <= Fraction(1, 2))
        True

        >>> print(Fraction(3, 4) >= Fraction(2, 3))
        True

        >>> print(Fraction(1, 2) == Fraction(2, 4))
        True

        >>> print(Fraction(2, 3) != Fraction(2, 4))
        True

        >>> print(-Fraction(3, 4))
        -3/4

        >>> print(3 + 1 / (7 + Fraction(1, 15)))
        3 15/106

        >>> Fraction(1, -2)
        Fraction(1, -2)
        """
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
        minus=''

        if (self.zaehler<0 and self.nenner>0) or (self.zaehler>0 and self.nenner<0):
            minus = "-"

        if ganzteil == 0:
            if rest == 0:
                return minus+str(0)
            else:
                return minus+str(rest)+"/"+str(abs(self.nenner))
        else:
            if rest == 0:
                return minus+str(ganzteil)
            else:
                return minus+str(ganzteil)+" "+str(rest)+"/"+str(abs(self.nenner))

    def __float__(self):
        return self.zaehler/self.nenner

    def __add__(self, b):
        a = b
        if isinstance(b, int):  #2/3+1/2
            a = Fraction(b, 1)
        n = math.floor(self.nenner*a.nenner) #n=6
        z = math.floor(self.zaehler*(n/self.nenner)+a.zaehler*(n/a.nenner)) #z=7
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