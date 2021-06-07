# by ToastedWaffless

# Use https://www.rapidtables.com/convert/number/binary-to-ascii.html
# for translating ascii to binary

import os

def clear():
    os.system('clear')

def execute_python_from_file(file):
    with open(file, "r") as f:
        binary_int = int(f.read(), 2)
        byte_number = binary_int.bit_length()

        binary_array = binary_int.to_bytes(byte_number, "big")
        ascii_text = binary_array.decode()
        ascii_text = ascii_text.replace("\x00", "")

        print("\n***EXECUTING BINARY***\n")

        try:
            exec(ascii_text)
        except:
            print("\n\n***END PROGRAM***\n")
            exit()

        print("\n***END PROGRAM***\n")
        exit()

def read_raw_bytes_from_file(file):
    with open(file, "r") as f:
        raw = ""
        binary_int = int(f.read(), 2)
        byte_number = binary_int.bit_length()
        binary_array = binary_int.to_bytes(byte_number, "big")
        ascii_text = binary_array.decode()
        ascii_text = ascii_text.replace("\x00", "")

        for l in ascii_text:
            hex_ = format(ord(l), "X")
            if len(hex_) < 2:
                hex_ = "0" + hex_
            raw += "\\x" + hex_

        print("\n***RAW BYTES***\n")

        print(raw)

        print("\n***END PROGRAM***\n")
        exit()

def read_from_bin_file(file):
    with open(file, "r") as f:
        binary_int = int(f.read(), 2)
        byte_number = binary_int.bit_length()

        binary_array = binary_int.to_bytes(byte_number, "big")
        ascii_text = binary_array.decode()
        ascii_text = ascii_text.replace("\x00", "")

        print("\n***BINARY TO ASCII***\n")

        print(ascii_text)

        print("\n***END PROGRAM***\n")
        exit()


def main():
    print("NOTE: Make sure binary file is formated")
    file = input("File to work with\n> ")
    if not os.path.exists(file):
        print(f"[-] The file: \"{file}\" does not exist")
        exit()

    print("[1] Translate from file")
    print("[2] Execute python from file")
    print("[3] Get raw-bytes from file\n")

    a = int(input(">"))
    if a == 1:
        read_from_bin_file(file)
    elif a == 2:
        execute_python_from_file(file)
    elif a == 3:
        read_raw_bytes_from_file(file)
    else:
        clear()
        main()


if __name__ == "__main__":
    main()
