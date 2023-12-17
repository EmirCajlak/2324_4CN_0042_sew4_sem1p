from typing import List

class Vigenere:
    """
    Vigenere Chiffre zur Verschlüsselung und Entschlüsselung von Texten.
    """

    def __init__(self):
        """
        Initialisiert eine Instanz der Vigenere-Klasse.
        """
        self._key = ""

    @property
    def key(self) -> str:
        """
        Gibt den aktuellen Schlüssel zurück.
        """
        return self._key

    @key.setter
    def key(self, value: str) -> None:
        """
        Setzt den Schlüssel für die Vigenere-Chiffre.

        :param value: Schlüssel als String
        :raise ValueError: Wenn der Schlüssel ungültig ist
        """
        if not value.isalpha() or not value:
            raise ValueError("Key must be a non-empty string of alphabetic characters")
        self._key = value.lower()

    def encrypt(self, plaintext: str, key: str = None) -> str:
        """
        Verschlüsselt den Text mithilfe der Vigenere-Chiffre.

        :param plaintext: Der zu verschlüsselnde Text
        :param key: Optionaler Schlüssel, falls nicht festgelegt
        :return: Verschlüsselter Text
        :raise ValueError: Wenn der Schlüssel nicht festgelegt ist
        """
        key = key or self.key
        if not key:
            raise ValueError("Key must be set before encrypting")
        encrypted_text = ""
        key_index = 0
        for char in plaintext:
            if char.isalpha():
                shift = ord(key[key_index]) - ord('a')
                caesar = Caesar()
                caesar.key = key[key_index]
                encrypted_char = caesar.encrypt(char)
                encrypted_text += encrypted_char
                key_index = (key_index + 1) % len(key)
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, ciphertext: str, key: str = None) -> str:
        """
        Entschlüsselt den Text mithilfe der Vigenere-Chiffre.

        :param ciphertext: Der zu entschlüsselnde Text
        :param key: Optionaler Schlüssel, falls nicht festgelegt
        :return: Entschlüsselter Text
        :raise ValueError: Wenn der Schlüssel nicht festgelegt ist
        """
        key = key or self.key
        if not key:
            raise ValueError("Key must be set before decrypting")
        decrypted_text = ""
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                shift = ord(key[key_index]) - ord('a')
                caesar = Caesar()
                caesar.key = key[key_index]
                decrypted_char = caesar.decrypt(char)
                decrypted_text += decrypted_char
                key_index = (key_index + 1) % len(key)
            else:
                decrypted_text += char
        return decrypted_text

    # def crack(self, ciphertext: str, key_length: int) -> List[str]:
    #     """
    #     Knackt den Schlüssel und gibt eine Liste möglicher Entschlüsselungen zurück.
    #
    #     :param ciphertext: Der verschlüsselte Text
    #     :param key_length: Die Länge des Schlüssels
    #     :return: Liste möglicher Entschlüsselungen
    #     """
    #     possibilities = []
    #     for i in range(key_length):
    #         substring = ciphertext[i::key_length]
    #         caesar = Caesar()
    #         cracked_positions = caesar.crack(substring, elements=1)
    #         possibilities.append((cracked_positions[0][0], ""))
    #     return possibilities

# class Caesar:
#     """
#         Caesar Chiffre zur Verschlüsselung und Entschlüsselung von Texten.
#         """
#
#     def __init__(self):
#         """
#         Initialisiert eine Instanz der Caesar-Klasse.
#         """
#         self._key = None
#
#     @property
#     def key(self) -> str:
#         """
#         Gibt den aktuellen Schlüssel zurück.
#         """
#         return self._key
#
#     @key.setter
#     def key(self, value: str) -> None:
#         """
#         Setzt den Schlüssel für die Caesar-Chiffre.
#
#         :param value: Einzelner Buchstabe als Schlüssel
#         :raise ValueError: Wenn der Schlüssel ungültig ist
#         """
#         if not value.isalpha() or len(value) != 1:
#             raise ValueError("Key must be a single alphabet character")
#         self._key = value.lower()
#
#     def encrypt(self, plaintext: str, key: str = None) -> str:
#         """
#         Verschlüsselt den Text mithilfe der Caesar-Chiffre.
#
#         :param plaintext: Der zu verschlüsselnde Text
#         :param key: Optionaler Schlüssel, falls nicht festgelegt
#         :return: Verschlüsselter Text
#         :raise ValueError: Wenn der Schlüssel nicht festgelegt ist
#         """
#         key = key or self.key
#         if not key:
#             raise ValueError("Key must be set before encrypting")
#         encrypted_text = ""
#         for char in plaintext:
#             if char.isalpha():
#                 shift = ord(key) - ord('a')
#                 encrypted_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
#                 encrypted_text += encrypted_char.upper() if char.isupper() else encrypted_char
#             else:
#                 encrypted_text += char
#         return encrypted_text
#
#     def decrypt(self, ciphertext: str, key: str = None) -> str:
#         """
#         Entschlüsselt den Text mithilfe der Caesar-Chiffre.
#
#         :param ciphertext: Der zu entschlüsselnde Text
#         :param key: Optionaler Schlüssel, falls nicht festgelegt
#         :return: Entschlüsselter Text
#         :raise ValueError: Wenn der Schlüssel nicht festgelegt ist
#         """
#
#         key = key or self.key
#         if not key:
#             raise ValueError("Key must be set before decrypting")
#         decrypted_text = ""
#         for char in ciphertext:
#             if char.isalpha():
#                 shift = ord(key) - ord('a')
#                 decrypted_char = chr((ord(char.lower()) - ord('a') - shift) % 26 + ord('a'))
#                 decrypted_text += decrypted_char.upper() if char.isupper() else decrypted_char
#             else:
#                 decrypted_text += char
#         return decrypted_text
#
#     def crack(self, ciphertext: str, elements: int = 1) -> list[str]:
#         """
#         Knackt den Schlüssel und gibt eine Liste möglicher Entschlüsselungen zurück.
#
#         :param ciphertext: Der verschlüsselte Text
#         :param elements: Anzahl der zurückzugebenden Möglichkeiten
#         :return: Liste möglicher Entschlüsselungen
#         """
#         possibilities = []
#         for i in range(26):
#             possible_key = chr((ord('a') + i) % 26 + ord('a'))
#             decrypted_text = self.decrypt(ciphertext, key=possible_key)
#             possibilities.append(decrypted_text)
#             if len(possibilities) == elements:
#                 break
#         return possibilities

if __name__ == "__main__":
    # Beispiel für die Verwendung der Vigenere-Klasse
    vigenere = Vigenere()
    vigenere.key = 'key'

    plaintext = "Hello, World!"
    encrypted_text = vigenere.encrypt(plaintext)
    decrypted_text = vigenere.decrypt(encrypted_text)
    cracked_positions = vigenere.crack(encrypted_text, key_length=3)

    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text}")
    print(f"Cracked possibilities: {cracked_positions}")
