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


