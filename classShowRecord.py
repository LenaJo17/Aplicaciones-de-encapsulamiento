import tkinter as tk

class classShowRecord:
    def __init__(self, master, get_record_instance):
        self.__get_record_instance = get_record_instance

        # Crear elementos de la ventana
        tk.Button(master, text="Obtener Último Registro", command=self.__obtener_ultimo_registro).pack(pady=10)
        self.__resultado_label = tk.Label(master, text="", justify="left", font=("Arial", 12))
        self.__resultado_label.pack(pady=10)

    def __mostrar_datos(self, registro):
        texto = (
            f"ID: {registro['id']}\n"
            f"Nombre: {registro['nombre']}\n"
            f"Apellido: {registro['apellido']}\n"
            f"Ciudad: {registro['ciudad']}\n"
            f"Calle: {registro['calle']}"
        ) if registro else "No se encontraron registros."
        self.__resultado_label.config(text=texto)

    def __obtener_ultimo_registro(self):
        self.__mostrar_datos(self.__get_record_instance.get_last_record())


