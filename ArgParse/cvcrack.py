"""
Author: Emir Cajlakovic 4CN
UE08
"""
import os
import sys

from Kasiski import Caesar, Vignere, Kasiski
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile',
        help='Input file to be cyphered')
    parser.add_argument('-c',
        '--cypher',
        help='Choose the cypher to use',
        type=str,
        nargs=1,
        choices=['caesar','c','vigenere','v']
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', action='store_true',
        help='Prints the cyphered text')
    group.add_argument('-q', '--quiet', action='store_true',
        help='Does not print the cyphered text')
    args = parser.parse_args()

    if args.cipher == 'caesar' or args.cipher == 'c':
        cipher_mode = 'Caesar'
    elif args.cipher == 'vigenere' or args.cipher == 'v':
        cipher_mode = 'Vignere'

    key: str = ""
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
    if args.verbose:
        print(f'Cracking {cipher_mode}-encryptetd file {args.infile}: Key=' + key)

    if args.quiet:
        print(key)

if __name__ == "__main__":
    main()