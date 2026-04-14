#!/usr/bin/env python3

def secure_archive(
    name_file: str, option: str = "r", data: str = ""
) -> tuple[bool, str]:
    try:
        with open(name_file, option) as file:
            if (option == "r"):
                data = file.read()
            elif (option == "w"):
                file.write(data)
                data = "Content successfully written to file"
        return (True, data)
    except Exception as e:
        return (False, str(e))


def main():
    options = ["r", "w"]
    data = ""
    for option in options:
        while True:
            file_name = input(
                "Using'secure_archive' to read from a nonexistent file: ")
            result = secure_archive(file_name, option, data)
            print(result)
            if (result[0]):
                data = result[1]
                break


if __name__ == "__main__":
    main()
