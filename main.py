#!/usr/bin/python3


import sys
import subprocess
import re
import click
from colorama import Fore, Style
from time import sleep


def test_func():
    """ TODO delete function"""
    identify = 0
    for i in range(3):
        identify += i
    list_date = True
    if identify is not None:
        list_date = list(range(5))
    res = identify in list_date
    return res


def split_string(string2, range2):
    """разбивает строку по диапазону"""
    before = string2[:range2[0]]
    middle = string2[range2[0]:range2[1]]
    after = string2[range2[1]:]
    return before, middle, after


def color_string(regexp, text):
    """разукращивает в тексте совпадения по регулярке"""
    if re.search(regexp, text) is None:
        return False
    res = ""
    symbol = True
    while symbol:
        symbol = re.search(regexp, text)
        if not symbol:
            break
        split = split_string(text, symbol.span())
        res += split[0] + f"{Fore.RED}{split[1]}{Style.RESET_ALL}"
        text = split[2]
    res += text
    return res


@click.command()
@click.argument('pattern')
@click.argument('file')
def main(pattern, file):
    """occur"""
    file = file
    try:
        while True:
            subprocess.call("clear")
            with open(file, "r", encoding="utf-8") as f:
                for line in enumerate(f, start=1):
                    string = color_string(pattern, line[1])
                    if string is False:
                        continue
                    print(Fore.GREEN + str(line[0]) + ":" + Style.RESET_ALL, end="")
                    print(string, end="")
            sleep(1)
    except KeyboardInterrupt:
        print("[ Stop ]")
        sys.exit(0)
    except re.error:
        print("[ error regexp ]")
        sys.exit(0)


if __name__ == "__main__":
    main()
