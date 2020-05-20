import argparse
import numpy as np

def sumring(mod, lim, end):
    ls = np.arange(0, mod)
    result = ''
    print("Sum table for modulo" + str(mod))
    for i in range(mod):
        for u in range(mod):
            if u == mod -1:
                result += str((i+u) % mod) + end
            else:
                result += str((i+u)%mod) + lim

    print(result)

def multiplyring(mod, lim, end):
    ls = np.arange(0, mod)
    result = ''
    print("Multiplication table for modulo" + str(mod))
    for i in range(mod):
        for u in range(mod):
            if u == mod -1:
                result += str((i*u) % mod) + end
            else:
                result += str((i*+u)%mod) + lim

    print(result)

parser = argparse.ArgumentParser(description='Z-ring calculator')
parser.add_argument('mod', type=int, help="ring modulo")
parser.add_argument("-l", "--latex", help="print output in latex table format", action="store_true")
args = parser.parse_args()

def main():
    lim = "\t"
    end = "\n"
    if args.latex:
        lim = " & "
        end = " \\\\\n"
    sumring(args.mod, lim, end)
    multiplyring(args.mod, lim, end)

main()
