"""
Author: Emir Cajlakovic 4CN
04.12.2023
UE05
"""



def to_lower_letter_only(plaintext:str) -> str:
    """
    Text in nur kleine Buchstaben und ohne Sonderzeichen.

    :param plaintext: String
    :return: String nur mit Kleinbuchstaben
    >>> to_lower_letter_only("Wandelt den plaintext in Kleinbuchstaben um und entfernt alle Zeichen, die keine Kleinbuchstaben aus dem Bereich [a..z] sind.")
    'wandeltdenplaintextinkleinbuchstabenumundentferntallezeichendiekeinekleinbuchstabenausdembereichazsind'
    """
    return ''.join(char.lower() for char in plaintext if char.isalpha())

def encrypt (plaintext:str, key=None) -> str:
    """
    Text in nur kleine Buchstaben und ohne Sonderzeichen.

    :param plaintext: String
    :return: String nur mit Kleinbuchstaben
    >>> encrypt("hallo")
    'ibmmp'
    """



