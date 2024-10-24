import tkinter as tk
from classGetRecord import GetRecord
from classShowRecord import classShowRecord

class AppDB:
    def __init__(self):
        self.root = tk.Tk()  # Crear la ventana principal
        self.get_record_instance = GetRecord()  # Crear la instancia de GetRecord
        self.show_record_instance = classShowRecord(self.root, self.get_record_instance)  # Crear la instancia de classShowRecord
        self.root.mainloop()  # Iniciar la aplicación

# Ejecución de la aplicación
if __name__ == "__main__":
    AppDB()  # Instancia y ejecuta la aplicación



