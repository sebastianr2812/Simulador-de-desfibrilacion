# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 14:29:26 2018

@author: Juan Camilo
"""
import numpy as np
import math

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

t=np.linspace(0,3,300)
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