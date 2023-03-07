import serial
import json

class SensorData:
    def __init__(self, baudrate=9600):
        try:
         print("conectado serial")
         self.serial_port = serial.Serial('COM6', baudrate)
        except:
          print("EL puerto o serial no esta conectado")
            
    def read_sensor_data(self):
        self.line = self.serial_port.readline().decode().strip()
        return self.line
