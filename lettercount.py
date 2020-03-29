from string import ascii_lowercase
import sys

def lettercount(input_text):
    """Return the amount of all alphabetical characters in text"""
    input_text = "".join(input_text.split()) # remove whitespace
    total = len(input_text)
    result = 'total: ' + str(total) + '\n' # result string to be constructed
    for c in ascii_lowercase:
        count = 0
        for letter in input_text:
            if letter == c:
                count = count + 1
        percentage = '{0:.2f}'.format(count / total * 100)
        result = result + str(c) + " " + str(count) + " \t"+ percentage + "%" + "\n"
    print(result)

def main():
    if len(sys.argv) < 2:
        text = """"xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpit
        ghlxiwiwtxgqadds."""
    else:
        try:
            f = open(sys.argv[1])
            text = f.read()
        except:
            text = sys.argv[1]
    print(text)
    lettercount(text)
    f.close()


main()

