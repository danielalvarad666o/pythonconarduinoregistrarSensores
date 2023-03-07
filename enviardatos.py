import os
import json
from Serial import serialclase
import time
from datetime import datetime
from Mongoclass import mongo
from Sensores import sensor



def monitorear_sensores():
    serial_port = serialclase.SensorData()
    # Inicializar cliente de MongoDB
    client = mongo.MongoDBClient("mongodb+srv://root:2tCVgy$_DEa!ZYB@5b.y2llyqd.mongodb.net/test")
    elsensor = sensor.Sensor()
    last_sensor_check_time = time.time()
    sensor_connection = client.connect()
    temp_data = []
    
    while True:
        # Leer datos del puerto serial usando el método de la clase SensorData
        line = serial_port.read_sensor_data()

        # Procesar los datos del sensor
        elsensor.Crearsensor(line)

        if sensor_connection:
            current_time = time.time()

            if current_time - last_sensor_check_time >= 15:
                last_sensor_check_time = current_time

                if elsensor.lista:
                    # Agregar los datos a la base de datos
                    elsensor.agregarproducto(elsensor.lista, "sensores")
                    client.update_all_documents("Arduino", "Sensores", elsensor.datosdeljson1("sensores"))

                    # Limpiar la lista
                    elsensor.lista.clear()
                    
                    # Eliminar archivo de sensores cada 15 segundos
                    if os.path.exists("sensores.json"):
                        os.remove("sensores.json")
                        print("Archivo sensores.json eliminado")

        else:
            # Guardar los datos en un archivo temporal
            elsensor.agregarproducto(elsensor.lista, "temp")
            temp_data.extend(elsensor.lista)
            
            if not os.path.exists("temp.json"):
                with open("temp.json", "w") as file:
                    file.write(elsensor.datosdeljson1("temp"))
                    print("Archivo temp.json creado")
                    
            # Si hay conexión, pasar datos de temp.json a MongoDB
            if sensor_connection:
                with open("temp.json", "r") as file:
                    temp_data = json.load(file)
                
                if temp_data:
                    # Agregar los datos a la base de datos
                    elsensor.agregarproducto(temp_data, "sensores")
                    client.update_all_documents("Arduino", "Sensores", elsensor.datosdeljson1("sensores"))
                    
                    # Limpiar la lista
                    temp_data.clear()
                    os.remove("temp.json")
                    print("Archivo temp.json eliminado")
        
        
        
        respuesta = input("¿Deseas seguir en la opción? (s/n): ")
        if respuesta.lower() == "n":
            if os.path.exists("temp.json") and not sensor_connection:
                print(f"Eliminando archivo: temp.json")
                os.remove("temp.json")
            
            break
