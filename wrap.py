import argparse


def wrap(file, maxLength=80, colPar=False):
    with open(file, 'r') as f:
        allLines = f.readlines()

    newLines = []
    if colPar:
        colLines = []
        par = ''
        for ii, line in enumerate(allLines):
            if (line == '\n'
                or line[0] == '\\'
                or line[0] == '%'
                or line[0] == ' '):
                if par != '':
                    colLines += [par + '\n', line]
                else:
                    colLines += [line]
                par = ''
            else:
                if len(par) > 0:
                    if par[-1] != ' ':
                        par += ' '
                par += line[:-1]
        colLines += [par + '\n']
        allLines = colLines

    for line in allLines:
        newLines += splitLine(line)

    with open(file, 'w') as f:
        f.writelines(newLines)


def splitLine(line, maxLength=80):
    if len(line) <= maxLength:
        return [line]
    lastSpaceInd = line[:maxLength].rfind(' ')
    if lastSpaceInd == -1:
        print('Did not break continuous line:')
        print(line)
        return [line]
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
    parser.add_argument('-p', '--colPar',
                        help="Collect paragraphs. Text separated by 1 line "
                             "atleast will be considered a separate "
                             "paragraph. Use with care.",
                        action='store_true')
    return parser.parse_args()


if __name__ == "__main__":
    args = grabInputArgs()
    wrap(file=args.file, maxLength=args.maxLength, colPar=args.colPar)
