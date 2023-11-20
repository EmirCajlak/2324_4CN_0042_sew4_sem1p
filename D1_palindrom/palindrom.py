"""
Author: Emir Cajlakovic 4CN
UE04
"""


def is_palindrom (s:str):
    """
    Die Methode überprüft, ob der gegebene String von Zeile 17 palindrom ist oder nicht
    [::-1],
    :param s: Der String, den man überprüfen soll
    :return: True, wenn es palindrom ist, false wenn nicht
    """
    if s[::-1] == s:
        return s

def is_palindrom_sentence(s:str):
    """

    :param s: Der String, den man überprüfen soll
    :return: True, wenn der Satz palindrom ist, false wenn nicht
    """
    s = s.lower()
    erg = ""
    for char in range(len(s)):
        if s[char].isalnum():
            erg += s[char]

    if erg[::-1] == erg:
        return erg


if __name__ == "__main__":
    #Methode1
    test_ispalindrom = "9009"
    if is_palindrom (test_ispalindrom):
        print("True")
    else:
        print("False")

    #Methode2
    test_ispalindrom_sentence = "oho!"
    if is_palindrom(test_ispalindrom_sentence):
        print("True")
    else:
        print("False")





