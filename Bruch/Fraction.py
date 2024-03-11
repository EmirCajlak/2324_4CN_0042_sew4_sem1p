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

        except:
            raise





