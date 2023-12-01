import random
from tkinter import StringVar
from tkinter import DoubleVar
from tkinter import Label
from tkinter import Entry
from tkinter import ttk
from tkinter import Button
from tkinter import Radiobutton
from modelo import Proyecto


class Window:
    def __init__(self, ventana):
        self.master = ventana
        self.objeto_proyecto = Proyecto()
        self.tree = ttk.Treeview(self.master)
        self.master.title("Proyecto UTN")
        self.master.configure(bg="Lavender")
        self.titulo = Label(
            self.master,
            text="Ingrese su tarea diaria",
            bg="LightSteelBlue",
            fg="black",
            height=1,
            width=50,
        )
        self.titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky="ew")

        self.tarea = Label(self.master, text="Tarea", bg="Lavender")
        self.tarea.grid(row=1, column=1, sticky="ew")
        self.hora = Label(self.master, text="Hora", bg="Lavender")
        self.hora.grid(row=3, column=1, sticky="ew")

        self.valor_t = StringVar()
        self.valor_h = DoubleVar()
        self.w_ancho = 25

        self.entrada_tarea = Entry(
            self.master,
            textvariable=self.valor_t,
            width=self.w_ancho,
        )
        self.entrada_tarea.grid(row=2, column=1)

        self.entrada_hora = Entry(
            self.master, textvariable=self.valor_h, width=self.w_ancho
        )
        self.entrada_hora.grid(row=4, column=1)

        ######### TREEVIEW #########

        self.tree["columns"] = ("col1", "col2")
        self.tree.column("#0", width=90, minwidth=50, anchor="w")
        self.tree.column("col1", width=200, minwidth=80)
        self.tree.column("col2", width=200, minwidth=80)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Tarea")
        self.tree.heading("col2", text="Hora")
        self.tree.grid(row=10, column=0, columnspan=4)

        ######### BOTONES #########
        self.alta_boton = Button(
            self.master,
            text="Guardar",
            command=lambda: self.objeto_proyecto.alta(
                self.valor_t, self.valor_h, self.tree
            ),
            height=1,
            width=6,
        )
        self.alta_boton.grid(row=6, column=1, padx=5, pady=5)

        self.borrar_boton = Button(
            self.master,
            text="Borrar",
            command=lambda: self.objeto_proyecto.borrar(self.tree),
            height=1,
            width=6,
        )
        self.borrar_boton.grid(row=8, column=1, padx=5, pady=5)

        self.modificar_boton = Button(
            self.master,
            text="Modificar",
            command=lambda: self.objeto_proyecto.modificar(
                self.valor_t, self.valor_h, self.tree
            ),
        )
        self.modificar_boton.grid(row=7, column=1, padx=5, pady=5)

        dia_noche_boton = Radiobutton(
            self.master, text="Dia-Noche", command=self.dia_noche, value=1
        )
        dia_noche_boton.grid(row=3, column=2, padx=5, pady=5)

    def dia_noche(
        self,
    ):
        colores = ["Lavender", "Black"]
        color = random.choice(colores)
        self.master.configure(background=color)

    def actualizar(
        self,
    ):
        self.objeto_proyecto.actualizar_treeview(self.tree)
