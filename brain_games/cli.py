#!/usr/bin/env python3

import prompt


def run():
    name = prompt.string('May I have your name? ')
    return ('Hello, ' + name + '!')


def main():
    run()


if __name__ == '__main__':
    main()
