class interfasMenu:
    
    def MostrarMenu(self):
        print("")
        print("[Seleccion]"+"-----------------------"*10)
        print("1)Agregar un sensor")
        print("2)Editar Ubicacion de un sensor")
        print("3)Editar Description de un sensor")
        print("4)Ver Sensores")
        print("5)Enviar datos")
        print("6)salir")
        option=int(input("Escoge una opcion: "))
        print("")
        return option
        