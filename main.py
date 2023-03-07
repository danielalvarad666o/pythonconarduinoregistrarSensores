from Menu import Menus
import enviardatos
from Sensores import sensor

from InterfaseSensor import interface


elsensor = sensor.Sensor()
elmenu = Menus.interfasMenu()




option = 0


while option != 6:
    
    option = elmenu.MostrarMenu()

    if option == 1:
        try:
         interface.AgregarSensor()
        except:
            print("opcion no valida")
    elif option == 2:
        try:
         interface.editaUbicacion()
        except:
            print("opcion no valida")
            
    elif option == 3:
        try:
         interface.editarDescription()
        except:
            print("opcion no valida")
    elif option == 4:
        try:
         interface.Versesnores()
        except:
            print("opcion no valida")
    elif option == 5:
        try:
         enviardatos.monitorear_sensores()
        except:
            print("opcion no valida")

    

# #------------------------------------------------------------------------------------------------------------------------------------------
