"""
Author: Emir Cajlakovic 4CN
UE08
"""
import os
import sys

from Kasiski import Caesar, Vignere, Kasiski
import argparse

def main():
    parser = argparse.ArgumentParser(description='cvrypt - Caesar & Vigenere encrypter / decrypter by MAT /HTL Rennweg')
    parser.add_argument( '-c','--cipher', help='Zu verwendete Chiffre', choices=['caesar','c','vigenere','v'])

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', action='store_true')
    group.add_argument('-q', '--quiet', action='store_true')

    group2 = parser.add_mutually_exclusive_group()
    group2.add_argument('-d', '--decrypt', action='store_true')
    group2.add_argument('-e', '--encrypt', action='store_true')

    parser.add_argument('-k', '--key', help='Encryption-key', type=str)
    parser.add_argument('infile', help='Zu verschlüssende Datei', type=str)
    parser.add_argument('outFile', help='Zieldatei', type=str, nargs='?')
    args = parser.parse_args()




if __name__ == '__main__':
    main()

