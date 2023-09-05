from serial import Serial
from decouple import config

ARDUINO_PORT = config("ARDUINO_PORT")
ARDUINO_BAUDRATE = config("ARDUINO_BAUDRATE")

serial = Serial(ARDUINO_PORT, ARDUINO_BAUDRATE)

def getValueFromArduino(name):
        line = serial.readline().decode('utf-8').rstrip()
        print(line)
        
        # Dividir la línea de datos en las partes correspondientes
        parts = line.split('|')

        for part in parts:
            
            if part.find(name) != -1:
                var = part.split(':')

                # Recuperar valor del módulos
                return float(var[1])