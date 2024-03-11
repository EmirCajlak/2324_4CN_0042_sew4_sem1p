"""
Author: Emir Cajlakovic 4CN
04.12.2023
UE05
"""
from collections import Counter


class Caesar:
    """
    Caesar Chiffre zur Verschlüsselung und Entschlüsselung von Texten.
    """

    def __init__(self, key='a'):
        self.key = key

    @property
    def key(self) -> str:
        """
        Gibt den aktuellen Schlüssel zurück.
        """
        return self._key

    def to_lowercase_letter_only(self,plaintext:str) -> str:
        """
        Diese Methode bekommt einen Plaintext übergeben aus dem nur noch alle kleinbuchstaben ohne zahlen, sonderzeichen und Abstände
        :param plaintext:

        :return: plaintext in nur leerzeichen ohne zahlen, sonderzeichen und Abstände
        """
        erg:str=""
        umlaute = "äöüßÄÖÜ"
        for i in plaintext:
            if i.isalpha() and i not in umlaute:
                erg+=i.lower()
        return erg

    @key.setter
    def key(self, value: str) -> None:
        """
        Setzt den Schlüssel für die Caesar-Chiffre.

        :param value: Einzelner Buchstabe als Schlüssel
        :raise ValueError: Wenn der Schlüssel ungültig ist
        """
        if not value.isalpha() or len(value) != 1:
            raise ValueError("Key must be a single alphabet character")
        self._key = value.lower()

    def encrypt(self, plaintext: str, key: str = None) -> str:
        """
        Verschlüsselt den Text mithilfe der Caesar-Chiffre.

        :param plaintext: Der zu verschlüsselnde Text
        :param key: Optionaler Schlüssel, falls nicht festgelegt
        :return: Verschlüsselter Text
        :raise ValueError: Wenn der Schlüssel nicht festgelegt ist

        >>> caesar = Caesar()
        >>> caesar.encrypt("xyz", "c")
        'zab'
        """
        if key is None:  # Überprüfen, ob key None ist
            key = self.key
        plaintext=self.to_lowercase_letter_only(plaintext)
        erg: str = ""
        for i in plaintext:
            shift=chr(((ord(i) - ord('a') + ord(key) - ord('a')) % 26) + ord('a'))
            erg+=shift
        return erg

    def decrypt(self, ciphertext: str, key: str = None) -> str:
        """
        Entschlüsselt den Text mithilfe der Caesar-Chiffre.

        :param ciphertext: Der zu entschlüsselnde Text
        :param key: Optionaler Schlüssel, falls nicht festgelegt
        :return: Entschlüsselter Text
        :raise ValueError: Wenn der Schlüssel nicht festgelegt ist
        """
        if key is None:
            key = self.key
        erg: str = ""
        for char in ciphertext:
            reshift = chr(((ord(char) - ord('a') - (ord(key) - ord('a'))) % 26) + ord('a'))
            erg += reshift
        return erg

    def crack(self, ciphertext: str, elements: int = 1) -> list[str]:
        """
        Knackt den Schlüssel und gibt eine Liste möglicher Entschlüsselungen zurück.

        :param ciphertext: Der verschlüsselte Text
        :param elements: Anzahl der zurückzugebenden Möglichkeiten
        :return: Liste möglicher Entschlüsselungen
        >>> caesar = Caesar()
        >>> s1='Vor einem großen Walde wohnte ein armer Holzhacker mit seiner Frau und seinen zwei Kindern; das Bübchen hieß Hänsel und das Mädchen Gretel. Er hatte wenig zu beißen und zu brechen, und einmal, als große Teuerung ins Land kam, konnte er das tägliche Brotnicht mehr schaffen. Wie er sich nun abends im Bette Gedanken machte und sich vor Sorgen herumwälzte, seufzte er und sprach zu seiner Frau: "Was soll aus uns werden? Wie können wir unsere armen Kinder ernähren da wir für uns selbst nichts mehr haben?"'
        >>> caesar.crack(s1)
        ['a']
        >>> crypted = caesar.encrypt(s1, "y")
        >>> caesar.crack(crypted, 3)
        ['y', 'h', 'l']
        >>> caesar.crack(s1, 100)
        ['a', 'j', 'n', 'o', 'e', 'w', 'd', 'q', 'z', 'p', 'i', 'h', 'y', 's', 'k', 'x', 'c', 'v', 'g', 'b', 'r', 'l']
        """
        erglist: list[str] = []
        crypttext1 = self.to_lowercase_letter_only(ciphertext)
        # print(crypttext1)
        c = Counter(crypttext1)  # Wie oft jeder Buchstabe vorkommt
        # print(c)
        statistik = c.most_common()  # Liste aus tuppeln mit charackter und vorkommnisse
        # print(statistik)
        for item in statistik:
            # print(item[0])
            erglist.append((chr(((ord(item[0]) - ord('e')) % 26) + ord('a'))))
        return erglist[:elements]

if __name__ == "__main__":
            # Beispiel für die Verwendung der Caesar-Klasse
            caesar = Caesar()
            caesar.key = 'd'

            plaintext = "Hello, World!"
            encrypted_text = caesar.encrypt(plaintext)
            decrypted_text = caesar.decrypt(encrypted_text)
            cracked_texts = caesar.crack(encrypted_text, 5)

            print(f"Plaintext: {plaintext}")
            print(f"Encrypted: {encrypted_text}")
            print(f"Decrypted: {decrypted_text}")
            print(f"Cracked possibilities: {cracked_texts}")

