import os


class Decoradores:
    def alta_decorador(funcion):
        def Envoltura(*args, **kwargs):
            try:
                reg_dir = os.path.dirname(os.path.abspath(__file__))
                log_path = os.path.join(reg_dir)
                if Envoltura:
                    log_path = os.path.join(reg_dir, "registro_alta.txt")
                    with open(log_path, "a", encoding="utf-8") as archivo_registro:
                        archivo_registro.write(
                            f"Nuevo ingreso registrado: {args[1].get()} con la función {funcion.__name__}\n"
                        )
                else:
                    print("Hubo un error")
            except Exception as e:
                print(f"Hubo un error ejecutando {funcion.__name__}: {str(e)}\n")
            return funcion(*args, **kwargs)

        return Envoltura

    def baja_decorador(funcion):
        def Envoltura(*args, **kwargs):
            try:
                reg_dir = os.path.dirname(os.path.abspath(__file__))
                log_path = os.path.join(reg_dir)
                if Envoltura:
                    log_path = os.path.join(reg_dir, "registro_baja.txt")
                    with open(log_path, "a", encoding="utf-8") as archivo_registro:
                        archivo_registro.write(
                            f"Se borro nuevo dato con la función {funcion.__name__}\n"
                        )
            except Exception as e:
                print(f"Hubo un error ejecutando {funcion.__name__}: {str(e)}\n")
            return funcion(*args, **kwargs)

        return Envoltura

    def modificar_decorador(funcion):
        def Envoltura(*args, **kwargs):
            try:
                reg_dir = os.path.dirname(os.path.abspath(__file__))
                log_path = os.path.join(reg_dir)

                if Envoltura:
                    log_path = os.path.join(reg_dir, "modificar_tarea.txt")
                    with open(log_path, "a") as archivo_registro:
                        archivo_registro.write(
                            f"Nueva modificacion realizada con la función {funcion.__name__}\n"
                        )
            except Exception as e:
                print(f"Hubo un error ejecutando {funcion.__name__}: {str(e)}\n")
                return funcion(*args, *kwargs)

        return Envoltura
