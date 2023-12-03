"""
Author: Emir Cajlakovic 4CN
UE04
"""

def collatz(n: int):
    """
    Berechnet den nächsten Wert in der Collatz-Folge.

    :param n: Aktuelle Zahl
    :return: Nächster Wert in der Collatz-Folge
    """
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

from typing import List

def collatz_sequence(number: int):
    """
    Generiert die Collatz-Zahlenfolge für eine gegebene Startzahl.

    :param number: Startzahl
    :return: Collatz-Zahlenfolge
    """
    sequence = [number]
    while number != 1:
        number = collatz(number)
        sequence.append(number)
    return sequence

from typing import Tuple

def longest_collatz_sequence(n: int):
    """
    Ermittelt den Startwert und die Länge der längsten Collatz-Zahlenfolge bis zu einer gegebenen Grenze.

    :param n: Obergrenze für den Startwert
    :return: Tuple (Startwert, Länge der Zahlenfolge)
    """
    max_start, max_length = 0, 0
    for start in range(1, n + 1):
        current_sequence = collatz_sequence(start)
        current_length = len(current_sequence)
        if current_length > max_length:
            max_start, max_length = start, current_length
    return max_start, max_length


if __name__ == "__main__":
    test_collatz = 5
    print(collatz(test_collatz))


