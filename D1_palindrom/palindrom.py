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
    # Satz ohne Nicht-Buchstaben und Nicht-Ziffern und mit "seinem" Rückwörts verglichen
    erg = ''.join(s.lower() for c in s if s.isalnum())
    return erg == erg[::-1]

def palindrom_product(x: int):
    """
    Findet die größte Palindromzahl (kleiner als x), die das Produkt von zwei 3-stelligen Zahlen ist.

    :param x: Obergrenze
    :return: Größte Palindromzahl

    """

    groesster_palindrom = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            produkt = i * j
            if 1000 > produkt < x and is_palindrom(str(produkt)):
                groesster_palindrom = max(groesster_palindrom, produkt)
    return groesster_palindrom


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





