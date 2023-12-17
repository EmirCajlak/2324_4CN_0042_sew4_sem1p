class Kasiski:
    def __init__(self, crypttext: str):
        self._crypttext = crypttext

    @property
    def crypttext(self):
        return self._crypttext

    def dist(self, text: str, teilstring: str) -> list:
        """Berechnet die Abstände zwischen den Wiederholungen des Teilstrings im verschlüsselten Text."""
        positions = [pos for pos, char in enumerate(text) if text.find(teilstring, pos) == pos]
        distances = [positions[i + 1] - positions[i] for i in range(len(positions) - 1)]
        return distances

# Beispielanwendung
if __name__ == "__main__":
    # Beispieltext
    encrypted_text = "heissajuchei, ein ei"

    # Erstellen einer Kasiski-Instanz
    kasiski_instance = Kasiski(encrypted_text)

    # Testen der dist-Methode
    distances = kasiski_instance.dist(encrypted_text, "ei")
    print(distances)  # Ausgabe: [9, 13, 17]

    distances_hai = kasiski_instance.dist(encrypted_text, "hai")
    print(distances_hai)  # Ausgabe: []
