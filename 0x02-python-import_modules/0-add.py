#!/usr/bin/python3
# 0-add.py - imports a function that adds two values and display them to stdout
# arth: Mahmud Zango

if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
