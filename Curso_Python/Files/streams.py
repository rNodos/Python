import os

try:
    file_path = os.path.expanduser("~/Documents/Python/Curso_Python/Files/file.txt")
    stream = open(file_path, "rt")
    print("Archivo abierto con éxito.")
    stream.close()
except Exception as exc:
    print("No se puede abrir el archivo:", exc)

