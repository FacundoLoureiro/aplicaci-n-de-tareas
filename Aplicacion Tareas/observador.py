class Participante:
    Participantes = []

    def agregar(self, obj):
        self.Participantes.append(obj)

    def notificar(self, *args):
        for participante in self.Participantes:
            participante.update(args)


class Observador:
    def update(
        self,
    ):
        raise NotImplementedError("Actualizacion")


class ConcreteObservadorA(Observador):
    def __init__(self, obj):
        self.observador_a = obj
        self.observador_a.agregar(self)

    def update(self, *args):
        print("Patron observador capto los siguientes parametros :", args)
