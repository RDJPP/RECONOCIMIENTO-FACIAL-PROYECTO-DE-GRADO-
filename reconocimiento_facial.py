# --------------------------------------Importamos librerias--------------------------------------------
import tkinter as tk
from tkinter import *
import os
import cv2
from matplotlib import pyplot
from mtcnn import MTCNN
import numpy as np
from tkinter import Tk, Button, Entry, Label, ttk, PhotoImage
from tkinter import StringVar, Scrollbar, Frame
from conexion import *
import time


# ------------------------ Crearemos una funcion que se encargara de registrar el usuario ---------------------


def registrar_usuario():
    usuario_info = usuario.get()  # Obetnemos la informacion almacenada en usuario
    contra_info = contra.get()  # Obtenemos la informacion almacenada en contra

    archivo = open(usuario_info, "w")  # Abriremos la informacion en modo escritura
    archivo.write(usuario_info + "\n")  # escribimos la info
    archivo.write(contra_info)
    archivo.close()

    # Limpiaremos los text variable
    usuario_entrada.delete(0, END)
    contra_entrada.delete(0, END)

    # Ahora le diremos al usuario que su registro ha sido exitoso
    
    global ventana8
    ventana8 = Toplevel()
    ventana8.geometry("300x200")
    ventana8.title("Registro usuario")
    Label(ventana8, text="").pack()
    Label(ventana8, text="").pack()
    Label(ventana8, text="").pack()
    Label(ventana8, text="Registro de usuario exitoso", font=("Century Gothic", 12)).pack()
    Label(ventana8, text="").pack()
    Label(ventana8, text="").pack()
    Button(ventana8, text="Ok", width=15, height=1,bg="#BA5649",
            fg="white", command=registro_usuario).pack()


# --------------------------- Funcion para almacenar el registro facial --------------------------------------


def registro_facial():
    # Vamos a capturar el rostro
    cap = cv2.VideoCapture(0)  # Elegimos la camara con la que vamos a hacer la deteccion
    while True:
        ret, frame = cap.read()  # Leemos el video
        cv2.imshow("Registro Facial", frame)  # Mostramos el video en pantalla
        if cv2.waitKey(1) == 27:  # Cuando oprimamos "Escape" rompe el video
            break
    usuario_img = usuario.get()
    cv2.imwrite(
        usuario_img + ".jpg", frame
    )  # Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
    cap.release()  # Cerramos
    cv2.destroyAllWindows()

    usuario_entrada.delete(0, END)  # Limpiamos los text variables
    contra_entrada.delete(0, END)
    # Label(pantalla1, text = "Registro Facial Exitoso", fg = "green", font = ("Calibri",11)).pack()
    global ventana10
    ventana10 = Toplevel()
    ventana10.geometry("300x200")
    ventana10.title("Registro usuario")
    Label(ventana10, text="").pack()
    Label(ventana10, text="").pack()
    Label(ventana10, text="").pack()
    Label(ventana10, text="Registro facial usuario exitoso", font=("Century Gothic", 12)).pack()
    Label(ventana10, text="").pack()
    Label(ventana10, text="").pack()
    Button(ventana10, text="Ok", width=15, height=1,bg="#BA5649",
            fg="white", command=cerrar_facial_2).pack()

    # ----------------- Detectamos el rostro y exportamos los pixeles --------------------------

    def reg_rostro(img, lista_resultados):
        data = pyplot.imread(img)
        for i in range(len(lista_resultados)):
            x1, y1, ancho, alto = lista_resultados[i]["box"]
            x2, y2 = x1 + ancho, y1 + alto
            pyplot.subplot(1, len(lista_resultados), i + 1)
            pyplot.axis("off")
            cara_reg = data[y1:y2, x1:x2]
            cara_reg = cv2.resize(
                cara_reg, (150, 200), interpolation=cv2.INTER_CUBIC
            )  # Guardamos la imagen con un tamaño de 150x200
            cv2.imwrite(usuario_img + ".jpg", cara_reg)
            pyplot.imshow(data[y1:y2, x1:x2])
        pyplot.show()

    img = usuario_img + ".jpg"
    pixeles = pyplot.imread(img)
    detector = MTCNN()
    caras = detector.detect_faces(pixeles)
    reg_rostro(img, caras)


# --------------------------------SEGUNDO REGISTRO FACIAL------------------------------

#Esta funcion registra la cara del usuario

    # ----------------- Detectamos el rostro y exportamos los pixeles --------------------------

    def reg_rostro(img, lista_resultados):
        data = pyplot.imread(img)
        for i in range(len(lista_resultados)):
            x1, y1, ancho, alto = lista_resultados[i]["box"]
            x2, y2 = x1 + ancho, y1 + alto
            pyplot.subplot(1, len(lista_resultados), i + 1)
            pyplot.axis("off")
            cara_reg = data[y1:y2, x1:x2]
            cara_reg = cv2.resize(
                cara_reg, (150, 200), interpolation=cv2.INTER_CUBIC
            )  # Guardamos la imagen con un tamaño de 150x200
            cv2.imwrite(usuario_img + ".jpg", cara_reg)
            pyplot.imshow(data[y1:y2, x1:x2])
        pyplot.show()

    img = usuario_img + ".jpg"
    pixeles = pyplot.imread(img)
    detector = MTCNN()
    caras = detector.detect_faces(pixeles)
    reg_rostro(img, caras)


