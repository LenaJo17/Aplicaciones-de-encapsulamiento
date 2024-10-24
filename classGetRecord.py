import requests
from tkinter import messagebox

class GetRecord:
    def __init__(self):  # Corrige _init_ a __init__
        self.__url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"

    def get_last_record(self):  # Cambié a snake_case para consistencia
        try:
            respuesta = requests.get(self.__url)
            respuesta.raise_for_status()  # Verifica si la solicitud tuvo éxito

            datos = respuesta.json()

            if datos:
                return datos[-1]  # Devuelve el último registro
            else:
                messagebox.showinfo("Información", "No hay registros disponibles.")
                return None

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"No se pudo obtener el registro: {e}")
            return None
