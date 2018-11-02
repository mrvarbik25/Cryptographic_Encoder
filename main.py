
try:
    filename = input('The file in which the archive will be encrypted: ')
    with open(filename, 'rb') as file1:
        read1 = file1.read()
except FileNotFoundError:
    print('[x] File not found')
    raise SystemExit
try:
    zip = input('Archive to encrypt to file: ')
    with open(zip, 'rb') as file2:
        read2 = file2.read()
except FileNotFoundError:
    print('[x] File not found')
    raise SystemExit
with open(filename, 'wb') as file3:
    file3.write(read1)
    file3.write(read2)
print('[+] Successfully overwritten the file.')
