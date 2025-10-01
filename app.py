
##Abrir fichero y lo cierra automaticamente
with open("files/fichero1.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)

##Escribir en un archivo
#Si el fichero no existe lo crea
with open("files/fichero2.txt","w",encoding="utf-8") as file:
    file.write("\nEste es el nuevo texto creado.\n")

##Volvemos a leer el fichero
with open("files/fichero1.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)

with open("files/fichero1.txt", "a", encoding="utf-8") as file:
    file.write("\nLo añade al final del fichero.\n")

## Leer de nuevo para mostrar los cambios
with open("files/fichero1.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)