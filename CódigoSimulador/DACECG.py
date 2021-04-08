#IMportar las librerias para usar el modulo
import smbus
import time
import math

bus = smbus.SMBus(1)

#check your PCF8591 address by type in 'sudo i2cdetect -y 1' in terminal.
""" Función para determinar la direccion del Modulo """
# def setup(Addr1):
#   global address
#   address = Addr
def setup(Addr1, Addr2, Addr3, Addr4, Addr5, Addr6, Addr7, Addr8):
    
        global address1
        global address2
        global address3
        global address4
        global address5
        global address6
        global address7
        global address8
        address1 = Addr1
        address2 = Addr2
        address3 = Addr3
        address4 = Addr4
        address5 = Addr5
        address6 = Addr6
        address7 = Addr7
        address8 = Addr8
        
def leer(): #channel
    bus.write_byte(address1,0x42)
    reading=bus.read_byte(address1)
    v=reading*5/255
    return v
    
        
""" Función que envía datos al DAC"""       
# def WriteDAC(Dato,Dato2):
def WriteDAC(Dato,Dato2, Dato3, Dato4,Dato5,Dato6,Dato7,Dato8):
    try:
        temp1 = int(Dato)
        bus.write_byte_data(address1, 0x40, temp1)
        temp2=int(Dato2)
        bus.write_byte_data(address2, 0x40, temp2)
        temp3 = int(Dato3)
        bus.write_byte_data(address3, 0x40, temp3)
        temp4 = int(Dato4)
        bus.write_byte_data(address4, 0x40, temp4)
        temp5=int(Dato5)
        bus.write_byte_data(address5, 0x40, temp5)
##        temp6 = int(Dato6)
##        bus.write_byte_data(address6, 0x40, temp6)
        temp7=int(Dato7)
        bus.write_byte_data(address7, 0x40, temp7)
        temp8 = int(Dato8)
        bus.write_byte_data(address8, 0x40, temp8)
      
      
    except Exception as e:
        print ("Error: Device address: 0x%2X" % address1)
        print (e)
        
def WriteDAC1(Dato):
    try:
        
        temp1 = int(Dato)
        bus.write_byte_data(address1, 0x40, temp1)
        
    except Exception as e:
        print ("Error: Device address: 0x%2X" % address1)
        print (e)