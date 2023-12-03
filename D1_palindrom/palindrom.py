"""
Author: Emir Cajlakovic 4CN
UE04
"""


def is_palindrom (s:str):
    """
    Die Methode überprüft, ob der gegebene String von Main palindrom ist oder nicht
    [::-1],
    :param s: Der String, den man überprüfen soll
    :return: True, wenn es palindrom ist, false wenn nicht
    """
    if s[::-1] == s:
        return s

def is_palindrom_sentence(s:str):
    """
    Überprüft ob der Satz von Main palindrom ist oder nicht
    :param s: Der String, den man überprüfen soll
    :return: True, wenn der Satz palindrom ist, false wenn nicht
    """
    erg = ''.join(s.lower() for c in s if s.isalnum())
    return erg == erg[::-1]


if __name__ == "__main__":
    #Methode1
    test_ispalindrom = "9009"
    if is_palindrom (test_ispalindrom):
        print("True")
    else:
        print("False")

    #Methode2
    test_ispalindrom_sentence = "jbdafba"
    print(f'Ist "{test_ispalindrom_sentence}" ein palindrom Satz? {is_palindrom_sentence(test_ispalindrom_sentence)}')





