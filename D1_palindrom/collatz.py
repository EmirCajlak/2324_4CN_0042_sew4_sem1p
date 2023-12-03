"""
Author: Emir Cajlakovic 4CN
UE04
"""

def collatz(n: int) -> int:
    """
    Berechnet den nächsten Wert in der Collatz-Folge.

    :param n: Aktuelle Zahl
    :return: Nächster Wert in der Collatz-Folge
    """
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1