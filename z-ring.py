import argparse
import numpy as np

def sumring(mod):
    ls = np.arange(0, mod)
    result = ''
    print("Sum table for modulo" + str(mod))
    for i in range(mod):
        for u in range(mod):
            if u == mod -1:
                result += str((i+u) % mod) + 2*'\n'
            else:
                result += str((i+u)%mod) + "\t"

    print(result)

def multiplyring(mod):
    ls = np.arange(0, mod)
    result = ''
    print("Multiplication table for modulo" + str(mod))
    for i in range(mod):
        for u in range(mod):
            if u == mod -1:
                result += str((i*u) % mod) + 2*'\n'
            else:
                result += str((i*+u)%mod) + "\t"

    print(result)

""" Debugging
mod = 5
sumring(mod)
multiplyring(mod)
"""
parser = argparse.ArgumentParser(description='Z-ring calculator')
parser.add_argument('mod', type=int, help="ring modulo")
args = parser.parse_args()
def main():
    sumring(args.mod)
    multiplyring(args.mod)

main()
