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

    startzahl = 19
    collatz_sequence_result = collatz_sequence(startzahl)
    print(f'Collatz-Folge für Startzahl {startzahl}: {collatz_sequence_result}')

    startwert, laenge = longest_collatz_sequence(20)
    print(f'Längste Collatz-Folge bis 20 startet bei {startwert} und hat eine Länge von {laenge}.')

    startwert, laenge = longest_collatz_sequence(100)
    print(f'Längste Collatz-Folge bis 100 startet bei {startwert} und hat eine Länge von {laenge}.')

    startwert, laenge = longest_collatz_sequence(500)
    print(f'Längste Collatz-Folge bis 500 startet bei {startwert} und hat eine Länge von {laenge}.')

