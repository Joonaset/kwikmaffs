from string import ascii_lowercase
import argparse

def decrypt(inputtext, key):
    result = ''
    for i in range(len(inputtext)):
        inchar = inputtext[i]
        keychar = key[i % len(key)] # loop key if cipher text longer than key
        keyvalue = ascii_lowercase.index(keychar)
        decrypted = ascii_lowercase[(ascii_lowercase.index(inchar) - keyvalue) % 26]
        result = result + decrypted
    print(result)

#decrypt("bsasppkkuosp", "rsidpydkawoa")

def encrypt(inputtext, key):
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
parser.add_argument('-d', '--decrypt', dest='crypt', action='store_const', const=1, help="decrypt input")
parser.add_argument('-e', '--encrypt', dest='crypt', action='store_const', const=0, help="decrypt input")
parser.add_argument('-i', '--input', nargs=1, help="input file or text")
parser.add_argument('-k', '--key', nargs=1, help="key file or text")

args = parser.parse_args()

def main():
    print(args.crypt)
    try:
        inputfile = open(args.input[0])
        inputtext = inputfile.read()
        inputfile.close()
    except IOError:
        inputtext = args.input[0]
    try:
        keyfile = open(args.key[0])
        key = keyfile.read()
        keyfile.close()
    except IOError:
        key = args.key[0]
    if not args.crypt:
        print("provide -d or -e option")
    elif args.crypt == 0:
        encrypt(inputtext, key)
    else:
        decrypt(inputtext, key)

main()
