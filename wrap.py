import argparse


def wrap(file, maxLength=80):
    with open(file, 'r') as f:
        allLines = f.readlines()

    newLines = []
    for line in allLines:
        newLines += splitLine(line)

    with open(file, 'w') as f:
        f.writelines(newLines)


def splitLine(line, maxLength=80):
    if len(line) <= maxLength:
        return [line]
    splits = []
    lastSpaceInd = line[:maxLength].rfind(' ')
    splits = [line[:lastSpaceInd] + '\n'] + splitLine(line[lastSpaceInd + 1:])
    return splits


def grabInputArgs():
    parser = argparse.ArgumentParser(
        description='This script wraps all lines in the given file upto '
                    'maxLength provided (default 80)')
    parser.add_argument('file', type=str,
                        help='File name with path to wrap',
                        default=None)
    parser.add_argument('-l', '--maxLength', type=int,
                        help='Maximum Lenght of a line in file. Default 80.',
                        default=80)
    return parser.parse_args()


if __name__ == "__main__":
    args = grabInputArgs()
    wrap(file=args.file, maxLength=args.maxLength)
