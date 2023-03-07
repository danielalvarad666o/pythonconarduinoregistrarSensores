import math
import datetime
import json
from ClaseLista import lista

class SensorINFO(lista.Lista):
    def __init__(self):
        super().__init__
        self.lista=[]
        self.sensors = {}

    def add_sensor(self, line):
     try:
        with open("sensorinfo.json", "r") as f:
            self.lista = json.load(f)
     except FileNotFoundError:
        self.lista = []

     data = {}
     sensors = line.split('\n')
     for sensor in sensors:
        if ':' not in sensor:
            continue
        name, value = sensor.split(':')
        name_parts = name.split('.')
        sensor_name = name_parts[0]
        sensor_id = int(name_parts[1])
        data[sensor_name] = data.get(sensor_name, {})
        data[sensor_name][sensor_id] = float(value)

     for sensor_name, values in data.items():
        for sensor_id, value in values.items():
            if not math.isnan(value) and value > 0.0:
                clave = str(sensor_id)
                tipo = sensor_name.capitalize()

                # Comprobar si el sensor ya está registrado
                sensor_present = any(s.get('id') == sensor_id and s.get('tipo') == tipo for s in self.lista)
                if sensor_present:
                    #print(f"El sensor {tipo} id {sensor_id} ya está registrado.")
                    continue

                # Pedir información faltante al usuario
                print("Hola usuario :D se detecto un sensor nuevo")
                nombre = input(f"Por favor, proporcione un nombre para el sensor {tipo} id {sensor_id}: ")
                ubicacion = input(f"Por favor, proporcione una ubicación para el sensor {tipo} id {sensor_id}: ")
                descripcion = input(f"Por favor, proporcione una descripción para el sensor {tipo} id {sensor_id}: ")
                

                # Agregar el sensor a la lista
                sensor_info = {"id": sensor_id, "nombre": nombre, "tipo": tipo, "ubicacion": ubicacion, "descripcion": descripcion, "fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                self.lista.append(sensor_info)

    # Guardar los datos actualizados
     super().agregarproducto(self.lista,"sensorinfo")








    def guardar_json(self):
        with open("sensorinfo.json", "w") as f:
            json.dump(self.lista, f, indent=4)

    def cargar_json(self):
        with open("sensorinfo.json", "r") as f:
            self.lista = json.load(f)

    def cambiar_ubicacion(self):
     id_sensor =int( input("Por favor, proporcione el ID del sensor que desea cambiar su ubicación: "))
     tipo_sensor = input("Por favor, proporcione el tipo del sensor que desea cambiar su ubicación: ")
     
    
     for sensor in self.lista:
     
        if (sensor["id"] == id_sensor) & (sensor["tipo"] == tipo_sensor):
            ubicacion_nueva = input("Por favor, proporcione una nueva ubicación para el sensor: ")
            sensor["ubicacion"] = ubicacion_nueva
            self.guardar_json()
            print(f"La ubicación del sensor con ID {id_sensor} y tipo {tipo_sensor} se ha actualizado exitosamente.")
            return
        
     print(f"No se encontró ningún sensor con ID {id_sensor} y tipo {tipo_sensor}.")


    def cambiar_descripcion(self):
         id_sensor =int( input("Por favor, proporcione el ID del sensor que desea cambiar su ubicación: "))
         tipo_sensor = input("Por favor, proporcione el tipo del sensor que desea cambiar su ubicación: ")
     
    
         for sensor in self.lista:
     
          if (sensor["id"] == id_sensor) & (sensor["tipo"] == tipo_sensor):
            description_nueva = input("Por favor, proporcione una nueva description para el sensor: ")
            sensor["descripcion"] = description_nueva
            self.guardar_json()
            print(f"La Description del sensor con ID {id_sensor} y tipo {tipo_sensor} se ha actualizado exitosamente.")
            return
        
          print(f"No se encontró ningún sensor con ID {id_sensor} y tipo {tipo_sensor}.")
       
