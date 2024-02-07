#!/usr/bin/python3


def read_file(filename=""):
    """Reads a text file and prints its content to stdout.

    Args:
        filename (str): The name of the file to read from.

    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")

# Example usage:
read_file("example.txt")
