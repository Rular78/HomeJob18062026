# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import inspect
import os

import oc


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print_hi("PyCharm")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import os

# Быстрый способ увидеть все функции
# print([name for name in dir(os) if callable(getattr(os, name))])
print([name for name in dir(oc) if callable(getattr(oc, name))])
