
class Login:

    def initial_session(self):
        try:
            print("Iniciando sesión ...")
            print("... Procesando ...")
            for i in range (0,10):
                print(f"Procesando: {i}")                
        except Exception as e:
            print(e)

    def close_session(self):
        try:
            print("Cerrando sesión ...")
        except Exception as e:
            print(e)            

Login().initial_session()
Login().close_session()