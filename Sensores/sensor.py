import json
import math

from ClaseLista import lista

import datetime

current_date = datetime.datetime.now()

class Sensor(lista.Lista):
    def __init__(self):
        super().__init__()
    
    def Crearsensor(self, line):
        data = {}
        sensors = line.strip().split('\n')
        for sensor in sensors:
            name, value = sensor.split(':')
            name_parts = name.split('.')
            if len(name_parts) < 2:
                # if name doesn't have expected format, skip it
                continue
            sensor_name = name_parts[0]
            sensor_id = int(name_parts[1])
            data[sensor_name] = data.get(sensor_name, {})
            data[sensor_name][sensor_id] = float(value)

        current_date = datetime.datetime.now()
        for sensor_name, values in data.items():
            for sensor_id, value in values.items():
                if not math.isnan(value):
                    self.id = sensor_id
                    self.nombre = sensor_name
                    self.valor = value
                    self.fecha = current_date.strftime('%Y-%m-%d %H:%M:%S')
                    diccionario_sensor = {
                        "Id": self.id,
                        "Tipo": self.nombre,
                        "Valor": self.valor,
                        "Fecha": self.fecha
                    }
                    self.lista.append(diccionario_sensor)

        super().agregarproducto(self.lista, "sensores")
