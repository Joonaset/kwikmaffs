# Kvikmaffs

This repository is collection of scripts and tools for mathematical purposes. For now, it will be populated with tools for cryptomathematical purposes.

# Scripts

## lettercount.py

Counts lowercase alphabetic characters and their frequency in given text. Usage example:

`lettercount.py example.txt` or ` lettercount.py "this is example string"`

## vignere.py

Encrypt or decrypt text by vignere algorithm. works only on lowercase a-z characters. Usage example:

` vignere.py -d -i inputfile -k keytext`

`vignere.py -e -i "input text" -k keyfile.txt`
