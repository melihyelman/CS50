import sys
from cs50 import get_string

def main():
    if len(sys.argv) != 2:
        print("Usage: ./caesar k")
        sys.exit(1)

    key = int(sys.argv[1])
    plaintext = get_string("plaintext: ")

    print("ciphertext: ", end="")

    for i in plaintext:
        if not i.isalpha():
            print(i, end="")
            continue

        ascii= 65 if i.isupper() else 97

        a = ord(i) - ascii
        b = (a + key) % 26

        print(chr(b + ascii), end="")

    print()

if __name__ == "__main__":
    main()