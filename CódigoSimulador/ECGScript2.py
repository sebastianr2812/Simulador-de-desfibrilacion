# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 11:58:48 2018

@author: Juan Camilo
"""
################ IMPORTAR LIBRERIAS ######################

import math
import matplotlib.pyplot as plt
import ECGGen as ECG
import Normalizacion as Normal
import time
import numpy as np
import DACECG as DigRW
############## VALORES DETERMINADOS POR EL USUARIO ######

BPM=float(input('Introduzca la frecuencia cardiaca: '))
N=int(input('Introduzca el número de armónicos: '))

Frecs=BPM/60
T=1/Frecs
pi=3.1416

############### DURACIÓN DE ONDAS ########################

TPW=0.37*(math.sqrt(T))-0.22*T-0.06
TTW=1.06*(math.sqrt(T))-0.51*T-0.33
TQRS=0.25*(math.sqrt(T))-0.16*T-0.01 #0.02
TPQ=0.33*(math.sqrt(T))-0.18*T-0.08
TST=-0.09*(math.sqrt(T))+0.13*T+0.04

############## DESFASES ONDA P Y T #######################

DesfaseP=-0.5*TPW-TPQ-0.5*TQRS
DesfaseT=0.5*TPW+TST+0.5*TQRS

############# INTERVALOS DE TIEMPO #######################

A=-TPQ-0.5*TQRS-TPW
B=-TPQ-0.5*TQRS
C=TST+0.5*TQRS
D=TTW+TST+0.5*TQRS

############# CREACIÓN DE VECTORES ###################### 

t=np.linspace(0,3*T,3*T*100)
D1=np.zeros([len(t),1],dtype=np.float64)
D2=np.zeros([len(t),1],dtype=np.float64)
D3=np.zeros([len(t),1],dtype=np.float64)
avR=np.zeros([len(t),1],dtype=np.float64)
avL=np.zeros([len(t),1],dtype=np.float64)
avF=np.zeros([len(t),1],dtype=np.float64)
V1=np.zeros([len(t),1],dtype=np.float64)
V2=np.zeros([len(t),1],dtype=np.float64)
V3=np.zeros([len(t),1],dtype=np.float64)
V4=np.zeros([len(t),1],dtype=np.float64)
V5=np.zeros([len(t),1],dtype=np.float64)
V6=np.zeros([len(t),1],dtype=np.float64)
LV1=np.zeros([len(t),1],dtype=np.float64)
LV2=np.zeros([len(t),1],dtype=np.float64)
LV3=np.zeros([len(t),1],dtype=np.float64)
LV4=np.zeros([len(t),1],dtype=np.float64)
LV5=np.zeros([len(t),1],dtype=np.float64)
LV6=np.zeros([len(t),1],dtype=np.float64)

############ LEAD 1 ######################################

Ap=0.1
At=0.15
Aqrs=0.6

D1=ECG.ECG_NS(t,DesfaseP,DesfaseT,A,B,C,D,pi,TPW,TTW,TQRS,TPQ,TST,T,Aqrs,Ap,At,N)
Corte=((TQRS/2)+TST*0.5)/0.01
Corte=math.ceil(Corte)
D1[:]=D1[:]-D1[Corte]
for i in range (0,len(t)):
    if (D1[i]<-0.01):
        D1[i]=D1[Corte];
        


########### LEAD 2 ########################################

Ap=0.15
At=0.25
Aqrs=0.9
D2=ECG.ECG_NS(t,DesfaseP,DesfaseT,A,B,C,D,pi,TPW,TTW,TQRS,TPQ,TST,T,Aqrs,Ap,At,N)
D2[:]=D2[:]-D2[Corte]
for i in range (0,len(t)):
    if (D2[i]<-0.01):
        D2[i]=D2[Corte];
 

########### LEAD 3 ############################################

D3=D2-D1



################################################################
################ LAS BIPOLARES AUMENTADAS ######################
################################################################ 

##################### aVR ######################################

avR=(-1/2)*(D1+D2)


#################### aVL ########################################

avL=D1-(1/2)*D2



################### aVF #########################################

avF=D2-(1/2)*D1



################################################################
################ LAS PRECORDIALES ##############################
################################################################ 

################### V1 #########################################

Ar=0.2
As=0.5
At=0.1
Ap=0.05

V1=ECG.ECG_S(t,DesfaseP,DesfaseT,A,B,C,D,pi,TPW,TTW,TQRS,TPQ,TST,T,Ap,Ar,As,At,N)
V1[:]=V1[:]-V1[Corte];


################## V2 #############################################

Ar=0.4
As=0.7
At=0.2
Ap=0.1

V2=ECG.ECG_S(t,DesfaseP,DesfaseT,A,B,C,D,pi,TPW,TTW,TQRS,TPQ,TST,T,Ap,Ar,As,At,N)
V2[:]=V2[:]-V2[Corte];


################## V3 #############################################

Ar=1.0
As=0.5
At=0.3
Ap=0.2

V3=ECG.ECG_S(t,DesfaseP,DesfaseT,A,B,C,D,pi,TPW,TTW,TQRS,TPQ,TST,T,Ap,Ar,As,At,N)
V3[:]=V3[:]-V3[Corte];


################## V4 #############################################

Ap=0.1
At=0.25
Aqrs=1.1
V4=ECG.ECG_NS(t,DesfaseP,DesfaseT,A,B,C,D,pi,TPW,TTW,TQRS,TPQ,TST,T,Aqrs,Ap,At,N)
V4[:]=V4[:]-V4[Corte]
for i in range (0,len(t)):
    if (V4[i]<-0.01):
        V4[i]=V4[Corte];



################ V5 #######################################################

Ap=0.1
At=0.2
Aqrs=0.9
V5=ECG.ECG_NS(t,DesfaseP,DesfaseT,A,B,C,D,pi,TPW,TTW,TQRS,TPQ,TST,T,Aqrs,Ap,At,N)
V5[:]=V5[:]-V5[Corte]
for i in range (0,len(t)):
    if (V5[i]<-0.01):
        V5[i]=V5[Corte];

################################## V6 #####################################

Ap=0.1
At=0.15
Aqrs=0.7
V6=ECG.ECG_NS(t,DesfaseP,DesfaseT,A,B,C,D,pi,TPW,TTW,TQRS,TPQ,TST,T,Aqrs,Ap,At,N)
V6[:]=V6[:]-V6[Corte]
for i in range (0,len(t)):
    if (V6[i]<-0.01):
        V6[i]=V6[Corte];


################################ LATIGUILLOS PRECORDIALES ###################
LV1=V1+(1/3)*(D1+D2)
LV2=V2+(1/3)*(D1+D2)
LV3=V3+(1/3)*(D1+D2)
LV4=V4+(1/3)*(D1+D2)
LV5=V5+(1/3)*(D1+D2)
LV6=V6+(1/3)*(D1+D2)

D1N=Normal.Norm(5,-5,D1)
D2N=Normal.Norm(5,-5,D2)
LV1N = Normal.Norm(5,-5,LV1)
LV2N = Normal.Norm(5,-5,LV2)
LV3N = Normal.Norm(5,-5,LV3)
LV4N = Normal.Norm(5,-5,LV4)
LV5N = Normal.Norm(5,-5,LV5)
LV6N = Normal.Norm(5,-5,LV6)

DigRW.setup(0x48, 0x4a, 0x4b, 0x49, 0x4f, 0x4c, 0x4d, 0x4e)
i=0
timeFs=0.01
while True:
    
    DigRW.WriteDAC(D1N[i],D2N[i], LV1N[i], LV2N[i],LV3N[i],LV4N[i], LV5N[i],LV6N[i])
    time.sleep(0.0058)
    i=i+1
    if (i>=len(D1N)):
        i=0




##fig, aD1 = plt.subplots()
##aD1.plot(t, D1)
##aD1.set(xlabel='Tiempo (s)', ylabel='Voltaje (mV)', title='LEAD I')
##aD1.grid()
##plt.plot(t,D1)
##plt.show()
##
##fig, aD3 = plt.subplots()
##aD3.plot(t, D3)
##aD3.set(xlabel='Tiempo (s)', ylabel='Voltaje (mV)', title='LEAD III')
##aD3.grid()
##plt.plot(t,D3)
##plt.show()
##
##
##fig, aavR = plt.subplots()
##aavR.plot(t, avR)
##aavR.set(xlabel='Tiempo (s)', ylabel='Voltaje (mV)', title='LEAD avR')
##aavR.grid()
##plt.plot(t,avR)
##plt.show()
##
##fig, aavL = plt.subplots()
##aavL.plot(t, avL)
##aavL.set(xlabel='Tiempo (s)', ylabel='Voltaje (mV)', title='LEAD avL')
##aavL.grid()
##plt.plot(t,avL)
##plt.show()
##
##fig, aavF = plt.subplots()
##aavF.plot(t, avF)
##aavF.set(xlabel='Tiempo (s)', ylabel='Voltaje (mV)', title='LEAD avF')
##aavF.grid()
##plt.plot(t,avF)
##plt.show()
##
##fig, aV1 = plt.subplots()
##aV1.plot(t, V1)
##aV1.set(xlabel='Tiempo (s)', ylabel='Voltaje (mV)', title='LEAD V1')
##aV1.grid()
##plt.plot(t,V1)
##plt.show()
##
##fig, aV2 = plt.subplots()
##aV2.plot(t, V2)
##aV2.set(xlabel='Tiempo (s)', ylabel='Voltaje (mV)', title='LEAD V2')
##aV2.grid()
##plt.plot(t,V2)
##plt.show()
##
##
##fig, aV3 = plt.subplots()
##aV3.plot(t, V3)
##aV3.set(xlabel='Tiempo (s)', ylabel='Voltaje (mV)', title='LEAD V3')
##aV3.grid()
##plt.plot(t,V3)
##plt.show()
##
##fig, aV4 = plt.subplots()
##aV4.plot(t, V4)
##aV4.set(xlabel='Tiempo (s)', ylabel='Voltaje (mV)', title='LEAD V4')
##aV4.grid()
##plt.plot(t,V4)
##plt.show()
##
##
##fig, aV5 = plt.subplots()
##aV5.plot(t, V5)
##aV5.set(xlabel='Tiempo (s)', ylabel='Voltaje (mV)', title='LEAD V5')
##aV5.grid()
##plt.plot(t,V5)
##plt.show()
##
##fig, aV6 = plt.subplots()
##aV6.plot(t, V6)
##aV6.set(xlabel='Tiempo (s)', ylabel='Voltaje (mV)', title='LEAD V6')
##aV6.grid()
##plt.plot(t,V6)
##plt.show()
##
