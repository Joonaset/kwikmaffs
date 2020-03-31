from string import ascii_lowercase
import re
import argparse

exp = re.compile("[a-z]")

def decrypt(inputtext, key):
    print("INPUT: ", inputtext)
    print("KEY: ", key)
    inputtext = inputtext.lower()
    inputtext = exp.findall(inputtext)
    inputtext = "".join(inputtext)
    key = key.lower()
    key = exp.findall(key)
    key = "".join(key)
    result = ''
    for i in range(len(inputtext)):
        inchar = inputtext[i]
        keychar = key[i % len(key)] # loop key if cipher text longer than key
        keyvalue = ascii_lowercase.index(keychar)
        decrypted = ascii_lowercase[(ascii_lowercase.index(inchar) - keyvalue) % 26]
        result = result + decrypted
    print(result)

#decrypt("bsasppkkuosp", "rsidpydkawoa") # debug purposes, should result in "kaspar hausep"

def encrypt(inputtext, key):
    print("INPUT: ", inputtext)
    print("KEY: ", key)
    inputtext = inputtext.lower()
    inputtext = exp.findall(inputtext)
    inputtext = "".join(inputtext)
    key = key.lower()
    key = exp.findall(key)
    key = "".join(key)
    result = ''
    for i in range(len(inputtext)):
        inchar = inputtext[i]
        keychar = key[i]
        keyvalue = ascii_lowercase.index(keychar)
        encrypted = ascii_lowercase[(ascii_lowercase.index(inchar) + keyvalue) % 26]
        result = result + encrypted
    print(result)
#encrypt("kasparhauser", "rsidpydkawoa")

parser = argparse.ArgumentParser(description='Vigenere cipher decryptor and encryptor')
parser.add_argument('crypt', choices=["d", "e"], help="decrypt input")
parser.add_argument('input', nargs=1, help="input file or text")
parser.add_argument('key', nargs=1, help="key file or text")

args = parser.parse_args()

def main():
    try:
        inputfile = open(args.input[0])
        inputtext = inputfile.read()
        inputtext = inputtext[:-1]
        inputfile.close()
    except IOError:
        inputtext = args.input[0]
    try:
        keyfile = open(args.key[0])
        key = keyfile.read()
        key = key[:-1]
        keyfile.close()
    except IOError:
        key = args.key[0]
    if not args.crypt:
        print("provide -d or -e option")
    elif args.crypt == "e":
        encrypt(inputtext, key)
    elif args.crypt == "d":
        decrypt(inputtext, key)

main()
