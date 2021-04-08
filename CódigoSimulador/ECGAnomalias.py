
import numpy as np
import math
import ECGGenAn as ECGAn

############## VALORES DETERMINADOS POR EL USUARIO ######
def AnomFunc(N,T,t,Anomalia):
    
    print(Anomalia)
    print("s")
    
    
    if (Anomalia==2):
        print('Fibrilación ventricular')
        fib=np.loadtxt("/home/pi/Desktop/Simulador/arritmias/fibrilación.txt")
        Signal=fib
        fib2=np.append(fib,fib)
        t=np.linspace(0,14,len(fib2))
#         t=np.linspace(0,8,len(fib))
    
    elif (Anomalia==3):
        print('Taquicardia ventricular')
        fib=np.loadtxt("/home/pi/Desktop/Simulador/arritmias/TaquicardiaV.txt")
        Signal=fib
        t=np.linspace(0,8,len(fib))
    
    elif (Anomalia==4):
        print('Fibrilación auricular')
        fib=np.loadtxt("/home/pi/Desktop/Simulador/arritmias/UnstableAF.txt")
        Signal=fib
        t=np.linspace(0,8,len(fib))

    elif (Anomalia==5):
        print('Aleteo auricular')
        fib=np.loadtxt("/home/pi/Desktop/Simulador/arritmias/AtrialFlutter.txt")
        Signal=fib
        t=np.linspace(0,8,len(fib))
        
    elif (Anomalia==6):
        fib=np.loadtxt("/home/pi/Desktop/Simulador/arritmias/tsv.txt")
        Signal=fib
        t=np.linspace(0,8,len(fib))
        print('Taquicardia supraventricular')

    return Signal
