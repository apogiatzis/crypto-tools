import argparse
from pwn import *
from Crypto.Util.number import long_to_bytes

"""
Requires Python 3.2+
"""

"""
Default table is base58
"""
table='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def baseNencode(text):
    """
    Encode string to baseN
    """
    N = len(table)
    text_as_int = int.from_bytes(text.encode(), 'big')
    encoded = ''
    while text_as_int > 0:
        encoded += table[text_as_int % N]
        text_as_int //= N
    return encoded[::-1] 

def baseNdecode(text):
    """
    Decode string to baseN
    """
    N = len(table)
    decoded = 0
    for c in text:
        decoded *= N
        decoded += table.index(c)
    return long_to_bytes(decoded)

if __name__ == '__main__':
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-e", "--encode", help="String to encode")
    ap.add_argument("-d", "--decode", help="String to decode")
    args = vars(ap.parse_args())

    if args['encode']:
        print('Encoded text: ', baseNencode(args['encode']))

    if args['decode']:
        print('Decoded text: ', baseNdecode(args['decode']))