# ------------------------Crearemos una funcion para asignar al boton registro --------------------------------
def registro():
    global usuario
    global contra  # Globalizamos las variables para usarlas en otras funciones
    global usuario_entrada
    global contra_entrada
    global pantalla1
    pantalla.withdraw()
    pantalla1 = Toplevel(pantalla)  # Esta pantalla es de un nivel superior a la principal
    pantalla1.title("REGISTRO")
    pantalla1.geometry("550x700")  # Asignamos el tamaño de la ventana
    Label(
        pantalla1,
        text="REGISTRO DE USUARIO",
        bg="#2267BD",
        fg="white",
        width="300",
        height="2",
        font=("Century Gothic", 16),
    ).pack()

    # --------- Empezaremos a crear las entradas ----------------------------------------

    usuario = StringVar()
    contra = StringVar()

    Label(pantalla1, text="").pack()
    Label(pantalla1, text="").pack()
    Label(pantalla1, text="").pack()
    Label(pantalla1, text="").pack()
    Label(
        pantalla1, text="Registro facial: debe de asignar un usuario", font=("Century Gothic", 12)
    ).pack()
    Label(
        pantalla1,
        text="Registro tradicional: debe asignar usuario y contraseña",
        font=("Century Gothic", 12),
    ).pack()
    Label(pantalla1, text="").pack()  # Dejamos un poco de espacio
    Label(
        pantalla1, text="Usuario * ", font=("Century Gothic", 12)
    ).pack()  # Mostramos en la pantalla 1 el usuario
    usuario_entrada = Entry(
        pantalla1, textvariable=usuario
    )  # Creamos un text variable para que el usuario ingrese la info
    usuario_entrada.pack()
    Label(pantalla1, text="").pack()
    Label(
        pantalla1, text="Contraseña * ", font=("Century Gothic", 12)
    ).pack()  # Mostramos en la pantalla 1 la contraseña
    contra_entrada = Entry(
        pantalla1, textvariable=contra, show="*"
    )  # Creamos un text variable para que el usuario ingrese la contra
    contra_entrada.pack()
    Label(pantalla1, text="").pack()  # Dejamos un espacio para la creacion del boton
    Label(pantalla1, text="").pack()
    Button(
        pantalla1,
        text="Registro",
        bg="#2267BD",
        fg="white",
        width="20",
        height="1",
        command=registrar_usuario,
        font=("Century Gothic", 12),
    ).pack()  # Creamos el boton

    # ------------ Vamos a crear el boton para hacer el registro facial --------------------
    Label(pantalla1, text="").pack()
    Button(
        pantalla1,
        text="Registro Facial",
        bg="#2267BD",
        fg="white",
        width="20",
        height="1",
        command=registro_facial,
        font=("Century Gothic", 12),
    ).pack()
    Label(pantalla1, text="").pack()
    Label(pantalla1, text="").pack()
    Label(pantalla1, text="").pack()
    Label(pantalla1, text="").pack()
    Label(pantalla1, text="").pack()
    Label(pantalla1, text="").pack()
    Label(pantalla1, text="").pack()
    Button(
        pantalla1,
        text="Volver",
        height="1",
        bg="#BA5649",
        fg="white",
        width="10",
        anchor="center",
        command=retroceder2,
        font=("Century Gothic", 12),
    ).pack()


# ------------------------------------------- Funcion para verificar los datos ingresados al login ------------------------------------


def verificacion_login():
    log_usuario = verificacion_usuario.get()
    log_contra = verificacion_contra.get()

    usuario_entrada2.delete(0, END)
    contra_entrada2.delete(0, END)

    lista_archivos = os.listdir()  # Vamos a importar la lista de archivos con la libreria os
    if log_usuario in lista_archivos:  # Comparamos los archivos con el que nos interesa
        archivo2 = open(log_usuario, "r")  # Abrimos el archivo en modo lectura
        verificacion = (
            archivo2.read().splitlines()
        )  # leera las lineas dentro del archivo ignorando el resto
        if log_contra in verificacion:
            print("Inicio de sesion exitoso")
            pantalla2.destroy()
            pantalla.destroy()
            ventana999 = Tk()
            ventana999.title("CORSPSYS")
            ventana999.minsize(height=475, width=795)
            ventana999.geometry("1000x500+180+80")
            ventana999.call(
                            "wm",
                            "iconphoto",
                            ventana999._w,
            PhotoImage(file=os.path.join(os.path.dirname(__file__), "logo2.png")),
            ),
            app999 = Ventana2(ventana999)
            app999.mainloop()

            # --------- Empezaremos a crear las entradas ----------------------------------------

        else:
            print("Contraseña incorrecta, ingrese de nuevo")
            # Label(pantalla2, text = "Contraseña Incorrecta", fg = "red", font = ("Calibri",11)).pack()
            global ventana3
            ventana3 = Toplevel()
            ventana3.geometry("350x250")
            ventana3.title("Inicio de Sesion")
            Label(ventana3, text="").pack()
            Label(ventana3, text="").pack()
            Label(ventana3, text="").pack()
            Label(
                ventana3, text="Contraseña incorrecta, ingrese de nuevo", font=("Century Gothic", 11)
            ).pack()
            Label(ventana3, text="").pack()
            Label(ventana3, text="").pack()
            Button(ventana3, text="Ok", width=15, height=1, bg="#BA5649",
            fg="white", command=contra_incorrecta).pack()
    else:
        print("Usuario no encontrado")
        # Label(pantalla2, text = "Usuario no encontrado", fg = "red", font = ("Calibri",11)).pack()
        global ventana4
        ventana4 = Toplevel()
        ventana4.geometry("300x200")
        ventana4.title("Inicio de Sesion")
        Label(ventana4, text="").pack()
        Label(ventana4, text="").pack()
        Label(ventana4, text="").pack()
        Label(
            ventana4, text="Usuario no encontrado, favor registrarse", font=("Century Gothic", 11)
        ).pack()
        Label(ventana4, text="").pack()
        Label(ventana4, text="").pack()
        Button(ventana4, text="Ok", width=15, height=1, bg="#BA5649",
        fg="white", command=usuario_no_encontrado).pack()


