import argparse
import os


def killTmux(sessionRoot):
    over = False
    suffix = ''
    while(not over):
        over = (os.system('tmux kill-session -t '
                          + sessionRoot + suffix) == 256)
        suffix = suffix + 'x'


def grabInputArgs():
    parser = argparse.ArgumentParser(
        description='This script kills all tmux sessions created by tmuxmux')
    parser.add_argument('sessionRoot', type=str,
                        help='Root name of tmux sessions to kill.')
    return parser.parse_args()


if __name__ == "__main__":
    args = grabInputArgs()
    killTmux(args.sessionRoot)
