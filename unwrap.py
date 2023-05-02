#!/opt/anaconda3/bin/python

import argparse


def unwrap(file):
    if isinstance(file, list):
        for f in file:
            unwrap(f)
        return
    with open(file, 'r') as f:
        allLines = f.readlines()

    newLines = []
    stopUnwrapping = False
    for line in allLines:
        if line == '\n':
            newLines += ['\n', line]
        elif line.find(r'\label') != -1:
            newLines += [line]
        elif line.find(r'\section') != -1:
            newLines += ['\n', line]
        elif line.find(r'\subsection') != -1:
            newLines += ['\n', line]
        elif (line.find(r'\begin{equation}') != -1
              or line.find(r'\begin{subequations}') != -1):
            newLines += ['\n', line]
            stopUnwrapping = True
        elif (line.find(r'\end{equation}') != -1
              or line.find(r'\end{subequation}') != -1):
            newLines += [line]
            stopUnwrapping = False
        else:
            if stopUnwrapping:
                newLines += [line]
            else:
                newLines += [line.replace('\n', ' ')]

    with open(file, 'w') as f:
        f.writelines(newLines)


def grabInputArgs():
    parser = argparse.ArgumentParser(
        description='This script unwraps wrapped file.')
    parser.add_argument('file', nargs='+',
                        help='File path(s) to wrap separated by space',
                        default=None)
    return parser.parse_args()


if __name__ == "__main__":
    args = grabInputArgs()
    unwrap(file=args.file)
