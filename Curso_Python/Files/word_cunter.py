from os import strerror
import os

try:
    counter = 0
    file_path = os.path.expanduser("~/Documents/Python/Curso_Python/Files/file.txt")
    stream = open(file_path, "rt")
    char = stream.read(1)
    while char != '':
        print(char, end='')
        counter += 1
        char = stream.read(1)
    stream.close()
    print("\n\nCaracteres en el archivo:", counter)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))