"""
Author: Emir Cajlakovic 4CN
UE06
"""
import string
from typing import List, Tuple, Set
# 1)
def read_file(filename: str) -> Set[str]:
    """
    Liest eine Datei ein und gibt eine Menge von Wörtern zurück.

    :param filename: Der Pfad zur Datei.
    :return: Eine Menge, die alle Wörter in der Datei enthält.
    """
    word_set = set()

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            word_set.update(words)

    return word_set

def split_word(word: str) -> List[Tuple[str, str]]:
    """
    Teilt ein Wort in alle möglichen Kombinationen von Anfang und Ende auf.

    :param word: Das zu teilende Wort.
    :return: Eine Liste von Tupeln, die Anfangs- und Endkombinationen enthalten.
    >>> split_word("abc")
    [('', 'abc'), ('a', 'bc'), ('ab', 'c'), ('abc', '')]
    >>> split_word("abm")
    [('', 'abm'), ('a', 'bm'), ('ab', 'm'), ('abm', '')]
    >>> split_word("hallo")
    [('', 'hallo'), ('h', 'allo'), ('ha', 'llo'), ('hal', 'lo'), ('hall', 'o'), ('hallo', '')]
    """

    return [(word[:i], word[i:]) for i in range(len(word) + 1)]

def edit1(word: str) -> Set[str]:
    """
    Findet alle Wörter mit einer Edit-Distanz von eins.

    :param word: Das Eingabewort.
    :return: Eine Menge von Wörtern mit einer Edit-Distanz von eins.
    """
    splits = split_word(word)
    letters = string.ascii_lowercase
    delete = {a + b[1:] for a, b in splits if b}
    misplaced = {a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1}
    replaced = {a + c + b[1:] for a, b in splits if b for c in letters}
    inserted = {a + c + b for a, b in splits for c in letters}
    return misplaced | delete | replaced | inserted

def edit1_good(word: str, all_words: List[str]) -> Set[str]:
    """
    Filtert korrekte Wörter aus den Ergebnissen von edit1.

    :param word: Das Eingabewort.
    :param all_words: Eine Liste aller korrekten Wörter.
    :return: Eine Menge korrekter Wörter mit einer Edit-Distanz von eins.
    """
    return edit1(word) & set(all_words)

def edit2_good(word:str, all_words:list[str]) -> set[str]:
    """ed2= das set was am Ende rauskommen soll, die erste schleife schreibt in e1 alle mögliochen edit 1 fehlern
    und die zweite Schleife schreibt dann ins endergebnisset alle edit 1 fehlern von den bereits edit 1 fehlern was
    zu edit 2 fehlern wird und im wörterbuch stehen ins ed2 hinein.
    """
    return {candidate for candidate in edit1(word) for candidate in edit1_good(candidate, all_words)}

def correct(word: str, all_words: List[str]) -> Set[str]:
    """
    Findet Korrekturen für ein Wort.

    :param word: Das Eingabewort.
    :param all_words: Eine Liste aller korrekten Wörter.
    :return: Eine Menge von Korrekturen für das Eingabewort.
    >>> all_words = read_file("C:/Users/User/PycharmProjects/python4CN/UE06/de-en.txt")
    >>> correct("Aalsuppe", all_words)
    {'aalsuppe'}
    >>> correct("Alsuppe", all_words)
    {'aalsuppe'}
    >>> sorted(correct("Alsupe",all_words))
    ['aalsuppe', 'absude', 'alse', 'lupe']
    """
    word_lower = word.lower()
    candidates = (edit1_good(word_lower, all_words) or
                  edit2_good(word_lower, all_words) or
                  {word_lower})
    return candidates

# Doctests
if __name__ == "__main__":
    word_set:set[str] = read_file("C:\\Users\\User\\PycharmProjects\\python4CN\\UE06\\de-en.txt")
    erg_word:list[str] =list(word_set)
    #print(word_set)
    print(edit1("Hallo"))
    print(edit1_good("Alsuppe", erg_word))
    print(edit2_good("Alsupp", erg_word))


