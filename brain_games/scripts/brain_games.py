#!/usr/bin/env python3

from brain_games.cli import run


def greet():
    print('Welcome to Brain Games!\n')
    print(run())


def main():
    greet()


if __name__ == '__main__':
    main()
