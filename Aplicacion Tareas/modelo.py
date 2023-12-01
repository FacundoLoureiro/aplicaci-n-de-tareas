import sqlite3
import re
from peewee import *
from decoradores import Decoradores
from observador import Participante


db = SqliteDatabase("mis_tareas.db")


class BaseModel(Model):
    class Meta:
        database = db


class Tareas(BaseModel):
    tarea = CharField()
    hora = CharField()


try:
    db.connect()
    db.create_tables([Tareas])
except Exception as e:
    print(f"Error: {e}")


class Proyecto(Participante):
    def __init__(
        self,
    ):
        pass

    @Decoradores.alta_decorador
    def alta(self, tarea, hora, tree):
        cadena = tarea.get()
        patron = "^[A-aZ-z]+(?i:[ _-]+)*$"
        if re.match(patron, cadena):
            proyecto = Tareas()
            proyecto.tarea = tarea.get()
            proyecto.hora = hora.get()
            proyecto.save()
            self.actualizar_treeview(tree)
            self.notificar(tarea.get(), hora.get())

    @Decoradores.baja_decorador
    def borrar(self, tree):
        item_seleccionado = tree.focus()
        valor_id = tree.item(item_seleccionado)
        borrar = Tareas.get(Tareas.id == valor_id["text"])
        borrar.delete_instance()

        self.actualizar_treeview(tree)

    @Decoradores.modificar_decorador
    def modificar(self, tarea, hora, tree):
        item_seleccionado = tree.focus()
        valor_id = tree.item(item_seleccionado)
        actualizar = Tareas.update(tarea=tarea.get(), hora=hora.get()).where(
            Tareas.id == valor_id["text"]
        )
        actualizar.execute()
        self.actualizar_treeview(tree)

    def actualizar_treeview(self, mitreview):
        self.records = mitreview.get_children()
        for element in self.records:
            mitreview.delete(element)
        for fila in Tareas.select():
            mitreview.insert("", 0, text=fila.id, values=(fila.tarea, fila.hora))
