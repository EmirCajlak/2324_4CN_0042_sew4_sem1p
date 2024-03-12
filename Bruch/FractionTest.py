from Fraction import Fraction
import doctest
def Test():
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



