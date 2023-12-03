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

def get_dec_hex_palindrom(x: int):
    """
    Findet die größte Zahl (kleiner als x), die sowohl im Dezimalsystem als auch im Hexadezimalsystem ein Palindrom ist.

    :param x: Obergrenze
    :return: Größte Palindromzahl
    """
    groesster_palindrom = 0
    for zahl in range(x - 1, 0, -1): #Eine Schleife wird gestartet, die von x - 1 bis 1 in absteigender Reihenfolge läuft. Das bedeutet, dass wir von der oberen Grenze x beginnen und bis zur Zahl 1 hinuntergehen.
        if is_palindrom(str(zahl)) and is_palindrom(hex(zahl)[2:]): #[2:], um die ersten beiden zu entfernen
            groesster_palindrom = zahl
            break
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

    #Methode3
    test_is_palindrom_produkt = palindrom_product(1000)
    print(f'Größtes Palindromprodukt von zwei 3-stelligen Zahlen kleiner als 1000: {test_is_palindrom_produkt}')

    #Methode4
    max_dec_hex_palindrom = get_dec_hex_palindrom(10000)
    print(f'Größtes Palindrom im Dezimal- und Hexadezimalsystem kleiner als 10000: {max_dec_hex_palindrom}')


