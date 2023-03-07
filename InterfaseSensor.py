from informaciondelsensor import infodelsensor
from Serial import serialclase
import time


elsensor=infodelsensor.SensorINFO()







class interface():
  
      
        
        
        

  def AgregarSensor():
    ser= serialclase.SensorData()
    
  
   
    print("Bienvenido :D ---------------------------------------------------\n")
    bools = int(input("Cuantos sensores tienes? "))
    print()
   
    print("Detectando Sensores ..........")
    time.sleep(5)
   
    sensor_detectado = False  # variable de bandera para verificar si se detectó al menos un sensor
   
    for i in range(1, bools+1):
       line=ser.read_sensor_data()
       
      
       
      
       if not line:  # si no se detecta ningún sensor, establecer la variable de bandera en False
           sensor_detectado = False
           print(f"Sensor {i} no detectado")
           break
      
       sensor_detectado = True  # si se detecta al menos un sensor, establecer la variable de bandera en True
    
       elsensor.add_sensor(line)
       print("")
      
       if i == bools:
          print("TODOS LOS SENSORES ESTAN REGISTRADOS PARA VERLO VE AL MENU")
          break
   
       if not sensor_detectado:  # si no se detecta ningún sensor, mostrar mensaje apropiado
        print("Nuevo sensor no detectado")


     
 
      
      
   
     
     
  def editaUbicacion():
   elsensor.cargar_json()
  
   print()
   print("Hola bienvenido a la editacion de tu sensor en cuestion de Ubicacion")
   elsensor.cambiar_ubicacion()
  
  def editarDescription():
   elsensor.cargar_json()
   print()
   print("Hola bienvenido a la editacion de tu sensor en cuestion de Description")
   elsensor.cambiar_descripcion()

  def Versesnores():
    elsensor.cargar_json()
    print("-------------------------TABLA--------------------------------------------------------------------------------------")
    print()
    numero=len(elsensor.lista)
    for sensor in elsensor.lista:
        print("--------------------------------Sensores--------------------------------------")
        print("|| ID: ",format(sensor["id"])+"\t ||Nombre: "+format(sensor["nombre"])+"\t ||Tipo : "+format(sensor["tipo"])+"\t ||Ubicacion : $"+format(sensor["ubicacion"])+"\t|| Description: ",format(sensor["descripcion"])+"\t || Fecha: ",format(sensor["fecha"]))
        print()
        print()
    print("TOTAL DE SENSORES REGISTRADOS: ",numero)
    print()
    
    
    

  
     
  
      