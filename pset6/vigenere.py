import sys
from cs50 import get_string


def valid(key):
    for i in key:
        if not i.isalpha():
            return False
    return True


def main():
    if len(sys.argv) != 2 or not valid(sys.argv[1]):
        print("Usage: ./vigenere k")
        sys.exit(1)

    key = sys.argv[1]
    plaintext = get_string("plaintext: ")
    j = 0

    print("ciphertext: ", end="")

    for i in plaintext:
        if not i.isalpha():
            print(i, end="")
            continue

        ascii = 65 if i.isupper() else 97

        a = ord(i) - ascii
        b = ord(key[j % len(key)].upper()) - 65
        c = (a + b) % 26
        j += 1

        print(chr(c + ascii), end="")

    print()

    return 0


if __name__ == "__main__":
    main()