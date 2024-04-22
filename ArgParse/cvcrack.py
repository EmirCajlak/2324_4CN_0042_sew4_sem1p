"""
Author: Emir Cajlakovic 4CN
UE08
"""
import os
import sys

from Kasiski import Caesar, Vignere, Kasiski
import argparse

def main():
    """
        Hauptfunktion zum Ausführen des cvcrack-Skripts.
        Verwendet argparse, um Befehlszeilenargumente zu parsen und den Caesar- oder Vigenere-Schlüssel zu knacken.
        Das Skript dient zum Knacken von Caesar- oder Vigenere-Schlüsseln, je nachdem, welcher
        Chiffre-Modus angegeben ist.
        Es verwendet das Kasiski-Verfahren, um den Vigenere-Schlüssel zu knacken,
        und den Caesar-Bruteforce-Ansatz, um den Caesar-Schlüssel zu knacken.
        Die Ausgabe kann je nach Verbositätsstufe entweder ausführliche
        Informationen oder nur den geknackten Schlüssel enthalten.
    """
    parser = argparse.ArgumentParser(description='cvcrack - Caesar & Vigenere key cracker by CAJ /HTL Rennweg')
    parser.add_argument('-c', '--cipher', help='Zu verwendete Chiffre', choices=['caesar', 'c', 'vignere', 'v'])

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', help='Zeigt Infos an', action='store_true')
    group.add_argument('-q', '--quiet', help='Liefert nur wahrscheinlichsten key zurück', action='store_true')

    parser.add_argument('infile', help='Zu knackende Datei', type=str)
    args = parser.parse_args()

    # Bestimme den Chiffriermodus
    if args.cipher == 'caesar' or args.cipher == 'c':
        cipher_mode = 'Caesar'
    elif args.cipher == 'vignere' or args.cipher == 'v':
        cipher_mode = 'Vignere'

    # Initialisierung des Chiffrier- oder Kasiski-Verfahrens
    if args.cipher == 'caesar':
        if not os.path.isfile(args.infile):
            print(f'{args.infile}: No such File or directory found')
            sys.exit(1)
        cipherC = Caesar()
        with open(args.infile, 'r') as f:
            crypttext = f.read()
            key = "".join(cipherC.crack(crypttext))
    else:
        if not os.path.isfile(args.infile):
            print(f'{args.infile}: No such File or directory found')
            sys.exit(1)
        with open(args.infile, 'r') as f:
            cipherV = Kasiski(f.read())
            key = (cipherV.crack_key(3))

    # Ausgabe des geknackten Schlüssels je nach Verbositätsstufe
    if args.verbose:
        print(f'Cracking {cipher_mode}-encryptetd file {args.infile}: Key=' + key)
    if args.quiet:
        print(key)

if __name__ == "__main__":
    main()