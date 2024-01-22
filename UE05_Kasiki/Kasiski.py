"""
Author: Emir Cajlakovic 4CN
UE05
"""
import math
from collections import Counter
from typing import List, Tuple


class Kasiski:
    def __init__(self, crypttext: str):
        self.crypttext = crypttext

    @property
    def crypttext(self) -> str:
        return self._crypttext

    @crypttext.setter
    def crypttext(self, value: str) -> None:
        self._crypttext = value.lower()

    def dist(self, text: str, substring: str) -> List[int]:
        """
        Berechnet die Abstände zwischen den Wiederholungen des Teilstrings im verschlüsselten Text.

        Usage examples:
        >>> kasiski_instance = Kasiski("heissajuchei, ein ei")
        >>> kasiski_instance.dist("heissajuchei, ein ei", "ei")
        [9, 13, 17]
        >>> kasiski_instance.dist("heissajuchei, ein ei", "hai")
        []
        """
        positions = []
        index = 0

        while index < len(text):
            found_index = text.find(substring, index)
            if found_index == -1:
                break
            positions.append(found_index)
            index = found_index + 1

        distances = [positions[i + 1] - positions[i] for i in range(len(positions) - 1)]
        return distances

    def dist_n_tuple(text: str, substring: str, length: int) -> List[Tuple[str, int]]:
        """
        Überprüft alle Teilstrings aus text mit der gegebenen Länge und liefert eine Liste
        mit den Abständen aller Wiederholungen der Teilstrings in text.

        Usage examples:
        >>> dist_n_tuple("heissajuchei, ein ei", "ei", 2)
        [("he", 9), ("ei", 9), ("ei", 13), ("ei", 17)]
        >>> dist_n_tuple("heissajuchei, ein ei", "ei", 3)
        [("hei", 9)]
        >>> dist_n_tuple("heissajuchei, ein ei", "ei", 5)
        []
        """
        results = []

        for i in range(len(text) - length + 1):
            current_substring = text[i:i + length]
            if current_substring == substring:
                results.append((current_substring, i))

        return results

    def dist_n_list(self, text: str, substring: str, length: int) -> List[int]:
        """
        Wie dist_n_tuple, liefert aber nur eine Liste der Abstände ohne den Text zurück.

        Usage examples:
        >>> kasiski_instance = Kasiski("heissajuchei, ein ei")
        >>> kasiski_instance.dist_n_list("heissajuchei, ein ei", "ei", 2)
        [9, 9, 13, 17]
        >>> kasiski_instance.dist_n_list("heissajuchei, ein ei", "ei", 3)
        [9]
        >>> kasiski_instance.dist_n_list("heissajuchei, ein ei", "ei", 5)
        []
        """
        positions = []
        index = 0

        while index < len(self.crypttext):
            found_index = self.crypttext.find(substring, index)
            if found_index == -1:
                break
            positions.append(found_index)
            index = found_index + len(substring)

        distances = [positions[i + 1] - positions[i] for i in range(len(positions) - 1)]
        return distances

    def ggt(self, x: int, y: int) -> int:
        """
        Ermittelt den größten gemeinsamen Teiler von x und y.

        Usage examples:
        >>> kasiski_instance = Kasiski("heissajuchei, ein ei")
        >>> kasiski_instance.ggt(10, 25)
        5
        """
        while y:
            x, y = y, x % y
        return x

    def ggt_count(self, numbers: List[int]) -> Counter:
        """
        Bestimmt die Häufigkeit der paarweisen ggt aller Zahlen aus list.

        Usage examples:
        >>> kasiski_instance = Kasiski("heissajuchei, ein ei")
        >>> kasiski_instance.ggt_count([12, 14, 16])
        Counter({2: 2, 12: 1, 4: 1, 14: 1, 16: 1})
        >>> kasiski_instance.ggt_count([10, 25, 50, 100])
        Counter({10: 3, 25: 3, 50: 2, 5: 1, 100: 1})
        """
        gcd_counter = Counter()

        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                gcd_value = math.gcd(numbers[i], numbers[j])
                gcd_counter[gcd_value] += 2  # Increment count for both numbers

        return gcd_counter
    def get_nth_letter(self, s: str, start: int, n: int) -> str:
        """
        Extrahiert aus s jeden n. Buchstaben beginnend mit Index start.

        Usage examples:
        >>> kasiski_instance = Kasiski("heissajuchei, ein ei")
        >>> kasiski_instance.get_nth_letter("Das ist kein kreativer Text.", 1, 4)
        'asektrx'
        """
        return ''.join(s[start + i] for i in range(0, len(s) - start, n))

    def crack_key(self, length: int) -> List[str]:
        """
        Liefert eine Liste der ermittelten Schlüssel zurück.

        :param length: Die Länge des Schlüssels.
        :return: Liste der ermittelten Schlüssel.

        Usage examples:
        >>> kasiski_instance = Kasiski("heissajuchei, ein ei")
        >>> kasiski_instance.crack_key(2)
        ['ei']
        >>> kasiski_instance.crack_key(3)
        ['hei']
        >>> kasiski_instance.crack_key(5)
        ['heiss']
        """
