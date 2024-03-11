"""
Author: Emir Cajlakovic 4CN
UE05
"""
import math
from collections import Counter
from typing import List, Tuple

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
class Vignere(Caesar):
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

        >>> vigenere=Vignere()
        >>> vigenere.key
        'hallo'
        >>> p1="Security ist coolääää"
        >>> vigenere.encrypt(p1,"apfel")
        'sthyciidmdtrtsw'
        >>> vigenere.decrypt("sthyciidmdtrtsw","apfel")
        'securityistcool'

        """
        if key is None:  # Überprüfen, ob key None ist
            key = self.key
        plaintext = self.to_lowercase_letter_only(plaintext)
        encrypted_text = ''
        key_index = 0
        for char in plaintext:
            if key_index == len(key):
                key_index = 0
            encrypted_text += self.encrypt(char, key[key_index])
            key_index += 1
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

class Kasiski:
    def __init__(self, crypttext:str=''):
        self.crypttext = crypttext
    def allpos(self, text: str, substring: str) -> list[int]:
        """Berechnet die Positionen von teilstring in text.
        Usage examples:
        >>> k = Kasiski()
        >>> k.allpos("heissajuchei, ein ei", "ei")
        [1, 10, 14, 18]
        >>> k.allpos("heissajuchei, ein ei", "hai")
        []
        """
        positions = []
        pos = text.find(substring)
        while pos != -1:
            positions.append(pos)
            pos = text.find(substring, pos + 1)
        return positions

    def dist(self, text: str, substring: str) -> List[int]:
        """
        Berechnet die Abstände zwischen den Wiederholungen des Teilstrings im verschlüsselten Text.

        Usage examples:
        >>> k = Kasiski()
        >>> k.dist("heissajuchei, ein ei", "ei")
        {4, 8, 9, 13, 17}
        >>> k.dist("heissajuchei, ein ei", "hai")
        set()
        """
        anzWdh: set[int] = set()
        allpos = self.allpos(text, substring)
        for pos in range(len(allpos)):
            for pos2 in range(pos + 1, len(allpos)):
                anzWdh.add(allpos[pos2] - allpos[pos])
        return anzWdh

    def dist_n_tuple(self, text:str, length:int) -> set[tuple[str, int]]:
        """
        Überprüft alle Teilstrings aus text mit der gegebenen Länge und liefert eine Liste
        mit den Abständen aller Wiederholungen der Teilstrings in text.
        Usage examples:
        >>> k = Kasiski()
        >>> k.dist_n_tuple("heissajuchei", 2) == {('ei', 9), ('he', 9)}
        True
        >>> k.dist_n_tuple("heissajuchei", 3) == {('hei', 9)}
        True
        >>> k.dist_n_tuple("heissajuchei", 4) == set()
        True
        >>> k.dist_n_tuple("heissajucheieinei", 2) == \
        {('ei', 5), ('ei', 14), ('ei', 3), ('ei', 9), ('ei', 11), ('he', 9), ('ei', 2)}
        True
        """
        ergSet = set()
        for i in range(len(text)):
            head = text[i:length + i]  # Text in Teilstrings der länge 'length' in einer varuabel head speichern.
            # print(head)
            if text.find(head, length + i) != -1:  ##?
                alldistance = self.dist(text, head)
                # print(alldistance)
                for j in alldistance:
                    ergSet.add((head, j))
        return ergSet

    def dist_n_list(self, text:str, length:int) -> list[int]:
        """
        Wie dist_n_tuple, liefert aber nur eine Liste der Abstände ohne den Text zurück.

        Usage examples:
        >>> k = Kasiski()
        >>> k.dist_n_list("heissajucheieinei", 2)
        [2, 3, 5, 9, 11, 14]
        >>> k.dist_n_list("heissajucheieinei", 3)
        [9]
        >>> k.dist_n_list("heissajucheieinei", 4)
        []
        """
        ergSet = set()
        dist_tuple = self.dist_n_tuple(text, length)
        # print(dist_tuple)
        for elements in dist_tuple:
            ergSet.add(elements[1])
        return list(ergSet)

    def ggt(self, x: int, y: int) -> int:
        """
        Ermittelt den größten gemeinsamen Teiler von x und y.

        Usage examples:
        >>> kasiski_instance = Kasiski("heissajuchei, ein ei")
        >>> kasiski_instance.ggt(10, 25)
        5
        """
        while y:
            x, y = y, x % y
        return x

    def ggt_count(self, numbers: list[int])->Counter:
        """
        Bestimmt die Häufigkeit der paarweisen ggt aller Zahlen aus list.

        Usage examples:
        >>> k = Kasiski()
        >>> k.ggt_count([12, 14, 16])
        Counter({12: 1, 4: 1, 14: 1, 16: 1})
        >>> k.ggt_count([10, 25, 50, 100])
        Counter({10: 3, 25: 3, 50: 2, 5: 1, 100: 1})
        >>> k.ggt_count([10, 20, 30])
        Counter({10: 4, 20: 1, 30: 1})
        >>> k.ggt_count([150, 300, 600])
        Counter({150: 3, 300: 2, 600: 1})
        >>> k.ggt_count([128, 165])
        Counter({128: 1, 165: 1})
        """
        ergList = []

        for i in range(len(numbers)):
            for j in range(i, len(numbers)):
                ggt = self.ggt(numbers[i], numbers[j])
                if (ggt == 1 or ggt == 2):
                    continue
                ergList.append(ggt)
        return Counter(ergList)


    def get_nth_letter(self, s:str, start:int, n:int)->str:
        """
        Extrahiert aus s jeden n. Buchstaben beginnend mit Index start.

        Usage examples:
        >>> k = Kasiski()
        >>> k.get_nth_letter("Das ist kein kreativer Text.", 1, 4)
        'asektrx'
        """
        return s[start::n]

    def crack_key(self,length:int) -> str:
        """
        Liefert eine Liste der ermittelten Schlüssel zurück.

        :param length: Die Länge des Schlüssels.
        :return: Liste der ermittelten Schlüssel.

        Usage examples:
        >>> k = Kasiski("UEQPC VCKAH VNRZU RNLAO KIRVG JTDVR VRICV IDLMYIYSBC COJQS ZNYMB VDLOK FSLMW EFRZA VIOMF JTDIHCIFPS EBXMF FTDMH ZGNMW KAXAU VUHJH NUULS VSJIPJCKTI VSVMZ JENZS KAHZS UIHQV IBXMF FIPLC XEQXOCAVBV RTWMB LNGNI VRLPF VTDMH ZGNMW KRXVR QEKVRLKDBS EIPUC EAWJS BAPMB VSZCF UEGIT LEUOS JOUOHUAVAG ZEZIS YRHVR ZHUMF RREMW KULKV KGHAH FEUBKLRGMB JIHLI IFWMB ZHUMP LEUWG RBHZO LCKCW THWDSILDAG VNEMJ FRVQS VIQMU VSWMZ CTHII WGDJSNBSPXEOWSJTKIHNBSPKEQ")
        >>> k.crack_key(3)
        'radio'
        >>> k1=Kasiski("fspomloqebscxayvhcgsfxxcomlkvkovfypxreauipwmrcigxippvyeylnwcsrcxduomisrbovlneqlfarilrmcrrqopsxhbkwkngforebiropcblydxcgilskxefcsilerbjyzbiarilerbomlwejkpqqvmoxceiperesrqvelnoywomxrroipneqdkjsgfofpyxlsgfdqcrvqmlypjcxagoipcmarrsxezorbcmklirdieohyxocxqymlroylnwgmltyvqyveorfovswajjxccispdroiperbctpkgfjyqomlovdbesgeqcsjvescylcacbhcxagoolxilgmperqovckvkorisrbovcbrfbilneusvdbylcwcvfqdrgmlrcqcrvfkfcx")
        >>> k1.crack_key(3)
        'key'
        >>> k2=Kasiski("ujrtslpcegesfzrdsygmfnasosluuiwowxdepxlvkpstocwvsgbflrxyizvegudeposbxydaomsbxefbpdxeukwpbsfbbutsxyaigtqapiksyukzekplfmwopsypeznasyxnygbbxogybbwxwkpikhcsmpnposuxdceanymxiqstbxcglzosgpnyftzepdxgsonatysosvvtjwesbyeorpimdcesygvsioaxhsptopdsetgtwpsbysbupzeygprpgflsqsdkxynasckbydpwnvzplbuevtebxixseeebwykxttbfmskkibvpftfsbwysfdeefoonpreoqhxyekuwwlnhbbdhhqfradsbyemscghyhxbogvsuesefnreobtqaesbwyskzhisoskyekgnvnseeoehxydbflfmtgjqshbreyfpwmpslvwsgoaascsgcakrosgqujwesbyeoochmcoqhzwkfmdomwgpikscgxttbbeolnhbiyuxqhoppfwpmescnxymxqshxdizvfbmprasxueyzbbosgdtltqjtrefvcsyzrjomnxtcebpbwpiksrfhpplfksewakdqsbqeysxskvbxfywvstbwyatwijhconxetfpwvsdxfliygeotlzepnasyigmehoybmpnwiqftrekcmsklnbwyskoeorpimdcesyigtvbfdwmeekgeiwteohsoupizvdsmktbapwgpgfsvogyeewyigobbuchxthkgzthctxiqrxftpqsabeefbpalnhksyuneekazfzpnjstbaprosckboeohpskqrxqesbyejscpkxlfqssglkwsyhbnhestsaprjoyblnhrzenbnheomszprxrpsbyidsxcgltbwyuktezvpbelnajpfucazvekhmrfupblthopfqaxefbdhgoidscfxtsbppuepiqscktcdfsdsklncoyulpikscfxoeaicqaorxbraxtnescnfttpsctkpuasowxdtfaxswpsxidzgoeogpflnhfsyabcmbzzrbdcescrxynjckokeipqssffsfytqacizvesmpdxvpfxtnbbgckprhsybmwizvvsbesqflvepnasypetchoftlpiksrceoeksmfbwlbrpbgwibppfycerboigolbgpfltedzliupngorokyizvekbpsbvckbcaizprbplfsmsgoibgtqaoibassgtcehgskorfspbelspsygbnhaicqafnpscslnhjypfatnaicqakucfpglpnfqskxcdbgzutcdfspbhcmphpbnywxvcgvsefbwwvskbwesgcepdpymteosyrxynjonvmpizvxwvszramsktcehtuxcdbguigrekrpimdcesykkoefqsrtouoqsnndefbpafttxfmsbeeownvsteesxwvsdfgvfxezrfnybnhyscztdsbwsawpnmzlhsfnarlgpzrqwnvplszvpaxtnbvyrxtnrbdqaflasdwlehbfxogydbfdsbyemccnxwlxbatxtfbgnvfluzvpbwfnavtbmprpstbxcglzosgpnyftzeplzvpzgozrwsbxysmftqae")
        >>> k2.crack_key(5)
        'axolotl'
        """
        c = Caesar()
        self.crypttext = c.to_lowercase_letter_only(self.crypttext)
        substring = self.dist_n_list(self.crypttext, length)
        möglichelänge = self.ggt_count(substring)
        mostprobkey = möglichelänge.most_common()[0][0]
        ergstr: str = ''
        for i in range(0, mostprobkey):
            ergstr += c.crack(self.crypttext[i::mostprobkey])[0]
        return ergstr
