import smbus
import time

bus = smbus.SMBus(1)

def insertar(v):
    y.append(v)
    #np.append(y,v)
def eliminar():
    y.pop(0)
def leer():
    reading = bus.read_byte(0x48) #Read AD
    v = reading*5/255