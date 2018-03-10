#!/usr/bin/env python3
"""
Encrypt a message using Vigenère_cipher.

Usage:
    cipher [-d] KEY

Options:
    -d          Decode a message.
    --help      Show this message.
    --version   Show version information.

"""

VERSION='1.0'

import sys
from itertools import cycle
from docopt import docopt

args = docopt(__doc__, version=VERSION)

key = args['KEY']

i = cycle(key)

import string

for line in sys.stdin:
    for letter in line:
        num_letter = ord(letter)

        if letter in string.ascii_uppercase:
            lowercase = False
        elif letter in string.ascii_lowercase:
            lowercase = True
            num_letter -= 32
        else:
            sys.stdout.write(letter)
            continue

        num_letter -= 65

        code = next(i)
        num_code = ord(code)
        
        if code in string.ascii_lowercase:
            num_code -= 32

        num_code -= 65

        if args['-d']:
            diff = num_letter - num_code
        else:
            diff = num_letter + num_code

        if diff < 0:
            diff += 26
        elif diff > 25:
            diff -= 26

        sys.stdout.write(chr(diff + (97 if lowercase else 65)))

sys.stdout.flush()
