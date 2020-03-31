from string import ascii_lowercase
import argparse

def lettercount(input_text):
    """Return the amount of all alphabetical characters in text"""
    input_text = input_text.lower()
    input_text = "".join(input_text.split()) # remove whitespace
    total = len(input_text)
    result = 'total: ' + str(total) + '\n' # result string to be constructed
    for c in ascii_lowercase:
        count = 0
        for letter in input_text:
            if letter == c:
                count = count + 1
        percentage = '{0:.2f}'.format(count / total * 100)
        result = result + str(c.upper()) + " " + str(count) + " \t"+ percentage + "%" + "\n"
    print(result)

parser = argparse.ArgumentParser(description='Count letter frequencies')
parser.add_argument('input', help='input text or file')

args = parser.parse_args()

def main():
    try:
        inputfile = open(args.input[0])
        text = inputfile.read()
        inputfile.close()
    except IOError:
        text = args.input
    print(text)
    lettercount(text)


main()
