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



