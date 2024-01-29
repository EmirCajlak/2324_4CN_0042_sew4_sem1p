"""
Author: Emir Cajlakovic 4CN
UE06
"""

from typing import List, Tuple, Set

def read_all_words(filename: str) -> Set[str]:
    word_set = set()

    # Verwende den Context Manager 'with', um die Datei zu öffnen und automatisch zu schließen
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # Teile die Zeile in Wörter auf und füge sie dem Set hinzu
            words = line.split()
            word_set.update(words)

    return word_set

# Beispielaufruf
filename = 'C:\\Users\\User\\Desktop\\4CN\\Softwareentwicklung\\de-en.txt'
word_set = read_all_words(filename)

# Ausgabe des Sets
print(word_set)
