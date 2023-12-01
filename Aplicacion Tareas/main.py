from tkinter import Tk
import observador
import vista


class controlador_1:
    def __init__(self, master):
        self.controlador_master = master
        self.objeto_vista = vista.Window(self.controlador_master)
        self.obsrvadorA = observador.ConcreteObservadorA(
            self.objeto_vista.objeto_proyecto
        )


if __name__ == "__main__":
    master_tk = Tk()
    proyecto_vista = controlador_1(master_tk)
    proyecto_vista.objeto_vista.actualizar()
    master_tk.mainloop()
