# main.py
# Punto de entrada principal de la aplicación

from app.menu import show_menu
from app.notes import add_note, view_notes, delete_notes

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_notes()
        elif choice == "4":
            print("Exiting Note-Taking App. Goodbye")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
