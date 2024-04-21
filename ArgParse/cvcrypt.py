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


    if args.cipher == 'caesar' or args.cipher == 'c':
        cipher_mode='Caesar'
    elif args.cipher == 'vigenere' or args.cipher == 'v':
        cipher_mode='Vigenere'
    if args.encrypt:
        mode='Encrypting'
    elif args.decrypt:
        mode='Decrypting'

    if args.verbose:
        print(f'{mode} {cipher_mode} with key={args.key} from {args.infile} into {args.outFile}')

    if args.quiet:
        print(f'{mode} {cipher_mode} with key= {args.key}')

    if args.cipher == 'caesar' or args.cipher == 'c':
        cipher_method=Caesar(args.key)
    elif args.cipher == 'vigenere' or args.cipher == 'v':
        cipher_method=Vignere(args.key)





if __name__ == '__main__':
    main()

