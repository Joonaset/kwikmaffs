from string import ascii_lowercase
import argparse

def decrypt(inputtext, key):
    inputtext = "".join(inputtext.split())
    key = "".join(key.split())
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
    inputtext = "".join(inputtext.split())
    key = "".join(key.split())
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
    elif args.crypt == 0:
        encrypt(inputtext, key)
    else:
        decrypt(inputtext, key)

main()
