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
        if data_request:
            file = open(data_request, "w")
            print(f"Saving data to {data_request}")
            file.write(content)
            file.close()
            print(f"Data saved in file {data_request}.\n")
        else:
            print("Data not saved.\n")
    except Exception as e:
        error_msg = f"[STDERR] Error opening file '{sys.argv[1]}': {e}"
        print(error_msg, file=sys.stderr)
        print("Data not saved.\n")


def main() -> None:
    if len(sys.argv) == 2:
        print("=== Cyber Archives Recovery & Preservation ===")
        try:
            content = reader(sys.argv[1])
            print("Enter new file name (or empty): ", end="", flush=True)
            data_request = sys.stdin.readline().strip()
            writed(content, data_request)
        except Exception as e:
            error_msg = f"[STDERR] Error opening file '{sys.argv[1]}': {e}"
            print(error_msg, file=sys.stderr)
            print()
    else:
        print("Usage: ft_ancient_text.py <file>")


if __name__ == "__main__":
    main()
