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

    
