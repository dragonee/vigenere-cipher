# Vigenère cipher

This tool allows for encoding/decoding files using Vigenère cipher.

    cipher.py [-d] PASSPHRASE < FILE

Main reason to write this was to translate Morrowind documents:

 - http://en.uesp.net/wiki/Morrowind:Sottilde's_Code_Book
 - http://en.uesp.net/wiki/Morrowind:Package_for_Caius_Cosades

However, it can be used for other purposes too.

To use the tool, you still need to strip HTML from the books.

See https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher for more detailed explanation.

## Installation

Requires Python 3.

Install dependencies with pip:

    pip3 install -r requirements.txt

At this point, you will be able to use the script.
