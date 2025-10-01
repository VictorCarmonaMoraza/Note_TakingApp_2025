# 📂 Abrir fichero en modo lectura ("r")
# 'with open' abre el archivo y lo cierra automáticamente al salir del bloque
with open("files/fichero1.txt", "r", encoding="utf-8") as file:
    content = file.read()        # Lee TODO el contenido del archivo como un string
    print(content)               # Imprime el contenido en la consola

# 📂 Escribir en un archivo en modo escritura ("w")
# Si el fichero no existe, se crea. Si ya existe, su contenido se BORRA
with open("files/fichero2.txt", "w", encoding="utf-8") as file:
    file.write("\nEste es el nuevo texto creado.\n")  # Escribe el texto dentro del archivo

# 📂 Volver a leer el fichero original (fichero1.txt)
with open("files/fichero1.txt", "r", encoding="utf-8") as file:
    content = file.read()        # Lee de nuevo todo el contenido
    print(content)               # Lo muestra en consola

# 📂 Abrir el fichero en modo append ("a")
# "a" significa añadir: no borra el contenido previo, todo lo nuevo se escribe al FINAL
with open("files/fichero1.txt", "a", encoding="utf-8") as file:
    file.write("\nLo añade al final del fichero.\n")  # Añade este texto al final del archivo

# 📂 Leer otra vez el fichero original para mostrar los cambios
with open("files/fichero1.txt", "r", encoding="utf-8") as file:
    content = file.read()        # Lee el contenido actualizado
    print(content)               # Imprime todo el contenido (incluyendo lo añadido al final)
