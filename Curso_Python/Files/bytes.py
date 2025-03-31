from os import strerror
import os

data = bytearray(10)

try:
    file_path = os.path.expanduser("~/Documents/Python/Curso_Python/Files/file.bin")
    binary_file = open(file_path, 'rb')
    binary_file.readinto(data)
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))