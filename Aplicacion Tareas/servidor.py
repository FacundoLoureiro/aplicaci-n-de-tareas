import socket
import os
import threading


class Servidor:
    def __init__(
        self,
    ):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.puerto = 456
        self.serversocket.bind((self.host, self.puerto))
        self.serversocket.listen(3)
        self.reg_servidor = os.path.dirname(os.path.abspath(__file__))
        self.log_path = os.path.join(self.reg_servidor, "registro_servidor.txt")

    def registrar_log(self, registros_servidor):
        if not registros_servidor:
            log_path = os.path.join(self.reg_servidor, "registro_servidor.txt")
            with open(log_path, "a", encoding="utf-8") as archivo_registro:
                archivo_registro.write(f"Nuevo ingreso registrado")

    def manejar_cliente(self, clientesocket, address):
        print("Recibo la conexión desde: " + str(address[0]))
        mensaje = b"Hola, bienvenido a nuestro servidor\r\n"
        clientesocket.send(mensaje)
        clientesocket.close()

    def conectar_servidor(
        self,
    ):
        while True:
            clientesocket, address = self.serversocket.accept()
            threading.Thread(
                target=self.manejar_cliente, args=(clientesocket, address)
            ).start()


if __name__ == "__main__":
    obj_servidor = Servidor()
    obj_servidor.conectar_servidor()
