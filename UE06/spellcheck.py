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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def insert(head, new_char, tail):
        return head + new_char + tail

    def delete(word):
        return [word[:i] + word[i+1:] for i in range(len(word))]

    def transpose(word):
        return [word[:i] + word[i+1] + word[i] + word[i+2:] for i in range(len(word)-1)]

    def replace(head, new_char, tail):
        return head + new_char + tail[1:]

    candidates = set()

    candidates.update([tail for head, tail in split_word(word) if tail])
    candidates.update([head + tail[1] + tail[0] + tail[2:] for head, tail in split_word(word) if len(tail) > 1])
    candidates.update([replace(head, tail[0], tail[1:]) for head, tail in split_word(word) if tail])
    candidates.update([insert(head, new_char, tail) for head, tail in split_word(word) for new_char in alphabet])

    return candidates

def edit1_good(word: str, all_words: List[str]) -> Set[str]:
    """
    Filtert korrekte Wörter aus den Ergebnissen von edit1.

    :param word: Das Eingabewort.
    :param all_words: Eine Liste aller korrekten Wörter.
    :return: Eine Menge korrekter Wörter mit einer Edit-Distanz von eins.
    """
    return edit1(word) & set(all_words)

def edit2_good(wort:str, alle_worter:list[str]) -> set[str]:
    """ed2= das set was am Ende rauskommen soll, die erste schleife schreibt in e1 alle mögliochen edit 1 fehlern
    und die zweite Schleife schreibt dann ins endergebnisset alle edit 1 fehlern von den bereits edit 1 fehlern was
    zu edit 2 fehlern wird und im wörterbuch stehen ins ed2 hinein.
    """
    return {ed2 for ed1 in edit1(wort) for ed2 in edit1_good(ed1, alle_worter)}

def correct(word: str, all_words: List[str]) -> Set[str]:
    """
    Findet Korrekturen für ein Wort.

    :param word: Das Eingabewort.
    :param all_words: Eine Liste aller korrekten Wörter.
    :return: Eine Menge von Korrekturen für das Eingabewort.
    >>> alle_woerter = read_file("C:/Users/User/PycharmProjects/python4CN/UE06/de-en.txt")
    >>> correct("Aalsuppe", all_words)
    {'aalsuppe'}
    >>> correct("Alsuppe", all_words)
    {'aalsuppe'}
    >>> sorted(correct("Alsupe",all_words))
    ['aalsuppe', 'absude', 'alse', 'lupe']
    """
    word = word.lower()
    if word in all_words:
        return {word}
    ergSet = edit1_good(word, all_words) or edit2_good(word, all_words)
    return ergSet


# Doctests
if __name__ == "__main__":
    word_set:set[str] = read_file("C:\\Users\\User\\PycharmProjects\\python4CN\\UE06\\de-en.txt")
    erg_word:list[str] =list(word_set)
    #print(ergSet)
    print(edit1("Hallo"))
    print(edit1_good("Alsuppe", erg_word))
    print(edit2_good("Alsupp", erg_word))


