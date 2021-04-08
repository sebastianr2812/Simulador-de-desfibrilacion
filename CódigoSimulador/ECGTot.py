# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 10:33:01 2019

@author: Juan Camilo
"""

################ IMPORTAR LIBRERIAS ######################

import math
import matplotlib.pyplot as plt
import ECGGen as ECG
import Normalizacion
import time
import numpy as np

def ECGDualGuide(ATotal,BPM,N,t):
    ############## VALORES DETERMINADOS POR EL USUARIO ######

    Frecs=BPM/60
    T=1/Frecs
    pi=3.1416
    
    ############### DURACIÓN DE ONDAS ########################
    
    TPW=0.37*(math.sqrt(T))-0.22*T-0.06
    TTW=1.06*(math.sqrt(T))-0.51*T-0.33
    TQRS=0.25*(math.sqrt(T))-0.16*T-0.01 
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
    

    
    ############ LEAD 1 ######################################
    
    Ap=(1/10)*ATotal   #Ap=0.1
    At=(2/10)*ATotal  #At=0.15
    Aqrs=(5/10)*ATotal   #Aqrs=0.6
    
    D1=ECG.ECG_NS(t,DesfaseP,DesfaseT,A,B,C,D,pi,TPW,TTW,TQRS,TPQ,TST,T,Aqrs,Ap,At,N)
    Corte=((TQRS/2)+TST*0.5)/0.01
    Corte=math.ceil(Corte)
    D1[:]=D1[:]-D1[Corte]
    for i in range (0,len(t)):
        if (D1[i]<-0.01):
            D1[i]=D1[Corte];
    
    ########### LEAD 2 ########################################
    
    Ap=(2/10)*ATotal
    At=(2.5/10)*ATotal
    Aqrs=ATotal
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
    
    Ar=(2/10)*ATotal
    As=(4.5/10)*ATotal
    At=(0.7/10)*ATotal
    Ap=(0.5/10)*ATotal
    
    V1=ECG.ECG_S(t,DesfaseP,DesfaseT,A,B,C,D,pi,TPW,TTW,TQRS,TPQ,TST,T,Ap,Ar,As,At,N)
    V1[:]=V1[:]-V1[Corte]
    
    ################## V2 #############################################
    
    Ar=(4/10)*ATotal
    As=(7/10)*ATotal
    At=(1.7/10)*ATotal
    Ap=(1/10)*ATotal
    
    V2=ECG.ECG_S(t,DesfaseP,DesfaseT,A,B,C,D,pi,TPW,TTW,TQRS,TPQ,TST,T,Ap,Ar,As,At,N)
    
    V2[:]=V2[:]-V2[Corte]
    
    
    ################## V3 #############################################
    
    Ar=(9/10)*ATotal
    As=(5/10)*ATotal
    At=(3/10)*ATotal
    Ap=(2/10)*ATotal
    
    V3=ECG.ECG_S(t,DesfaseP,DesfaseT,A,B,C,D,pi,TPW,TTW,TQRS,TPQ,TST,T,Ap,Ar,As,At,N)
    V3[:]=V3[:]-V3[Corte]
    
    ################## V4 #############################################
    
    Ap=(1.2/10)*ATotal
    At=(2/10)*ATotal
    Aqrs=(11/10)*ATotal
    V4=ECG.ECG_NS(t,DesfaseP,DesfaseT,A,B,C,D,pi,TPW,TTW,TQRS,TPQ,TST,T,Aqrs,Ap,At,N)
    V4[:]=V4[:]-V4[Corte]
    for i in range (0,len(t)):
        if (V4[i]<-0.01):
            V4[i]=V4[Corte]
    
    ################ V5 #######################################################
    
    Ap=(1/10)*ATotal
    At=(2/10)*ATotal
    Aqrs=(9/10)*ATotal
    V5=ECG.ECG_NS(t,DesfaseP,DesfaseT,A,B,C,D,pi,TPW,TTW,TQRS,TPQ,TST,T,Aqrs,Ap,At,N)
    V5[:]=V5[:]-V5[Corte]
    for i in range (0,len(t)):
        if (V5[i]<-0.01):
            V5[i]=V5[Corte]
    
    ################################## V6 #####################################
    
    Ap=(1/10)*ATotal
    At=(1.2/10)*ATotal
    Aqrs=(7/10)*ATotal
    V6=ECG.ECG_NS(t,DesfaseP,DesfaseT,A,B,C,D,pi,TPW,TTW,TQRS,TPQ,TST,T,Aqrs,Ap,At,N)
    V6[:]=V6[:]-V6[Corte]
    for i in range (0,len(t)):
        if (V6[i]<-0.01):
            V6[i]=V6[Corte]
    
    ################################ LATIGUILLOS PRECORDIALES ###################
    LV1=V1+(1/3)*(D1+D2)
    LV2=V2+(1/3)*(D1+D2)
    LV3=V3+(1/3)*(D1+D2)
    LV4=V4+(1/3)*(D1+D2)
    LV5=V5+(1/3)*(D1+D2)
    LV6=V6+(1/3)*(D1+D2)
    
    Signal=np.zeros((15,len(t)))
    Signal[0,0:len(t)]=D1[:,0]
    Signal[1,0:len(t)]=D2[:,0]
    Signal[2,0:len(t)]=LV1[:,0]
    Signal[3,0:len(t)]=LV2[:,0]
    Signal[4,0:len(t)]=LV3[:,0]
    Signal[5,0:len(t)]=LV4[:,0]
    Signal[6,0:len(t)]=LV5[:,0]
    Signal[7,0:len(t)]=LV6[:,0]
    Signal[8,0:len(t)]=V1[:,0]
    Signal[9,0:len(t)]=V2[:,0]
    Signal[10,0:len(t)]=V3[:,0]
    Signal[11,0:len(t)]=V4[:,0]
    Signal[12,0:len(t)]=V5[:,0]
    Signal[13,0:len(t)]=V6[:,0]
    
    
    return Signal