# --------------------------Funcion para el Login Facial --------------------------------------------------------
def login_facial():
    # ------------------------------Vamos a capturar el rostro-----------------------------------------------------
    cap = cv2.VideoCapture(0)  # Elegimos la camara con la que vamos a hacer la deteccion
    while True:
        ret, frame = cap.read()  # Leemos el video
        cv2.imshow("Login Facial", frame)  # Mostramos el video en pantalla
        if cv2.waitKey(1) == 27:  # Cuando oprimamos "Escape" rompe el video
            break
    usuario_login = (
        verificacion_usuario.get()
    )  # Con esta variable vamos a guardar la foto pero con otro nombre para no sobreescribir
    cv2.imwrite(
        usuario_login + "LOG.jpg", frame
    )  # Guardamos la ultima captura del video como imagen y asignamos el nombre del usuario
    cap.release()  # Cerramos
    cv2.destroyAllWindows()

    usuario_entrada2.delete(0, END)  # Limpiamos los text variables
    contra_entrada2.delete(0, END)

    # ----------------- Funcion para guardar el rostro --------------------------

    def log_rostro(img, lista_resultados):
        data = pyplot.imread(img)
        for i in range(len(lista_resultados)):
            x1, y1, ancho, alto = lista_resultados[i]["box"]
            x2, y2 = x1 + ancho, y1 + alto
            pyplot.subplot(1, len(lista_resultados), i + 1)
            pyplot.axis("off")
            cara_reg = data[y1:y2, x1:x2]
            cara_reg = cv2.resize(
                cara_reg, (150, 200), interpolation=cv2.INTER_CUBIC
            )  # Guardamos la imagen 150x200
            cv2.imwrite(usuario_login + "LOG.jpg", cara_reg)
            return pyplot.imshow(data[y1:y2, x1:x2])
        pyplot.show()

    # -------------------------- Detectamos el rostro-------------------------------------------------------

    img = usuario_login + "LOG.jpg"
    pixeles = pyplot.imread(img)
    detector = MTCNN()
    caras = detector.detect_faces(pixeles)
    log_rostro(img, caras)

    # -------------------------- Funcion para comparar los rostros --------------------------------------------
    def orb_sim(img1, img2):
        orb = cv2.ORB_create()  # Creamos el objeto de comparacion

        kpa, descr_a = orb.detectAndCompute(
            img1, None
        )  # Creamos descriptor 1 y extraemos puntos claves
        kpb, descr_b = orb.detectAndCompute(
            img2, None
        )  # Creamos descriptor 2 y extraemos puntos claves

        comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)  # Creamos comparador de fuerza

        matches = comp.match(descr_a, descr_b)  # Aplicamos el comparador a los descriptores

        regiones_similares = [
            i for i in matches if i.distance < 70
        ]  # Extraemos las regiones similares en base a los puntos claves
        if len(matches) == 0:
            return 0
        return len(regiones_similares) / len(matches)  # Exportamos el porcentaje de similitud

    # ---------------------------- Importamos las imagenes y llamamos la funcion de comparacion ---------------------------------

    im_archivos = os.listdir()  # Vamos a importar la lista de archivos con la libreria os
    if usuario_login + ".jpg" in im_archivos:  # Comparamos los archivos con el que nos interesa
        rostro_reg = cv2.imread(usuario_login + ".jpg", 0)  # Importamos el rostro del registro
        rostro_log = cv2.imread(
            usuario_login + "LOG.jpg", 0
        )  # Importamos el rostro del inicio de sesion
        similitud = orb_sim(rostro_reg, rostro_log)
        if similitud >= 0.80:
            print("Bienvenido al sistema, usuario: ", usuario_login)
            print("Compatibilidad con la foto del registro: ", similitud)
            pantalla2.destroy()
            pantalla.destroy()
            ventana999 = Tk()
            ventana999.title("CORSPSYS")
            ventana999.minsize(height=475, width=795)
            ventana999.geometry("1000x500+180+80")
            ventana999.call(
                            "wm",
                            "iconphoto",
                            ventana999._w,
            PhotoImage(file=os.path.join(os.path.dirname(__file__), "logo2.png")),
            ),
            app999 = Ventana2(ventana999)
            app999.mainloop()
        else:
            print("Rostro incorrecto, Verifique su usuario")
            print("Compatibilidad con la foto del registro: ", similitud)
            # Label(pantalla2, text = "Incompatibilidad de rostros", fg = "red", font = ("Calibri",11)).pack()
            global ventana5
            ventana5 = Toplevel()
            ventana5.geometry("300x250")
            ventana5.title("Inicio de Sesion Facial")
            Label(ventana5, text="").pack()
            Label(ventana5, text="").pack()
            Label(
                ventana5, text="Rostro incorrecto, verifique su usuario", font=("Century Gothic", 11)
            ).pack()
            Label(ventana5, text="").pack()
            Label(ventana5, text="").pack()
            Button(ventana5, text="Ok", width=15, height=1, bg="#BA5649",
            fg="white", command=rostro_incorrecto).pack()
    else:
        print("Usuario no encontrado")
        # Label(pantalla2, text = "Usuario no encontrado", fg = "red", font = ("Calibri",11)).pack()
        global ventana6
        ventana6 = Toplevel()
        ventana6.geometry("300x250")
        ventana6.title("Inicio de Sesion Facial")
        Label(ventana6, text="").pack()
        Label(ventana6, text="").pack()
        Label(
            ventana6, text="Usuario no encontrado, favor registrarse", font=("Century Gothic", 11)
        ).pack()
        Label(ventana6, text="").pack()
        Label(ventana6, text="").pack()
        Button(ventana6, text="Ok", width=15, height=1, bg="#BA5649",
        fg="white", command=rostro_no_encontrado).pack()


# ------------------------Funcion que asignaremos al boton login -------------------------------------------------


def login():
    global pantalla2
    global verificacion_usuario
    global verificacion_contra
    global usuario_entrada2
    global contra_entrada2
    pantalla.withdraw()
    pantalla2 = Toplevel(pantalla)
    pantalla2.title("LOGIN")
    pantalla2.geometry("550x700")  # Creamos la ventana
    Label(
        pantalla2,
        text="INICIO DE SESION",
        bg="#2267BD",
        fg="white",
        width="300",
        height="2",
        font=("Century Gothic", 16),
    ).pack()
    Label(pantalla2, text="").pack()  # Dejamos un poco de espacio
    Label(pantalla2, text="").pack()  # Dejamos un poco de espacio
    Label(pantalla2, text="").pack()  # Dejamos un poco de espacio
    Label(pantalla2, text="").pack()  # Dejamos un poco de espacio
    Label(
        pantalla2, text="Login facial: debe de asignar un usuario", font=("Century Gothic", 12)
    ).pack()
    Label(
        pantalla2,
        text="Login tradicional: debe asignar usuario y contraseña",
        font=("Century Gothic", 12),
    ).pack()
    Label(pantalla2, text="").pack()  # Dejamos un poco de espacio

    verificacion_usuario = StringVar()
    verificacion_contra = StringVar()

    # ---------------------------------- Ingresamos los datos --------------------------
    Label(pantalla2, text="Usuario * ", font=("Century Gothic", 12)).pack()
    usuario_entrada2 = Entry(pantalla2, textvariable=verificacion_usuario)
    usuario_entrada2.pack()
    Label(pantalla2, text="").pack()
    Label(pantalla2, text="Contraseña * ", font=("Century Gothic", 12)).pack()
    contra_entrada2 = Entry(pantalla2, textvariable=verificacion_contra, show="*")
    contra_entrada2.pack()
    Label(pantalla2, text="").pack()
    Label(pantalla2, text="").pack()
    Label(pantalla2, text="").pack()
    Button(
        pantalla2,
        text="Iniciar Sesion",
        bg="#2267BD",
        fg="white",
        width="20",
        height="1",
        command=verificacion_login,
        font=("Century Gothic", 12),
    ).pack()


    Label(pantalla2, text="").pack()
    Button(
        pantalla2,
        text="Inicio de Sesion Facial",
        bg="#2267BD",
        fg="white",
        width="20",
        height="1",
        command=login_facial,
        font=("Century Gothic", 12),
    ).pack()
    Label(pantalla2, text="").pack()
    Label(pantalla2, text="").pack()
    Label(pantalla2, text="").pack()
    Label(pantalla2, text="").pack()
    Label(pantalla2, text="").pack()
    Label(pantalla2, text="").pack()
    Label(pantalla2, text="").pack()
    Button(
        pantalla2,
        text="Volver",
        height="1",
        bg="#BA5649",
        fg="white",
        width="10",
        anchor="center",
        command=retroceder,
        font=("Century Gothic", 12),
    ).pack()
    Label(pantalla2, text="").pack()


