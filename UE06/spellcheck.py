"""
Author: Emir Cajlakovic 4CN
UE06
"""

from typing import List, Tuple, Set
# 1)
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

# 2)
def split_word(wort: str) -> List[Tuple[str, str]]:
    result = [(wort[:i], wort[i:]) for i in range(len(wort) + 1)]
    return result

# Beispielaufruf
word = "abcd"
result_list = split_word(word)
print(result_list)

# 3)

def edit1(wort: str) -> Set[str]:
    # Funktion zum Einfügen eines Buchstabens
    def insert(word: str, c: str) -> str:
        return [word[:i] + c + word[i:] for i in range(len(word) + 1)]

    # Funktion zum Löschen eines Buchstabens
    def delete(word: str) -> str:
        return [word[:i] + word[i+1:] for i in range(len(word))]

    # Funktion zum Vertauschen von zwei aufeinanderfolgenden Buchstaben
    def transpose(word: str) -> str:
        return [word[:i] + word[i+1] + word[i] + word[i+2:] for i in range(len(word)-1)]

    # Funktion zum Ersetzen eines Buchstabens
    def replace(word: str, c: str) -> str:
        return [word[:i] + c + word[i+1:] for i in range(len(word))]

    # Alle möglichen Wörter mit einem Fehler weniger
    candidates = set()

    # Ein Buchstabe fehlt
    candidates.update([tail for head, tail in split_word(wort) if tail])

    # Zwei Buchstaben vertauscht
    candidates.update([head + tail[1] + tail[0] + tail[2:] for head, tail in split_word(wort) if len(tail) > 1])

    # Ein Buchstabe ersetzt
    candidates.update(replace(head, tail[0]) for head, tail in split_word(wort) if tail)

    # Ein Buchstabe eingefügt
    candidates.update(insert(head, tail[0]) for head, tail in split_word(wort))

    return candidates

# Beispielaufruf
word = "abc"
result_set = edit1(word)
print(result_set)
