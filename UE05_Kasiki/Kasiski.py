class Kasiski:
    def __init__(self, crypttext):
        self._crypttext = crypttext

    @property
    def crypttext(self):
        return self._crypttext

    def dist(self, text, teilstring):
        """
        Berechnet die Abstände zwischen den Wiederholungen des Teilstrings im verschlüsselten Text.

        Usage examples:
        >>> dist("heissajuchei, ein ei", "ei")
        [9, 13, 17]
        >>> dist("heissajuchei, ein ei", "hai")
        []
        """
        positions = []
        start = 0

        while True:
            position = text.find(teilstring, start)
            if position == -1:
                break
            positions.append(position)
            start = position + 1

        distances = [positions[i + 1] - positions[i] for i in range(len(positions) - 1)]
        return distances


# Beispiel-Nutzung
if __name__ == "__main__":
    # Beispiel verschlüsselter Text
    crypttext_example = "xdytcyxtetydtgqehnxdytcyxtetydtgqehnxdytcyxtetydtgqehn"

    # Beispiel Klasse Kasiski
    kasiski_instance = Kasiski(crypttext_example)

    # Beispiel Nutzung der dist-Methode
    distances = kasiski_instance.dist(crypttext_example, "xdy")
    print(distances)
