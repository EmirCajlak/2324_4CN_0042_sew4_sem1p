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





if __name__ == "__main__":
    main()