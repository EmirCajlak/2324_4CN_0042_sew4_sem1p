"""
Author: Emir Cajlakovic 4CN
04.12.2023
UE05
"""
class Caesar:
    """
    Caesar Chiffre zur Verschlüsselung und Entschlüsselung von Texten.
    """

    def __init__(self):
        """
        Initialisiert eine Instanz der Caesar-Klasse.
        """
        self._key = None

    @property
    def key(self) -> str:
        """
        Gibt den aktuellen Schlüssel zurück.
        """
        return self._key

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
        """
        key = key or self.key
        if not key:
            raise ValueError("Key must be set before encrypting")
        encrypted_text = ""
        for char in plaintext:
            if char.isalpha():
                shift = ord(key) - ord('a')
                encrypted_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
                encrypted_text += encrypted_char.upper() if char.isupper() else encrypted_char
            else:
                encrypted_text += char
        return encrypted_text

        def decrypt(self, ciphertext: str, key: str = None) -> str:
            """
            Entschlüsselt den Text mithilfe der Caesar-Chiffre.

            :param ciphertext: Der zu entschlüsselnde Text
            :param key: Optionaler Schlüssel, falls nicht festgelegt
            :return: Entschlüsselter Text
            :raise ValueError: Wenn der Schlüssel nicht festgelegt ist
            """
        key = key or self.key
        if not key:
            raise ValueError("Key must be set before decrypting")
        decrypted_text = ""
        for char in ciphertext:
            if char.isalpha():
                shift = ord(key) - ord('a')
                decrypted_char = chr((ord(char.lower()) - ord('a') - shift) % 26 + ord('a'))
                decrypted_text += decrypted_char.upper() if char.isupper() else decrypted_char
            else:
                decrypted_text += char
        return decrypted_text

        def crack(self, ciphertext: str, elements: int = 1) -> list[str]:
            """
            Knackt den Schlüssel und gibt eine Liste möglicher Entschlüsselungen zurück.

            :param ciphertext: Der verschlüsselte Text
            :param elements: Anzahl der zurückzugebenden Möglichkeiten
            :return: Liste möglicher Entschlüsselungen
            """
            possibilities = []
            for i in range(26):
                possible_key = chr((ord('a') + i) % 26 + ord('a'))
                decrypted_text = self.decrypt(ciphertext, key=possible_key)
                possibilities.append(decrypted_text)
                if len(possibilities) == elements:
                    break
            return possibilities

        if __name__ == "__main__":
            # Beispiel für die Verwendung der Caesar-Klasse
            caesar = Caesar()
            caesar.key = 'd'

            plaintext = "Hello, World!"
            encrypted_text = caesar.encrypt(plaintext)
            decrypted_text = caesar.decrypt(encrypted_text)
            cracked_texts = caesar.crack(encrypted_text, elements=5)

            print(f"Plaintext: {plaintext}")
            print(f"Encrypted: {encrypted_text}")
            print(f"Decrypted: {decrypted_text}")
            print(f"Cracked possibilities: {cracked_texts}")

