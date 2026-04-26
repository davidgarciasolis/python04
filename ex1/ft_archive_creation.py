#!/usr/bin/env python3
import sys


def reader(name_file: str) -> str:
    print(f"Accessing file '{name_file}'")
    file = open(name_file, "r")
    content = file.read()
    print("---\n")
    print(content)
    print("\n---")
    print("File 'ancient_fragment.txt' closed.\n")
    file.close()
    return (content)


def writed(content: str, data_request: str) -> None:
    result = content.replace("\n", "#\n") + "#"
    try:
        file = open(data_request, "w")
        file.write(result)
        file.close()
    except FileNotFoundError:
        print("Not saving data.")


def main() -> None:
    if len(sys.argv) == 2:
        try:
            content = reader(sys.argv[1])
            data_request = input("Enter new file name (or empty): ")
            writed(content, data_request)
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
    else:
        print("Usage: ft_ancient_text.py <file>")


if __name__ == "__main__":
    main()
