""" 
Curso Python empresa de 'Lenguaje de Programación Python'

Autor: José Antonio Calvo López

Fecha: Noviembre 2023

"""

from tkinter import filedialog, simpledialog, messagebox, Tk, Button, PhotoImage
from PIL import Image
import tkinter as tk
import sys, os
import mariadb
from PyQt5 import QtWidgets
from LogDialog import LoginDialog  # Asegúrate de que esta importación sea correcta

def seleccionar_y_procesar_imagen():
    # Abre un diálogo para seleccionar la imagen
    file_path = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg;*.webp")])
    if file_path:
        # Se piden las dimensiones de la imagen
        ancho, alto = solicitar_dimensiones()
        
        # Llama a la función para procesar la imagen
        convertir_y_redimensionar_imagen(file_path, ancho, alto)

def resource_path(relative_path):
    """ Obtener el camino absoluto al recurso, funciona para el desarrollo y para el ejecutable único """
    try:
        # PyInstaller crea un directorio temporal y almacena el path en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def solicitar_dimensiones():
    # Se pide al usuario los valores de ancho y alto, se perimten valores vacios.
    ancho = simpledialog.askstring("Ancho", "Dame el ancho (en blanco valor original):")
    alto = simpledialog.askstring("Alto", "Dame el alto (en blanco valor original):")

    try:
        if ancho:
            ancho = int(ancho)
        else:
            ancho = None
        # Otra forma de sintaxis de condición, operador ternario
        alto = int(alto) if alto else None

    except ValueError:
        print("Error en los tamaños.")
        messagebox.showerror("Error", "Las dimensiones no son correctas" + "\nSe mantendrá el tamaño original")
        return None, None
    
    return ancho, alto

def convertir_y_redimensionar_imagen(ruta_entrada, ancho, alto):
    with Image.open(ruta_entrada) as img:
        # Cuando las dimensiones son válidas redimensiona
        if ancho and alto:
            img = img.resize((ancho, alto))

        # Pasa la imagen a WEBP
        ruta_salida = filedialog.asksaveasfilename(defaultextension=".webp", filetypes=[("WEBP", "*.webp")])
        if ruta_salida:
            img.save(ruta_salida, format="webp")
            print("Archivo WEBP guardado en:", ruta_salida)

def mostrar_ventana_principal():
    app = Tk()
    app.title("Redimensión y conversión a WEBP")
    app.geometry("400x200")
    app.eval('tk::PlaceWindow . center')
    app.resizable(False, False)

    icono_ruta = resource_path("Studium.png")
    fondo_ruta = resource_path("ImgCurso.png")

    icono = PhotoImage(file=icono_ruta)
    background_image = PhotoImage(file=fondo_ruta)

    background_label = tk.Label(app, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    select_button = Button(app, text="Selecciona una imagen", command=seleccionar_y_procesar_imagen)
    select_button.pack(pady=20)

    app.iconphoto(True,icono)
    app.mainloop()

def main():
    # Configurar la conexión a la base de datos
    try:
        db = mariadb.connect(
            host= "informaticosonline.es",
            user="ofluqcym_UsuLicencias",
            password="#JACL1970",
            database= "ofluqcym_Licencias"
        )

    except mariadb.Error as e:
        print(f"Error conectando a MariaDB: {e}")
        sys.exit(1)

    # Crear y mostrar el diálogo de inicio de sesión
    app = QtWidgets.QApplication(sys.argv)
    login_dialog = LoginDialog(db)
    if login_dialog.exec_() == QtWidgets.QDialog.Accepted:
        mostrar_ventana_principal()

if __name__ == "__main__":
    main()

