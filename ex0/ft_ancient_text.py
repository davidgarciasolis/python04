#!/usr/bin/env python3
import sys


def reader(name_file: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{name_file}'")
    file = open(name_file, "r")
    content = file.read()
    print("---\n")
    print(content)
    print("---")
    print("File 'ancient_fragment.txt' closed.\n")
    file.close()


def main() -> None:
    if len(sys.argv) == 2:
        try:
            reader(sys.argv[1])
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}\n")
    else:
        print("Usage: ft_ancient_text.py <file>\n")


if __name__ == "__main__":
    main()
