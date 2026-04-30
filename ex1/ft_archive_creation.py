#!/usr/bin/env python3
import sys


def reader(name_file: str) -> str:
    print(f"Accessing file '{name_file}'")
    file = open(name_file, "r")
    content = file.read()
    print("---\n")
    print(content)
    print("---")
    print("File 'ancient_fragment.txt' closed.\n")
    file.close()
    print("Transform data:")
    print("---\n")
    content = content.replace("\n", "#\n")
    print(content)
    print("---")
    return (content)


def writed(content: str, data_request: str) -> None:
    try:
        file = open(data_request, "w")
        print(f"Saving data to {data_request}")
        file.write(content)
        file.close()
        print(f"Data saved in file {data_request}.\n")
    except Exception:
        print("Not saving data.\n")


def main() -> None:
    if len(sys.argv) == 2:
        print("=== Cyber Archives Recovery & Preservation ===")
        try:
            content = reader(sys.argv[1])
            data_request = input("Enter new file name (or empty): ")
            writed(content, data_request)
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}\n")
    else:
        print("Usage: ft_ancient_text.py <file>")


if __name__ == "__main__":
    main()
