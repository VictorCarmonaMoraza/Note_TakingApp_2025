📝 Note-Taking App (Python)

Una sencilla aplicación de consola en Python para gestionar notas: añadir, ver y borrar notas de manera rápida y organizada.

🚀 Características

➕ Añadir notas al archivo Notas_2025.txt.

👀 Visualizar todas las notas guardadas.

🗑️ Borrar todas las notas con confirmación de seguridad.

📂 Organización en módulos (menu.py, notes.py, main.py).

📂 Estructura del proyecto

NoteTakingApp_11/
│── files/
│   └── Notas_2025.txt        # Archivo donde se almacenan las notas
│
│── app/
│   ├── __init__.py           # Marca la carpeta como un paquete Python
│   ├── menu.py               # Funciones relacionadas con el menú
│   ├── notes.py              # Funciones de gestión de notas
│   └── main.py               # Punto de entrada de la aplicación
│
└── README.md


⚙️ Requisitos

Python 3.12+

(Opcional) Entorno virtual para aislar dependencias:
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

▶️ Ejecución

Desde la raíz del proyecto, ejecuta:

python -m app.main

📌 Uso

Al iniciar, verás el menú principal:

--- Note-Taking App Menu ---
1. Add a new note
2. View all notes
3. Delete all notes
4. Exit


Elige una opción:

1 → Añadir una nueva nota.

2 → Ver todas las notas.

3 → Borrar todas las notas (con confirmación).

4 → Salir de la aplicación.

💡 Ejemplo
--- Note-Taking App Menu ---
1. Add a new note
2. View all notes
3. Delete all notes
4. Exit
Enter your choice (1-4): 1
Enter your note: Comprar leche
Note added successfully.

📖 Futuras mejoras

Exportar notas en formato JSON/CSV.

Buscar notas por palabras clave.

Interfaz gráfica con Tkinter o PyQt.

👉 Con este README cualquier persona podría clonar tu repo y usar la aplicación en minutos.