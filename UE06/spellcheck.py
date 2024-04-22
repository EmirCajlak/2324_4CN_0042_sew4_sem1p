"""
Author: Emir Cajlakovic 4CN
UE06
"""
import string
from typing import List, Tuple, Set
# 1)
def read_all_words(filename:str) -> set[str]:
    """
    Liest eine Datei ein und gibt eine Menge von Wörtern zurück.
    :param filename:
    :return:
    """
    ergSet:set[str] = set()
    with open(filename,"r",encoding="utf-8") as f:
        ergSet={line.strip().lower() for line in f}
    return ergSet

def split_word(wort:str) -> list[tuple[str, str]]:
    """
    Teilt ein Wort in alle möglichen Kombinationen von Anfang und Ende auf. ('', 'abc'), ('a', 'bc'), ('ab', 'c'), ('abc', '').
    :param wort:
    :return: list of tuples
    >>> split_word("abc")
    [('', 'abc'), ('a', 'bc'), ('ab', 'c'), ('abc', '')]
    >>> split_word("abm")
    [('', 'abm'), ('a', 'bm'), ('ab', 'm'), ('abm', '')]
    >>> split_word("hallo")
    [('', 'hallo'), ('h', 'allo'), ('ha', 'llo'), ('hal', 'lo'), ('hall', 'o'), ('hallo', '')]
    """
    return [(wort[:pos], wort[pos:]) for pos in range(len(wort)+1)] #word[:i] enthält die ersten i Zeichen des Wortes, während word[i:] die restlichen Zeichen enthält, beginnend bei Index i. Anschließend kombiniert man die Präfixe mit den Suffixe
def edit1(word: str) -> set[str]:
    """
    Findet alle Wörter mit einer Edit-Distanz von eins.
    :param wort:
    :return: ein set mit allen Möglichkeiten aus jeweils einem ,umtauschung,einsetungs,vertauschungs und löschungs Fehler
    """
    splits = split_word(word)
    letters = string.ascii_lowercase
    delete = {a + b[1:] for a, b in splits if b}  # den ersten Buchstaben aus dem zweiten Teil jedes Splittupels entfernen, Die Bedingung if b stellt sicher, dass nur Splittupels verarbeitet werden, die mindestens zwei Teile haben.
    misplaced = {a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1}  # den zweiten und ersten Buchstaben im zweiten Teil jedes Splittupels vertauschen
    replaced = {a + c + b[1:] for a, b in splits if b for c in letters}  # jeden Buchstaben im zweiten Teil jedes Splittupels durch jeden Kleinbuchstaben des Alphabets ersetzen
    inserted = {a + c + b for a, b in splits for c in letters}  # jeden Kleinbuchstaben des Alphabets zwischen den beiden Teilen jedes Splittupels einfügen
    return misplaced | delete | replaced | inserted


def edit1_good(word:str, all_words:list[str]) -> set[str]:
    """
    Filtert korrekte Wörter aus den Ergebnissen von edit1.
    :param word:
    :param all_words:
    :return:
    """
    return edit1(word.lower()) & set(all_words)

def edit2_good(word:str, all_words:list[str]) -> set[str]:
    """Jedes Element in der Menge von Wörtern mit einer Edit-Distanz von eins iteriert, die von der Funktion edit1(word) zurückgegeben wird.
    Innerhalb der äußeren Schleife gibt es eine weitere Schleife, die über jedes Wort candidate in der Menge von Wörtern iteriert,
    die von der Funktion edit1_good(candidate, all_words) zurückgegeben wird. Diese Menge enthält nur die Wörter aus der Menge edit1(word),
    die auch in der Liste all_words enthalten sind, was bedeutet, dass sie als korrekt angesehen werden.
    """
    # Die äußere Schleife durchläuft alle Wörter, die durch eine Bearbeitung aus `wort` entstehen und die innere Schleife durchläuft alle Wörter, die durch eine Bearbeitung aus einem dieser Zwischenwörter entstehen.
    dis1_wort = {edit_word for word in edit1(word) for edit_word in edit1(word)}
    # Schnitt der generierten Wörter
    return dis1_wort & all_words

def correct(word:str, alle_worter:list[str]) -> set[str]:
    """
    :param wort:
    :param alle_worter:
    :return: Korrekturen für das übergebene wort
    >>> alle_woerter = read_all_words("C:/Users/User/PycharmProjects/python4CN/UE06/de-en.txt")
    >>> correct("Aalsuppe", alle_woerter)
    {'aalsuppe'}
    >>> correct("Alsuppe", alle_woerter)
    {'aalsuppe'}
    >>> sorted(correct("Alsupe",alle_woerter))
    ['aalsuppe', 'absude', 'alse', 'lupe']
    """
    word=word.lower()
    if word in alle_worter:
        return {word}
    ergSet=edit1_good(word, alle_worter) or edit2_good(word, alle_worter)
    return ergSet



if __name__ == "__main__":
    woerterbuch = read_all_words("de-en.txt")

    print(split_word("hallo"))
    print(edit1("hallo"))
    print(edit1_good("hallo", woerterbuch))
    print(edit2_good("HALLO", woerterbuch))
    print(correct("halo", woerterbuch))






