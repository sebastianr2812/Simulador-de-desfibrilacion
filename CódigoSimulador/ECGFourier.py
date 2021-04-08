# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 22:35:45 2018

@author: Juan Camilo
"""

import numpy as np
import math
import matplotlib.pyplot as plt
#import PCF8591v2 as DAC
import ECGGen as ECG
import Normalizacion
import time

#N=int(input('Digite número de armónicos: '))
#BPM=float(input('Digite el número de latidos por minuto: '))
N=30
BPM=60
Max=5
Min=-5

Frecs=BPM/60
T=1/Frecs
pi=3.1416
TPW=0.37*(math.sqrt(T))-0.22*T-0.06
TTW=1.06*(math.sqrt(T))-0.51*T-0.33
TQRS=0.25*(math.sqrt(T))-0.16*T-0.02
TPQ=0.33*(math.sqrt(T))-0.18*T-0.08
TST=-0.09*(math.sqrt(T))+0.13*T+0.04

DesfaseP=-0.5*TPW-TPQ-0.5*TQRS
DesfaseT=0.5*TPW+TST+0.5*TQRS

A=-TPQ-0.5*TQRS-TPW
B=-TPQ-0.5*TQRS
C=TST+0.5*TQRS
D=TTW+TST+0.5*TQRS


t=np.linspace(0,3,300)
D1=np.zeros([len(t),1],dtype=np.float64)
D2=np.zeros([len(t),1],dtype=np.float64)
D2DAC=D2
D3=np.zeros([len(t),1],dtype=np.float64)

Ap=0.5
At=0.75
Aqrs=1.5
D2=ECG.ECG_NS(t,DesfaseP,DesfaseT,A,B,C,D,pi,TPW,TTW,TQRS,TPQ,TST,T,Aqrs,Ap,At,N)
Corte=((TQRS/2)+TST*0.5)/0.01
Corte=math.ceil(Corte)
D2[:]=D2[:]-D2[Corte]
for i in range (0,len(t)):
    if (D2[i]<-0.1):
        D2[i]=D2[Corte];
    

plt.plot(t,D2)

Ap=0.1
Ar=1.4
As=0.5
At=0.6
D1=ECG.ECG_S(t,DesfaseP,DesfaseT,A,B,C,D,pi,TPW,TTW,TQRS,TPQ,TST,T,Ap,Ar,As,At,N)
plt.show()
plt.plot(t,D1)

D3[:]=D2[:]-D1[:]
plt.show()
plt.plot(t,D3)

D2DAC=Normalizacion.Norm(Max,Min,D2)
plt.show()
plt.plot(t,D2DAC)
"""
for j in range (0,20):
    for i in range (0,300):
        DAC.Write(D2DAC[i],0)
        time.sleep(0.01)
"""