# ------------------------- Funcion del boton de retroceso ------------------------------------------------


def retroceder():
    pantalla2.destroy()
    pantalla.deiconify()


def retroceder2():
    pantalla1.destroy()
    pantalla.deiconify()


def contra_incorrecta():
    ventana3.destroy()


def usuario_no_encontrado():
    ventana4.destroy()


def rostro_incorrecto():
    ventana5.destroy()


def rostro_no_encontrado():
    ventana6.destroy()


def registro_usuario():
    ventana8.destroy()



def cerrar_facial_2():
    ventana10.destroy()


# ------------------------- Funcion de nuestra pantalla principal ------------------------------------------------


def pantalla_principal():
    global pantalla  # Globalizamos la variable para usarla en otras funciones
    pantalla = Tk()
    pantalla.geometry("450x400")  # Asignamos el tamaño de la ventana
    pantalla.title("Control de Acceso Sistema Facial")  # Asignamos el titulo de la pantalla
    Label(
        text="Control de Acceso",
        bg="#2267BD",
        fg="white",
        width="300",
        height="2",
        font=("Century Gothic", 16),
    ).pack()  # Asignamos caracteristicas de la ventana

    # ------------------------- Vamos a Crear los Botones ------------------------------------------------------

    Label(text="").pack()  # Creamos el espacio entre el titulo y el primer boton
    Label(text="").pack()  # Creamos el espacio entre el titulo y el primer boton
    Label(text="").pack()  # Creamos el espacio entre el titulo y el primer boton
    Label(text="").pack()  # Creamos el espacio entre el titulo y el primer boton
    Button(
        text="Iniciar Sesion",
        height="2",
        width="30",
        anchor="center",
        command=login,
        background="#2267BD",
        fg="white",
        font=("Century Gothic", 14),
    ).pack()
    Label(text="").pack()  # Creamos el espacio entre el primer boton y el segundo boton
    Label(text="").pack()
    Button(
        text="Registro",
        height="2",
        width="30",
        anchor="center",
        command=registro,
        background="#2267BD",
        fg="white",
        font=("Century Gothic", 14),
    ).pack()
    Label(text="").pack()  # Creamos el espacio entre el primer boton y el segundo boton
    pantalla.mainloop()


# --------------------------------------------------------MENU DESPLEGABLE------------------------------------------------------
# ---------las librerias, conexion a base de datos, ya estan puestas, estan en la primera linea de codigo-----------------------


