import socket


class Cliente:
    def __init__(
        self,
    ):
        self.clientesocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "192.168.1.22"
        self.puerto = 456
        self.clientesocket.connect((self.host, self.puerto))

    def conectar_cliente(
        self,
    ):
        try:
            mensaje = self.clientesocket.recv(1024)
            print(mensaje.decode("ascii"))
        except Exception as e:
            print(f"Error en la conexion: {e}")
        finally:
            self.clientesocket.close()


if __name__ == "__main__":
    obj_cliente = Cliente()
    obj_cliente.conectar_cliente()
