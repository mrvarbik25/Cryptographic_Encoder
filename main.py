#!/usr/bin/python3
input_string = input('>>> ').upper()

def choice():
    userChoice = int(input('\n(1)Encrypt (2)Decrypt: '))
    if userChoice == 1: encrypt(input_string)
    elif userChoice == 2: decrypt(input_string)
    else: raise SystemExit

def encrypt(string):
    for char in string:
        print(chr(ord(char) + 3), end='')
    print('')



def decrypt(string):
    for char in string:
        print(chr(ord(char) - 3), end='')
    print('')

def main():
    choice()

if __name__ == '__main__':
    main()