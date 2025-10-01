# notes.py
# Funciones para añadir, ver y borrar notas

FILE_NAME = "../files/Notas_2025.txt"

# Añadir una nueva nota
def add_note():
    note = input("Enter your note: ")
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(note + "\n")
    print("Note added successfully.")

# Ver todas las notas
def view_notes():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            content = file.read()
            if content:
                print("\n--- All Notes ---")
                print(content)
            else:
                print("No notes found.")
    except FileNotFoundError:
        print("No notes found.")

# Borrar todas las notas
def delete_notes():
    confirm = input("Are you sure you want to delete all notes? (Yes/n): ")
    if confirm.lower() == "yes":
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            pass  # Deja el fichero vacío
        print("All notes have been deleted.")
    else:
        print("Delete cancelled.")
