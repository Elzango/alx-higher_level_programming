#!/usr/bin/python3
# 0-read_file.py
# Arth: Mahmud
"""Defines a text file-reading function."""
def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")