class Ventana2(Frame):
    def __init__(self, master, *args):
        super().__init__(master, *args)

        self.menu = True
        self.color = True
        self.cedula = StringVar()
        self.nombre = StringVar()
        self.apellido = StringVar()
        self.telefono = StringVar()
        self.direccion = StringVar()
        self.buscar = StringVar()
        self.buscar_actualiza = StringVar()
        self.id = StringVar()
        self.base_datos = Registro_datos()

        self.frame_inicio = Frame(self.master, bg="#E6ECED", width=50, height=45)
        self.frame_inicio.grid_propagate(0)
        self.frame_inicio.grid(column=0, row=0, sticky="nsew")
        self.frame_menu = Frame(self.master, bg="#E6ECED", width=50)
        self.frame_menu.grid_propagate(0)
        self.frame_menu.grid(column=0, row=1, sticky="nsew")
        self.frame_top = Frame(self.master, bg="#E6ECED", height=50)
        self.frame_top.grid(column=1, row=0, sticky="nsew")
        self.frame_principal = Frame(self.master, bg="#E6ECED")
        self.frame_principal.grid(column=1, row=1, sticky="nsew")
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.frame_principal.columnconfigure(0, weight=1)
        self.frame_principal.rowconfigure(0, weight=1)
        self.widgets()

    def pantalla_inicial(self):
        self.paginas.select([self.frame_uno])

    def pantalla_datos(self):
        self.paginas.select([self.frame_dos])
        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.columnconfigure(1, weight=1)
        self.frame_dos.rowconfigure(2, weight=1)
        self.frame_tabla_uno.columnconfigure(0, weight=1)
        self.frame_tabla_uno.rowconfigure(0, weight=1)

    def pantalla_escribir(self):
        self.paginas.select([self.frame_tres])
        self.frame_tres.columnconfigure(0, weight=1)
        self.frame_tres.columnconfigure(1, weight=1)

    def pantalla_actualizar(self):
        self.paginas.select([self.frame_cuatro])
        self.frame_cuatro.columnconfigure(0, weight=1)
        self.frame_cuatro.columnconfigure(1, weight=1)

    def pantalla_buscar(self):
        self.paginas.select([self.frame_cinco])
        self.frame_cinco.columnconfigure(0, weight=1)
        self.frame_cinco.columnconfigure(1, weight=1)
        self.frame_cinco.columnconfigure(2, weight=1)
        self.frame_cinco.rowconfigure(2, weight=1)
        self.frame_tabla_dos.columnconfigure(0, weight=1)
        self.frame_tabla_dos.rowconfigure(0, weight=1)

    def pantalla_ajustes(self):
        self.paginas.select([self.frame_seis])

    def menu_lateral(self):
        if self.menu is True:
            for i in range(50, 170, 10):
                self.frame_menu.config(width=i)
                self.frame_inicio.config(width=i)
                self.frame_menu.update()
                clik_inicio = self.bt_cerrar.grid_forget()
                if clik_inicio is None:
                    self.bt_inicio.grid(column=0, row=0, padx=10, pady=10)
                    self.bt_inicio.grid_propagate(0)
                    self.bt_inicio.config(width=i)
                    self.pantalla_inicial()
            self.menu = False
        else:
            for i in range(170, 50, -10):
                self.frame_menu.config(width=i)
                self.frame_inicio.config(width=i)
                self.frame_menu.update()
                clik_inicio = self.bt_inicio.grid_forget()
                if clik_inicio is None:
                    self.frame_menu.grid_propagate(0)
                    self.bt_cerrar.grid(column=0, row=0, padx=10, pady=10)
                    self.bt_cerrar.grid_propagate(0)
                    self.bt_cerrar.config(width=i)
                    self.pantalla_inicial()
            self.menu = True

    def cambiar_color(self):
        if self.color == True:
            self.bt_color["image"] = self.dia
            self.titulo.config(fg="deep sky blue")
            self.frame_seis.config(bg="black")
            self.text_ajustes.config(bg="black")
            self.texto.config(bg="black")
            self.bt_color.config(bg="black", activebackground="black")
            self.color = False
        else:
            self.bt_color["image"] = self.noche
            self.titulo.config(fg="DarkOrchid1")
            self.frame_seis.config(bg="white")
            self.text_ajustes.config(bg="white")
            self.texto.config(bg="white")
            self.bt_color.config(bg="white", activebackground="white")
            self.color = True

    def widgets(self):
        self.imagen_inicio = PhotoImage(file=os.path.join(os.path.dirname(__file__), "inicio.png"))
        self.imagen_menu = PhotoImage(file=os.path.join(os.path.dirname(__file__), "menu.png"))
        self.imagen_datos = PhotoImage(file=os.path.join(os.path.dirname(__file__), "datos.png"))
        self.imagen_registrar = PhotoImage(
            file=os.path.join(os.path.dirname(__file__), "escribir.png")
        )
        self.imagen_actualizar = PhotoImage(
            file=os.path.join(os.path.dirname(__file__), "actualizar.png")
        )
        self.imagen_buscar = PhotoImage(file=os.path.join(os.path.dirname(__file__), "buscar.png"))
        self.imagen_ajustes = PhotoImage(
            file=os.path.join(os.path.dirname(__file__), "configuracion.png")
        )

        self.logo = PhotoImage(file=os.path.join(os.path.dirname(__file__), "logo.png"))
        self.imagen_uno = PhotoImage(file=os.path.join(os.path.dirname(__file__), "imagen_uno.png"))
        self.imagen_dos = PhotoImage(file=os.path.join(os.path.dirname(__file__), "imagen_dos.png"))
        self.dia = PhotoImage(file=os.path.join(os.path.dirname(__file__), "dia.png"))
        self.noche = PhotoImage(file=os.path.join(os.path.dirname(__file__), "noche.png"))
        self.bt_inicio = Button(
            self.frame_inicio,
            image=self.imagen_inicio,
            bg="#E6ECED",
            activebackground="#E6ECED",
            bd=0,
            command=self.menu_lateral,
        )
        self.bt_inicio.grid(column=0, row=0, padx=5, pady=10)
        self.bt_cerrar = Button(
            self.frame_inicio,
            image=self.imagen_menu,
            bg="#E6ECED",
            activebackground="#E6ECED",
            bd=0,
            command=self.menu_lateral,
        )
        self.bt_cerrar.grid(column=0, row=0, padx=5, pady=10)
        # BOTONES Y ETIQUETAS DEL MENU LATERAL
        Button(
            self.frame_menu,
            image=self.imagen_datos,
            bg="#E6ECED",
            activebackground="#E6ECED",
            bd=0,
            command=self.pantalla_datos,
        ).grid(column=0, row=1, pady=20, padx=10)
        Button(
            self.frame_menu,
            image=self.imagen_registrar,
            bg="#E6ECED",
            activebackground="#E6ECED",
            bd=0,
            command=self.pantalla_escribir,
        ).grid(column=0, row=2, pady=20, padx=10)
        Button(
            self.frame_menu,
            image=self.imagen_actualizar,
            bg="#E6ECED",
            activebackground="#E6ECED",
            bd=0,
            command=self.pantalla_actualizar,
        ).grid(column=0, row=3, pady=20, padx=10)
        Button(
            self.frame_menu,
            image=self.imagen_buscar,
            bg="#E6ECED",
            activebackground="#E6ECED",
            bd=0,
            command=self.pantalla_buscar,
        ).grid(column=0, row=4, pady=20, padx=10)
        Button(
            self.frame_menu,
            image=self.imagen_ajustes,
            bg="#E6ECED",
            activebackground="#E6ECED",
            bd=0,
            command=self.pantalla_ajustes,
        ).grid(column=0, row=5, pady=20, padx=10)

        Label(
            self.frame_menu,
            text="Base Datos",
            bg="#E6ECED",
            fg="#2267BD",
            font=("Century Gothic", 12, "bold"),
        ).grid(column=1, row=1, pady=20, padx=2)
        Label(
            self.frame_menu,
            text="Registrar",
            bg="#E6ECED",
            fg="#2267BD",
            font=("Century Gothic", 12, "bold"),
        ).grid(column=1, row=2, pady=20, padx=2)
        Label(
            self.frame_menu,
            text=" Actualizar",
            bg="#E6ECED",
            fg="#2267BD",
            font=("Century Gothic", 12, "bold"),
        ).grid(column=1, row=3, pady=20, padx=2)
        Label(
            self.frame_menu,
            text="Eliminar",
            bg="#E6ECED",
            fg="#2267BD",
            font=("Century Gothic", 12, "bold"),
        ).grid(column=1, row=4, pady=20, padx=2)
        Label(
            self.frame_menu,
            text="Ajustes",
            bg="#E6ECED",
            fg="#2267BD",
            font=("Century Gothic", 12, "bold"),
        ).grid(column=1, row=5, pady=20, padx=2)

        #############################  CREAR  PAGINAS  ##############################
        estilo_paginas = ttk.Style()
        estilo_paginas.configure(
            "TNotebook", background="black", foreground="black", padding=0, borderwidth=0
        )
        estilo_paginas.theme_use("default")
        estilo_paginas.configure("TNotebook", background="black", borderwidth=0)
        estilo_paginas.configure("TNotebook.Tab", background="black", borderwidth=0)
        estilo_paginas.map("TNotebook", background=[("selected", "black")])
        estilo_paginas.map(
            "TNotebook.Tab", background=[("selected", "black")], foreground=[("selected", "black")]
        )

        # CREACCION DE LAS PAGINAS
        self.paginas = ttk.Notebook(
            self.frame_principal, style="TNotebook"
        )  # , style = 'TNotebook'
        self.paginas.grid(column=0, row=0, sticky="nsew")
        self.frame_uno = Frame(self.paginas, bg="#2267BD")
        self.frame_dos = Frame(self.paginas, bg="white")
        self.frame_tres = Frame(self.paginas, bg="white")
        self.frame_cuatro = Frame(self.paginas, bg="white")
        self.frame_cinco = Frame(self.paginas, bg="white")
        self.frame_seis = Frame(self.paginas, bg="white")
        self.paginas.add(self.frame_uno)
        self.paginas.add(self.frame_dos)
        self.paginas.add(self.frame_tres)
        self.paginas.add(self.frame_cuatro)
        self.paginas.add(self.frame_cinco)
        self.paginas.add(self.frame_seis)
        ##############################         PAGINAS       #############################################

        ######################## FRAME TITULO #################
        self.titulo = Label(
            self.frame_top,
            text="SISTEMA CORPSYS",
            bg="#E6ECED",
            fg="#2267BD",
            font=("Imprint MT Shadow", 15, "bold"),
        )
        self.titulo.pack(expand=1)
        ######################## VENTANA PRINCIPAL #################
        Label(
            self.frame_uno,
            text="DEMO",
            bg="#2267BD",
            fg="white",
            font=("Freehand521 BT", 20, "bold"),
        ).pack(expand=1)
        Label(self.frame_uno, image=self.logo, bg="#2267BD").pack(expand=1)

        ######################## MOSTRAR TODOS LOS PRODUCTOS DE LA BASE DE DATOS MYSQL #################
        Label(
            self.frame_dos,
            text="Datos de MySQL",
            bg="white",
            fg="#2267BD",
            font=("Century Gothic", 20, "bold"),
        ).grid(column=0, row=0)
        Button(
            self.frame_dos,
            text="ACTUALIZAR",
            fg="black",
            font=("Century Gothic", 11, "bold"),
            command=self.datos_totales,
            bg="#AEE683",
            bd=2,
            borderwidth=2,
        ).grid(column=1, row=0, pady=5)
        # ESTILO DE LAS TABLAS DE DATOS TREEVIEW
        estilo_tabla = ttk.Style()
        estilo_tabla.configure(
            "Treeview", font=("Century Gothic", 12, "bold"), foreground="black", background="white"
        )  # , fieldbackground='yellow'
        estilo_tabla.map(
            "Treeview", background=[("selected", "#2267BD")], foreground=[("selected", "black")]
        )
        estilo_tabla.configure(
            "Heading", background="white", foreground="navy", padding=3, font=("Century Gothic", 12, "bold")
        )
        estilo_tabla.configure("Item", foreground="white", focuscolor="#2267BD")
        estilo_tabla.configure(
            "TScrollbar",
            arrowcolor="#2267BD",
            bordercolor="#2267BD",
            troughcolor="#E6ECED",
            background="white",
        )
        # TABLA UNO
        self.frame_tabla_uno = Frame(self.frame_dos, bg="gray90")
        self.frame_tabla_uno.grid(columnspan=3, row=2, sticky="nsew")
        self.tabla_uno = ttk.Treeview(self.frame_tabla_uno)
        self.tabla_uno.grid(column=0, row=0, sticky="nsew")
        ladox = ttk.Scrollbar(
            self.frame_tabla_uno, orient="horizontal", command=self.tabla_uno.xview
        )
        ladox.grid(column=0, row=1, sticky="ew")
        ladoy = ttk.Scrollbar(self.frame_tabla_uno, orient="vertical", command=self.tabla_uno.yview)
        ladoy.grid(column=1, row=0, sticky="ns")

        self.tabla_uno.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)
        self.tabla_uno["columns"] = ("Nombre", "Apellido", "Telefono", "Direccion")
        self.tabla_uno.column("#0", minwidth=100, width=120, anchor="center")
        self.tabla_uno.column("Nombre", minwidth=100, width=130, anchor="center")
        self.tabla_uno.column("Apellido", minwidth=100, width=120, anchor="center")
        self.tabla_uno.column("Telefono", minwidth=100, width=120, anchor="center")
        self.tabla_uno.column("Direccion", minwidth=100, width=105, anchor="center")

        self.tabla_uno.heading("#0", text="Cedula", anchor="center")
        self.tabla_uno.heading("Nombre", text="Nombre", anchor="center")
        self.tabla_uno.heading("Apellido", text="Apellido", anchor="center")
        self.tabla_uno.heading("Telefono", text="Telefono", anchor="center")
        self.tabla_uno.heading("Direccion", text="Direccion", anchor="center")
        self.tabla_uno.bind("<<TreeviewSelect>>", self.obtener_fila)

        ######################## REGISTRAR  NUEVOS PRODUCTOS #################
        Label(
            self.frame_tres,
            text="Agregar Nuevos Datos",
            fg="#2267BD",
            bg="white",
            font=("Century Gothic", 20, "bold"),
        ).grid(columnspan=2, column=0, row=0, pady=5)
        Label(
            self.frame_tres, text="Cedula", fg="navy", bg="white", font=("Rockwell", 13, "bold")
        ).grid(column=0, row=1, pady=15, padx=5)
        Label(
            self.frame_tres, text="Nombre", fg="navy", bg="white", font=("Rockwell", 13, "bold")
        ).grid(column=0, row=2, pady=15)
        Label(
            self.frame_tres, text="Apellido", fg="navy", bg="white", font=("Rockwell", 13, "bold")
        ).grid(column=0, row=3, pady=15)
        Label(
            self.frame_tres, text="Telefono", fg="navy", bg="white", font=("Rockwell", 13, "bold")
        ).grid(column=0, row=4, pady=15)
        Label(
            self.frame_tres, text="Direccion", fg="navy", bg="white", font=("Rockwell", 13, "bold")
        ).grid(
            column=0, row=5, pady=15
        )  ##E65561

        Entry(
            self.frame_tres,
            textvariable=self.cedula,
            font=("Century Gothic", 12),
            highlightbackground="#2267BD",
            highlightcolor="green2",
            highlightthickness=5,
        ).grid(column=1, row=1)
        Entry(
            self.frame_tres,
            textvariable=self.nombre,
            font=("Century Gothic", 12),
            highlightbackground="#2267BD",
            highlightcolor="green2",
            highlightthickness=5,
        ).grid(column=1, row=2)
        Entry(
            self.frame_tres,
            textvariable=self.apellido,
            font=("Century Gothic", 12),
            highlightbackground="#2267BD",
            highlightcolor="green2",
            highlightthickness=5,
        ).grid(column=1, row=3)
        Entry(
            self.frame_tres,
            textvariable=self.telefono,
            font=("Century Gothic", 12),
            highlightbackground="#2267BD",
            highlightcolor="green2",
            highlightthickness=5,
        ).grid(column=1, row=4)
        Entry(
            self.frame_tres,
            textvariable=self.direccion,
            font=("Century Gothic", 12),
            highlightbackground="#2267BD",
            highlightcolor="green2",
            highlightthickness=5,
        ).grid(column=1, row=5)

        Button(
            self.frame_tres,
            command=self.agregar_datos,
            text="REGISTRAR",
            font=("Century Gothic", 11, "bold"),
            bg="#AEE683",
        ).grid(column=3, row=6, pady=10, padx=4)
        Label(self.frame_tres, image=self.imagen_uno, bg="white").grid(
            column=3, rowspan=5, row=0, padx=50
        )
        self.aviso_guardado = Label(
            self.frame_tres, bg="white", font=("Comic Sans MS", 12), fg="black"
        )
        self.aviso_guardado.grid(columnspan=2, column=0, row=6, padx=5)

        ########################   ACTUALIZAR LOS PRODUCTOS REGISTRADOS     #################
        Label(
            self.frame_cuatro,
            text="Actualizar Datos",
            fg="#2267BD",
            bg="white",
            font=("Century Gothic", 20, "bold"),
        ).grid(columnspan=4, row=0)
        Label(
            self.frame_cuatro,
            text="Ingrese el nombre del producto a actualizar",
            fg="black",
            bg="white",
            font=("Century Gothic", 12),
        ).grid(columnspan=2, row=1)
        Entry(
            self.frame_cuatro,
            textvariable=self.buscar_actualiza,
            font=("Century Gothic", 12),
            highlightbackground="#2267BD",
            width=12,
            highlightthickness=5,
        ).grid(column=2, row=1, padx=5)
        Button(
            self.frame_cuatro,
            command=self.actualizar_datos,
            text="BUSCAR",
            font=("Century Gothic", 11, "bold"),
            bg="#AEE683",
        ).grid(column=3, row=1, pady=5, padx=15)
        self.aviso_actualizado = Label(
            self.frame_cuatro, fg="black", bg="white", font=("Century Gothic", 12, "bold")
        )
        self.aviso_actualizado.grid(columnspan=2, row=7, pady=10, padx=5)

        Label(
            self.frame_cuatro, text="Cedula", fg="navy", bg="white", font=("Century Gothic", 13, "bold")
        ).grid(column=0, row=2, pady=15, padx=10)
        Label(
            self.frame_cuatro, text="Nombre", fg="navy", bg="white", font=("Century Gothic", 13, "bold")
        ).grid(column=0, row=3, pady=15)
        Label(
            self.frame_cuatro, text="Apellido", fg="navy", bg="white", font=("Century Gothic", 13, "bold")
        ).grid(column=0, row=4, pady=15)
        Label(
            self.frame_cuatro, text="Telefono", fg="navy", bg="white", font=("Century Gothic", 13, "bold")
        ).grid(column=0, row=5, pady=15)
        Label(
            self.frame_cuatro, text="Direccion", fg="navy", bg="white", font=("Century Gothic", 13, "bold")
        ).grid(
            column=0, row=6, pady=15
        )  ##E65561

        Entry(
            self.frame_cuatro,
            textvariable=self.cedula,
            font=("Century Gothic", 12),
            highlightbackground="#2267BD",
            highlightcolor="green",
            highlightthickness=5,
        ).grid(column=1, row=2)
        Entry(
            self.frame_cuatro,
            textvariable=self.nombre,
            font=("Century Gothic", 12),
            highlightbackground="#2267BD",
            highlightcolor="green",
            highlightthickness=5,
        ).grid(column=1, row=3)
        Entry(
            self.frame_cuatro,
            textvariable=self.apellido,
            font=("Century Gothic", 12),
            highlightbackground="#2267BD",
            highlightcolor="green",
            highlightthickness=5,
        ).grid(column=1, row=4)
        Entry(
            self.frame_cuatro,
            textvariable=self.telefono,
            font=("Century Gothic", 12),
            highlightbackground="#2267BD",
            highlightcolor="green",
            highlightthickness=5,
        ).grid(column=1, row=5)
        Entry(
            self.frame_cuatro,
            textvariable=self.direccion,
            font=("Century Gothic", 12),
            highlightbackground="#2267BD",
            highlightcolor="green",
            highlightthickness=5,
        ).grid(column=1, row=6)

        Button(
            self.frame_cuatro,
            command=self.actualizar_tabla,
            text="ACTUALIZAR",
            font=("#2267BD", 11, "bold"),
            bg="#AEE683",
        ).grid(column=2, columnspan=2, row=7, pady=2)
        Label(self.frame_cuatro, image=self.imagen_dos, bg="white").grid(
            column=2, columnspan=2, rowspan=5, row=1, padx=2
        )

        ######################## BUSCAR y ELIMINAR DATOS #################
        Label(
            self.frame_cinco,
            text="Buscar y Eliminar Datos",
            fg="#2267BD",
            bg="white",
            font=("Century Gothic", 24, "bold"),
        ).grid(columnspan=4, row=0, sticky="nsew", padx=2)
        Entry(
            self.frame_cinco,
            textvariable=self.buscar,
            font=("Century Gothic", 12),
            highlightbackground="#2267BD",
            highlightcolor="#2267BD",
            highlightthickness=5,
        ).grid(column=0, row=1, sticky="nsew", padx=2)
        Button(
            self.frame_cinco,
            command=self.buscar_nombre,
            text="BUSCAR POR NOMBRE",
            font=("Century Gothic", 8, "bold"),
            bg="#AEE683",
        ).grid(column=1, row=1, sticky="nsew", padx=2)
        Button(
            self.frame_cinco,
            command=self.eliminar_fila,
            text="ELIMINAR",
            font=("Century Gothic", 8, "bold"),
            bg="#BA5649",
        ).grid(column=2, row=1, sticky="nsew", padx=2)
        self.indica_busqueda = Label(
            self.frame_cinco, width=15, text="", fg="purple", bg="white", font=("Century Gothic", 12, "bold")
        )
        self.indica_busqueda.grid(column=3, row=1, padx=2)

        # TABLA DOS
        self.frame_tabla_dos = Frame(self.frame_cinco, bg="gray90")
        self.frame_tabla_dos.grid(columnspan=4, row=2, sticky="nsew")
        self.tabla_dos = ttk.Treeview(self.frame_tabla_dos)
        self.tabla_dos.grid(column=0, row=0, sticky="nsew")
        ladox = ttk.Scrollbar(
            self.frame_tabla_dos, orient="horizontal", command=self.tabla_dos.xview
        )
        ladox.grid(column=0, row=1, sticky="ew")
        ladoy = ttk.Scrollbar(self.frame_tabla_dos, orient="vertical", command=self.tabla_dos.yview)
        ladoy.grid(column=1, row=0, sticky="ns")

        self.tabla_dos.configure(
            xscrollcommand=ladox.set,
            yscrollcommand=ladoy.set,
        )
        self.tabla_dos["columns"] = ("Nombre", "Apellido", "Telefono", "Direccion")
        self.tabla_dos.column("#0", minwidth=100, width=120, anchor="center")
        self.tabla_dos.column("Nombre", minwidth=100, width=130, anchor="center")
        self.tabla_dos.column("Apellido", minwidth=100, width=120, anchor="center")
        self.tabla_dos.column("Telefono", minwidth=100, width=120, anchor="center")
        self.tabla_dos.column("Direccion", minwidth=100, width=105, anchor="center")
        self.tabla_dos.heading("#0", text="Cedula", anchor="center")
        self.tabla_dos.heading("Nombre", text="Nombre", anchor="center")
        self.tabla_dos.heading("Apellido", text="Apellido", anchor="center")
        self.tabla_dos.heading("Telefono", text="Telefono", anchor="center")
        self.tabla_dos.heading("Direccion", text="Direccion", anchor="center")
        self.tabla_dos.bind("<<TreeviewSelect>>", self.obtener_fila)
        ######################## AJUSTES #################
        self.text_ajustes = Label(
            self.frame_seis,
            text="Configuracion",
            fg="#2267BD",
            bg="white",
            font=("Century Gothic", 20, "bold"),
        )
        self.text_ajustes.pack(expand=1)
        self.bt_color = Button(
            self.frame_seis,
            image=self.noche,
            command=self.cambiar_color,
            bg="white",
            bd=0,
            activebackground="white",
        )
        self.bt_color.pack(expand=1)
        self.texto = Label(self.frame_seis, bg="white", font=("Kaufmann BT", 18))
        self.texto.pack(expand=1)

       

    def datos_totales(self):
        datos = self.base_datos.mostrar_productos()
        self.tabla_uno.delete(*self.tabla_uno.get_children())
        i = -1
        for dato in datos:
            i = i + 1
            self.tabla_uno.insert("", i, text=datos[i][1:2], values=datos[i][2:6])

    def agregar_datos(self):
        cedula = self.cedula.get()
        nombre = self.nombre.get()
        apellido = self.apellido.get()
        telefono = self.telefono.get()
        direccion = self.direccion.get()
        datos = (nombre, apellido, telefono, direccion)
        if cedula and nombre and apellido and telefono and direccion != "":
            self.tabla_uno.insert("", 0, text=cedula, values=datos)
            self.base_datos.inserta_producto(cedula, nombre, apellido, telefono, direccion)
            self.aviso_guardado["text"] = "Datos Guardados"
            self.limpiar_datos()
            self.aviso_guardado.update()
            time.sleep(1)
            self.aviso_guardado["text"] = ""
        else:
            self.aviso_guardado["text"] = "Ingrese todos los datos"
            self.aviso_guardado.update()
            time.sleep(1)
            self.aviso_guardado["text"] = ""

    def actualizar_datos(self):
        dato = self.buscar_actualiza.get()
        dato = str("'" + dato + "'")
        nombre_buscado = self.base_datos.busca_producto(dato)
        if nombre_buscado == []:
            self.aviso_actualizado["text"] = "No existe"
            self.indica_busqueda.update()
            time.sleep(1)
            self.limpiar_datos()
            self.aviso_actualizado["text"] = ""
        else:
            i = -1
            for dato in nombre_buscado:
                i = i + 1
                self.id.set(nombre_buscado[i][0])
                self.cedula.set(nombre_buscado[i][1])
                self.nombre.set(nombre_buscado[i][2])
                self.apellido.set(nombre_buscado[i][3])
                self.telefono.set(nombre_buscado[i][4])
                self.direccion.set(nombre_buscado[i][5])

    def actualizar_tabla(self):
        Id = self.id.get()
        cedula = self.cedula.get()
        nombre = self.nombre.get()
        apellido = self.apellido.get()
        telefono = self.telefono.get()
        direccion = self.direccion.get()
        self.base_datos.actualiza_productos(Id, cedula, nombre, apellido, telefono, direccion)
        self.aviso_actualizado["text"] = "Datos Actualizados"
        self.indica_busqueda.update()
        time.sleep(1)
        self.aviso_actualizado["text"] = ""
        self.limpiar_datos()
        self.buscar_actualiza.set("")

    def limpiar_datos(self):
        self.cedula.set("")
        self.nombre.set("")
        self.apellido.set("")
        self.telefono.set("")
        self.direccion.set("")

    def buscar_nombre(self):
        nombre_producto = self.buscar.get()
        nombre_producto = str("'" + nombre_producto + "'")
        nombre_buscado = self.base_datos.busca_producto(nombre_producto)
        if nombre_buscado == []:
            self.indica_busqueda["text"] = "No existe"
            self.indica_busqueda.update()
            time.sleep(1)
            self.indica_busqueda["text"] = ""
        i = -1
        for dato in nombre_buscado:
            i = i + 1
            self.tabla_dos.insert("", i, text=nombre_buscado[i][1:2], values=nombre_buscado[i][2:6])

    def eliminar_fila(self):
        fila = self.tabla_dos.selection()
        if len(fila) != 0:
            self.tabla_dos.delete(fila)
            nombre = "'" + str(self.nombre_borrar) + "'"
            self.base_datos.elimina_productos(nombre)
            self.indica_busqueda["text"] = "Eliminado"
            self.indica_busqueda.update()
            self.tabla_dos.delete(*self.tabla_dos.get_children())
            time.sleep(1)
            self.indica_busqueda["text"] = ""
            self.limpiar_datos()
        else:
            self.indica_busqueda["text"] = "No se Elimino"
            self.indica_busqueda.update()
            self.tabla_dos.delete(*self.tabla_dos.get_children())
            time.sleep(1)
            self.indica_busqueda["text"] = ""
            self.buscar.set("")
            self.limpiar_datos()

    def obtener_fila(self, event):
        current_item = self.tabla_dos.focus()
        if not current_item:
            return
        data = self.tabla_dos.item(current_item)
        self.nombre_borrar = data["values"][0]


def start_app1():
    ventana999 = Tk()
    ventana999.title("CORSYS")
    ventana999.minsize(height=475, width=795)
    ventana999.geometry("1000x500+180+80")
    ventana999.call(
        "wm",
        "iconphoto",
        ventana999._w,
        PhotoImage(file=os.path.join(os.path.dirname(__file__), "logo2.png")),
    )
    app = Ventana2(ventana999)
    app.mainloop()

if __name__ == "__main__":
    pantalla_principal()
