#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import*
from tkinter import ttk
from tkinter import font
from tkinter import messagebox as MessageBox
from tkinter import simpledialog
from ttkSimpleDialog import ttkSimpleDialog
import ECGTot as ECG
import ProcesSel as ProSel
from PIL import Image, ImageTk
import threading
import time
import ECGAnomalias as ECGAnom
import math
import NoiseAdd as RuidoAdd
import Normalizacion as Normal
import DACECG as DigRW
import ADCDesf as ADC
import resultado as Res
import os, random

global Detener
Detener=1
def plotter(modo):
    global Detener, ECGSigns, x, w3, tamaño, total_time, y, fib,bAlerta,ArritNum
    fib=np.loadtxt("/home/pi/Desktop/Simulador/arritmias/fibrilación.txt")
    D1N=Normal.Norm(5,-5,ECGSigns)
    D1N=D1N/4
    DigRW.setup(0x48, 0x48, 0x48, 0x48, 0x48, 0x48, 0x48, 0x48)
    i=0
    cont=0
    mcont=10
        
    """ADC"""    
    Detener=1
    x=[]
    y=[]
    while (Detener==1):
#     for i in range (SAMPLES):
        start = time.monotonic()
        DigRW.WriteDAC1(D1N[i])
        i=i+1
        cont=cont+1
              
        if (i>=len(D1N)):
            i=0           
        ###leer      
        v=DigRW.leer()
        time.sleep(0.00000002)
        y.append(v)
        if (len(y)>=tamaño):
            y.pop(0)
            if (y[25]>=umbral):
                Detener=0
                
    if Detener==0:
        end = time.monotonic()
        total_time = end - start
        window3(modo,i)
                

    
#         print("Time of capture: {}s".format(total_time))
#     print("Sample rate actual={}".format(SAMPLES / total_time))
    
def BasicM(modo):
    global Detener, ECGSigns, w2, t, A, BPM, ArritNum
    Detener=1

    print("Proceso de simulación básico")
    ArritNum=float(ArritNum)
    BPM=60
    A=3
    F=BPM/60
    T=1/F
    t=np.linspace(0,3*T,3*T*100)
    N=int(30)
    ATotal=float(A)
    ECGSigns=ECG.ECGDualGuide(ATotal,BPM,N,t)
    if (modo=="0"):
        ECGSigns=ECGAnom.AnomFunc(N,T,t,ArritNum)
        

    if (modo=="1"):
        Arrit=ComboArritmias.get()
        ArritNum=ProSel.SelectProcArrit(Arrit)      
        ECGSigns=ECGAnom.AnomFunc(N,T,t,ArritNum)
        
    
#     w2.protocol("WM_DELETE_WINDOW",lambda:Stop("w2"))  
    print("Doit")
    threading.Thread(target=lambda:plotter(modo)).start()

def plotter2():
    global Detener, lec, x, tamaño, total_time, y
    DigRW.setup(0x48, 0x48, 0x48, 0x48, 0x48, 0x48, 0x48, 0x48)
    """ADC"""
    Detener=1
    x=[]
    y=[]
    while (Detener==1):
#     for i in range (SAMPLES):
        start = time.monotonic()
        ###leer
        v=DigRW.leer()
        time.sleep(0.00015)
        y.append(v)
       
        if (len(y)>=tamaño):
            y.pop(0)
            if (y[25]>=umbral):
                Detener=0                    
    
    if Detener==0:
        end = time.monotonic()
        total_time = end - start
        valoreslectura()
    
        
def plotter3(modo):
    global Detener, ECGSigns, x, w3, tamaño, total_time, y, ComboArritmias,boxFrecuencia,boxAmplitud
    ArritNum=1
    BPM=70
    A=2
#     Arritmia=str(ComboArritmias.get())
    F=BPM/60
    T=1/F
    t=np.linspace(0,3*T,3*T*100)
    N=int(30)
    ATotal=float(A)
    ECGSigns=ECG.ECGDualGuide(ATotal,BPM,N,t)
    if (modo=="3"):
        A=int(Amplitud.get())
        BPM=int(Frecuencia.get())
        F=BPM/60
        T=1/F
        t=np.linspace(0,3*T,3*T*100)
        N=int(30)
        ATotal=float(A)
        ECGSigns=ECG.ECGDualGuide(ATotal,BPM,N,t)
        continuar=PhotoImage(file="/home/pi/Desktop/Simulador/boton_mp.png")
        boton2=tk.Button(ecg,image=continuar,command=lambda:Stop("ecg"),relief="flat",activeforeground="white",activebackground="white",background="white",foreground="white",highlightthickness=0,bd=0)
        boton2.image = continuar
        boton2.place(x=46,y=46)
        continuar=PhotoImage(file="/home/pi/Desktop/Simulador/boton_cerrar.png")
        boton2=tk.Button(ecg,image=continuar,command=lambda:Stop("close"),relief="flat",activeforeground="white",activebackground="white",background="white",foreground="white",highlightthickness=0,bd=0)
        boton2.image = continuar
        boton2.place(x=1803,y=47)
        ecg.protocol("WM_DELETE_WINDOW",lambda:Stop("ecg"))

    if (ArritNum!=1):  
        ECGSigns=ECGAnom.AnomFunc(N,T,t,ArritNum)        
        
    D1N=Normal.Norm(5,-5,ECGSigns[0,:])/2.5
    D2N=Normal.Norm(5,-5,ECGSigns[1,:])/2.5
    LV1N = Normal.Norm(5,-5,ECGSigns[2,:])/2.5
    LV2N = Normal.Norm(5,-5,ECGSigns[3,:])/2.5
    LV3N = Normal.Norm(5,-5,ECGSigns[4,:])/2.5
    LV4N = Normal.Norm(5,-5,ECGSigns[5,:])/2.5
    LV5N = Normal.Norm(5,-5,ECGSigns[6,:])/2.5
    LV6N = Normal.Norm(5,-5,ECGSigns[7,:])/2.5
    DigRW.setup(0x48, 0x48, 0x48, 0x48, 0x48, 0x48, 0x48, 0x48)
  #  DigRW.setup(0x48, 0x4a, 0x4b, 0x49, 0x4f, 0x4c, 0x4d, 0x4e)
    i=0
    Detener=1
    while (Detener==1):
        start = time.monotonic()
#         DigRW.WriteDAC(D1N[i],D2N[i])
        DigRW.WriteDAC(D1N[i],D2N[i], LV1N[i], LV2N[i],LV3N[i],LV4N[i], LV5N[i],LV6N[i])
        i=i+1
        if (i>=len(D1N)):
            i=0
        time.sleep(0.00883) 
        end = time.monotonic()
        total_time = end - start           


def Stop(ventana):
    global Detener, Guide,w1, w2, w3, lec,ale, ecg
    Detener=2
    if ventana=="lec":
        lec.destroy()
        window1()
    if ventana=="ecg":
        ecg.destroy()
        window1()
    if ventana=="close":
        Guide.destroy()
    if ventana=="ale":
        ale.destroy()
        window1()
    if ventana=="ing":
        ing.destroy()
        window1()
    if ventana=="G":
        Guide.destroy()

def window1():
    global w1,w2
    Guide.withdraw()
    w1= tk.Toplevel()
    w=1920
    h=1080

    w1.attributes("-fullscreen",True)
    image=Image.open("/home/pi/Desktop/Simulador/Selección de modo.png")
    photo=ImageTk.PhotoImage(image)
    label = Label(image=photo)
    background_label=tk.Label(w1,image=photo).place(x=0,y=0,relwidth=1,relheight=1)
    label.image = photo
    aleatorio=PhotoImage(file="/home/pi/Desktop/Simulador/paciente_aleatorio.png")
    boton=tk.Button(w1,image=aleatorio,command=p_aleatorio, width=278,height=303,relief="flat",activeforeground="#9AE8CA",activebackground="#9AE8CA",background="#9AE8CA",foreground="#9AE8CA",highlightthickness=0,bd=0)
    boton.image = aleatorio
    boton.place(x=458,y=267)
    continuar=PhotoImage(file="/home/pi/Desktop/Simulador/boton_cerrar.png")
    boton2=tk.Button(w1,image=continuar,command=lambda:Stop("close"),relief="flat",activeforeground="white",activebackground="white",background="white",foreground="white",highlightthickness=0,bd=0)
    boton2.image = continuar
    boton2.place(x=1803,y=49)
    
    ingresar=PhotoImage(file="/home/pi/Desktop/Simulador/ingresar_paciente.png")
    boton2=tk.Button(w1,image=ingresar,command=p_ingresar,width=296,height=288,relief="flat",activeforeground="#9AE8CA",activebackground="#9AE8CA",background="#9AE8CA",foreground="#9AE8CA",highlightthickness=0,bd=0)
    boton2.image = ingresar
    boton2.place(x=1175,y=274)
   
    analizador=PhotoImage(file="/home/pi/Desktop/Simulador/modo_analizador.png")
    boton3=tk.Button(w1,image=analizador,command=lectura,width=287,height=108,relief="flat",activeforeground="#9AE8CA",activebackground="#9AE8CA",background="#9AE8CA",foreground="#9AE8CA",highlightthickness=0,bd=0)
    boton3.image = analizador
    boton3.place(x=447,y=701)
   
    simu=PhotoImage(file="/home/pi/Desktop/Simulador/modo_simu.png")
    boton4=tk.Button(w1,image=simu,command=simECG, width=278,height=116,relief="flat",activeforeground="#9AE8CA",activebackground="#9AE8CA",background="#9AE8CA",foreground="#9AE8CA",highlightthickness=0,bd=0)
    boton4.image = simu
    boton4.place(x=1186,y=697)

def p_aleatorio():
    global w1,A,BPM,fib, ale, bAlerta, ArritNum
    w1.destroy()
    ale= tk.Toplevel()
    ale.update_idletasks()
    ale.attributes("-fullscreen",True)
    image=Image.open("/home/pi/Desktop/Simulador/Fondo vacío.png")
    photo=ImageTk.PhotoImage(image)
    label = Label(image=photo)
    background_label=tk.Label(ale,image=photo).place(x=0,y=0,relwidth=1,relheight=1)
    label.image = photo
    
    Alerta=PhotoImage(file="/home/pi/Desktop/Simulador/D_Aviso de alerta.png")
    bAlerta=tk.Label(ale,image=Alerta,background="white",foreground="white")
    bAlerta.image = Alerta
    bAlerta.place(x=960,y=470)
    
    continuar=PhotoImage(file="/home/pi/Desktop/Simulador/boton_mp.png")
    boton2=tk.Button(ale,image=continuar,command=lambda:Stop("ale"),relief="flat",activeforeground="white",activebackground="white",background="white",foreground="white",highlightthickness=0,bd=0)
    boton2.image = continuar
    boton2.place(x=46,y=46)
    continuar=PhotoImage(file="/home/pi/Desktop/Simulador/boton_cerrar.png")
    boton2=tk.Button(ale,image=continuar,command=lambda:Stop("close"),relief="flat",activeforeground="white",activebackground="white",background="white",foreground="white",highlightthickness=0,bd=0)
    boton2.image = continuar
    boton2.place(x=1803,y=47)
    
    BPM=60
    A=3
    F=BPM/60
    T=1/F
    t=np.linspace(0,3*T,3*T*100)
    N=int(30)
    ATotal=float(A)
    f=random.choice(os.listdir("/home/pi/Desktop/Simulador/Pacientes/"))
    outdir="/home/pi/Desktop/Simulador/Pacientes/"
    full_path= os.path.join(outdir,f)
    ArritNum=float(f[0])
    ECGSigns=ECGAnom.AnomFunc(N,T,t,ArritNum)
    
    Paciente=PhotoImage(file=full_path)
    boton=tk.Label(ale,image=Paciente,background="white",foreground="white")
    boton.image = Paciente
    boton.place(x=53,y=418)
    
    fib=ECGSigns
    fib2=np.append(fib,fib)
    t=np.linspace(0,14,len(fib2))
    fig= Figure(figsize=(18,2))
    a=fig.add_subplot(111)
    a.plot(t,fib2)
    
    a.set_title ("Señal de ECG simulada", fontsize=8)
    a.set_ylabel("miliVoltios [mV]", fontsize=6)
    a.set_xlabel("Tiempo (s)", fontsize=6)
    
    canvas = FigureCanvasTkAgg(fig,master=ale)
    canvas.get_tk_widget().pack()
    canvas.get_tk_widget().place(relx=0.5,y=240,anchor="center")
    canvas.draw()
    BasicM("0")
    
def p_ingresar():
    global bAlerta, nombre, edad, sexo, ComboArritmias,ArritNum, Arritmia, Sexo, w1, ing, boxNombre, boxEdad, boxSexo, background_label, label
    
    w1.destroy()
    ing= tk.Toplevel()
    ing.update_idletasks()
    ing.attributes("-fullscreen",True)
    image=Image.open("/home/pi/Desktop/Simulador/Simulacion Paciente Ingresado.png")
    photo=ImageTk.PhotoImage(image)
    label = Label(image=photo)
    background_label=tk.Label(ing,image=photo).place(x=0,y=0,relwidth=1,relheight=1)
    label.image = photo
    
    nombre="Ingresar Nombre"
    sexo="Ingresar sexo"
    edad="Ingresar edad"
    boxNombre=Entry(ing,textvariable=nombre, font=Helvfont4,).place(x=780,y=334,width=597, height=40)
    boxEdad=Entry(ing,textvariable=edad,font=Helvfont4).place(x=739,y=449,width=104,height=34)
    """COMBOBOX"""
    ComboArritmias=ttk.Combobox(ing)
    ComboArritmias.place(x=1168,y=456,width=250,height=30)
    ComboArritmias['values']=('Fibrilación ventricular','Taquicardia ventricular','Taquicardia supraventricular','Fibrilación auricular','Aleteo auricular')
    ComboArritmias.current(0)
    boxSexo=ttk.Combobox(ing)
    boxSexo.place(x=728,y=572,width=50,height=30)
    boxSexo['values']=('','M','F')
    boxSexo.current(0)
    
    continuar=PhotoImage(file="/home/pi/Desktop/Simulador/boton_mp.png")
    boton2=tk.Button(ing,image=continuar,command=lambda:Stop("ing"),relief="flat",activeforeground="white",activebackground="white",background="white",foreground="white",highlightthickness=0,bd=0)
    boton2.image = continuar
    boton2.place(x=46,y=46)
    continuar=PhotoImage(file="/home/pi/Desktop/Simulador/boton_cerrar.png")
    boton2=tk.Button(ing,image=continuar,command=lambda:Stop("close"),relief="flat",activeforeground="white",activebackground="white",background="white",foreground="white",highlightthickness=0,bd=0)
    boton2.image = continuar
    boton2.place(x=1803,y=47)
    
    
    continuar=PhotoImage(file="/home/pi/Desktop/Simulador/Boton_continuar.png")
    boton2=tk.Button(ing,image=continuar,command=P_ingresado,width=333,height=119,relief="flat",activeforeground="white",activebackground="white",background="white",foreground="white",highlightthickness=0,bd=0)
    boton2.image = continuar
    boton2.place(x=1338,y=650)

def P_ingresado():
    global ing,ComboArritmias,ArritNum, boxNombre, boxEdad, boxSexo, label, boton2, bAlerta
    image=Image.open("/home/pi/Desktop/Simulador/Funcionamiento Paciente ingresado.png")
    photo=ImageTk.PhotoImage(image)
    label = Label(image=photo)
    background_label=tk.Label(ing,image=photo).place(x=0,y=0,relwidth=1,relheight=1)
    label.image = photo
    
    SexoP=tk.StringVar()
    ArritmiaP=tk.StringVar()
    Arritmia=str(ComboArritmias.get())
    Sexo=(boxSexo.get())
    ArritmiaP.set(Arritmia)
    SexoP.set(Sexo)
    
    continuar=PhotoImage(file="/home/pi/Desktop/Simulador/boton_mp.png")
    boton2=tk.Button(ing,image=continuar,command=lambda:Stop("ing"),relief="flat",activeforeground="white",activebackground="white",background="white",foreground="white",highlightthickness=0,bd=0)
    boton2.image = continuar
    boton2.place(x=50,y=51)
    continuar=PhotoImage(file="/home/pi/Desktop/Simulador/boton_cerrar.png")
    boton2=tk.Button(ing,image=continuar,command=lambda:Stop("close"),relief="flat",activeforeground="white",activebackground="white",background="white",foreground="white",highlightthickness=0,bd=0)
    boton2.image = continuar
    boton2.place(x=1812,y=57)
    
    BPM=60
    A=3
    F=BPM/60
    T=1/F
    t=np.linspace(0,3*T,3*T*100)
    N=int(30)
    ATotal=float(A)
    ArritNum=ProSel.SelectProcArrit(Arritmia)
    ECGSigns=ECGAnom.AnomFunc(N,T,t,ArritNum)
    fib=ECGSigns
    fib2=np.append(fib,fib)
    t=np.linspace(0,12,len(fib2))
    fig= Figure(figsize=(18,2))
    a=fig.add_subplot(111)
    a.plot(t,fib2)
    
    Alerta=PhotoImage(file="/home/pi/Desktop/Simulador/D_Aviso de alerta.png")
    bAlerta=tk.Label(ing,image=Alerta,background="white",foreground="white")
    bAlerta.image = Alerta
    bAlerta.place(x=960,y=470)

    TextAmp=Label(ing,textvariable=ArritmiaP,font=Helvfont3, background="#9AE8CA").place(x=308,y=619)
    TextAmp=Label(ing,textvariable=nombre,font=Helvfont3, background="#9AE8CA").place(x=325,y=485)
    TextAmp=Label(ing,textvariable=SexoP,font=Helvfont3, background="#9AE8CA").place(x=307,y=534)
    TextAmp=Label(ing,textvariable=edad,font=Helvfont3, background="#9AE8CA").place(x=312,y=576)
    
    
    a.set_title ("Señal de ECG simulada", fontsize=8)
    a.set_ylabel("miliVoltios [mV]", fontsize=6)
    a.set_xlabel("Tiempo (s)", fontsize=6)
    
    canvas = FigureCanvasTkAgg(fig,master=ing)
    canvas.get_tk_widget().pack()
    canvas.get_tk_widget().place(relx=0.5,y=240,anchor="center")
    canvas.draw()
    BasicM("1")


def simECG():
    global w1,A,BPM,fib, ale, bAlerta, ArritNum, lec,ecg,ComboArritmias,Frecuencia,Amplitud
    
    w1.destroy()
    ecg= tk.Toplevel()
    ecg.update_idletasks()
    ecg.attributes("-fullscreen",True)
    image=Image.open("/home/pi/Desktop/Simulador/Fondo vacío.png")
    photo=ImageTk.PhotoImage(image)
    label = Label(image=photo)
    background_label=tk.Label(ecg,image=photo).place(x=0,y=0,relwidth=1,relheight=1)
    label.image = photo
    
    continuar=PhotoImage(file="/home/pi/Desktop/Simulador/boton_mp.png")
    boton2=tk.Button(ecg,image=continuar,command=lambda:Stop("ecg"),relief="flat",activeforeground="white",activebackground="white",background="white",foreground="white",highlightthickness=0,bd=0)
    boton2.image = continuar
    boton2.place(x=46,y=46)
    continuar=PhotoImage(file="/home/pi/Desktop/Simulador/boton_cerrar.png")
    boton2=tk.Button(ecg,image=continuar,command=lambda:Stop("close"),relief="flat",activeforeground="white",activebackground="white",background="white",foreground="white",highlightthickness=0,bd=0)
    boton2.image = continuar
    boton2.place(x=1803,y=47)
    ecg.protocol("WM_DELETE_WINDOW",lambda:Stop("ecg"))
    
    SeñalEcg="Ingresar Señal"
    Amplitud=StringVar()
    Frecuencia=StringVar()
    boxFrecuencia=Entry(ecg,textvariable=Frecuencia, font=Helvfont4,).place(x=1100,y=490,width=50, height=34, anchor="center")
    boxAmplitud=Entry(ecg,textvariable=Amplitud,font=Helvfont4).place(x=1100,y=590,width=50,height=34, anchor="center")
    
    
    TextAmp=Label(ecg,text="INGRESE LOS VALORES A SIMULAR",font=Helvfont, bg="white").place(relx=0.5,y=250,anchor="center")
    TextAmp=Label(ecg,text="Señal ECG:",font=Helvfont4, bg="white").place(relx=0.35,y=400,anchor="center")
    TextAmp=Label(ecg,text="Ritmo sinusal normal",font=Helvfont4, bg="white").place(x=1100,y=400,anchor="center")
    TextAmp=Label(ecg,text="Frecuencia(BPM):",font=Helvfont4, bg="white").place(relx=0.35,y=500,anchor="center")
    TextAmp=Label(ecg,text="Amplitud(mV):",font=Helvfont4, bg="white").place(relx=0.35,y=600,anchor="center")
    
    continuar=PhotoImage(file="/home/pi/Desktop/Simulador/Boton_continuar.png")
    boton2=tk.Button(ecg,image=continuar,command=ECG_simu,width=333,height=119,relief="flat",activeforeground="white",activebackground="white",background="white",foreground="white",highlightthickness=0,bd=0)
    boton2.image = continuar
    boton2.place(x=1338,y=650)
def ECG_simu():
#     lambda:plotter3("3")
    print("Doit")
    threading.Thread(target=lambda:plotter3("3")).start()
#     threading.Thread(target=plotter3).start()

def lectura():
    global w1,A,BPM,fib, ale, bAlerta, ArritNum, lec
    
    w1.destroy()
    lec= tk.Toplevel()
    lec.update_idletasks()
    lec.attributes("-fullscreen",True)
    image=Image.open("/home/pi/Desktop/Simulador/Fondo vacío.png")
    photo=ImageTk.PhotoImage(image)
    label = Label(image=photo)
    background_label=tk.Label(lec,image=photo).place(x=0,y=0,relwidth=1,relheight=1)
    label.image = photo
    
    continuar=PhotoImage(file="/home/pi/Desktop/Simulador/boton_mp.png")
    boton2=tk.Button(lec,image=continuar,command=lambda:Stop("lec"),relief="flat",activeforeground="white",activebackground="white",background="white",foreground="white",highlightthickness=0,bd=0)
    boton2.image = continuar
    boton2.place(x=46,y=46)
    continuar=PhotoImage(file="/home/pi/Desktop/Simulador/boton_cerrar.png")
    boton2=tk.Button(lec,image=continuar,command=lambda:Stop("close"),relief="flat",activeforeground="white",activebackground="white",background="white",foreground="white",highlightthickness=0,bd=0)
    boton2.image = continuar
    boton2.place(x=1803,y=47)
    
    TextRlD=Label(lec,text="Realice la descarga",font=Helvfont5, bg="white")
    TextRlD.place(relx=0.5,rely= 0.4, anchor="center")
    lec.protocol("WM_DELETE_WINDOW",lambda:Stop("lec")) 
        
    print("Doit")
    threading.Thread(target=plotter2).start()
    
def valoreslectura():
    global lec, TextRlD, x_cor, y_cor, BotonD, total_time, y
    image=Image.open("/home/pi/Desktop/Simulador/Fondo vacío.png")
    photo=ImageTk.PhotoImage(image)
    label = Label(image=photo)
    background_label=tk.Label(lec,image=photo).place(x=0,y=0,relwidth=1,relheight=1)
    label.image = photo
    continuar=PhotoImage(file="/home/pi/Desktop/Simulador/boton_mp.png")
    boton2=tk.Button(lec,image=continuar,command=lambda:Stop("lec"),relief="flat",activeforeground="white",activebackground="white",background="white",foreground="white",highlightthickness=0,bd=0)
    boton2.image = continuar
    boton2.place(x=46,y=46)
    continuar=PhotoImage(file="/home/pi/Desktop/Simulador/boton_cerrar.png")
    boton2=tk.Button(lec,image=continuar,command=lambda:Stop("close"),relief="flat",activeforeground="white",activebackground="white",background="white",foreground="white",highlightthickness=0,bd=0)
    boton2.image = continuar
    boton2.place(x=1803,y=47)
    
    [E, I, V, t2, x]=Res.analizador(total_time,y)
    Energia.set("Energía:   " + str(round(E*1000))+" (J)")
    Tension.set("Tensión:   " + str(round(V,4))+" (V)")
    Corriente.set("Corriente:   " + str(round(I,4))+" (A)")

#     Boton=ttk.Button(lec,text="OTRA LECTURA", width=15,command=lambda:Stop("lec2")).place(x=150,y=600, anchor="center")
    
    fig= Figure(figsize=(7,5))
    a=fig.add_subplot(111)
    a.plot(t2[19:62]-t2[25],x[19:62])

            
    a.set_title ("Señal de Desfibrilación", fontsize=10,weight="bold")
    a.set_ylabel("Voltios (V)", fontsize=8)
    a.set_xlabel("Tiempo (s)", fontsize=8)
    
    canvas = FigureCanvasTkAgg(fig,master=lec)
    canvas.get_tk_widget().pack()
    canvas.get_tk_widget().place(relx=0.5,rely=0.35, anchor="center")
    
    """textbox"""
    TextAmp=Label(lec,textvariable=Energia,font=Helvfont4, bg="white").place(relx=0.5,y=720,anchor="center")
    TextAmp=Label(lec,textvariable=Tension,font=Helvfont4, bg="white").place(relx=0.5,y=760,anchor="center")
    TextAmp=Label(lec,textvariable=Corriente,font=Helvfont4, bg="white").place(relx=0.5,y=800,anchor="center")


def window3(modo,i):
    global  w2, w3, total_time, y, ale, bAlerta, ArritNum
    print("capture: {}".format(ArritNum))
    if modo == "0":
        """VALORES FINALES """
        [E, I, V, t2, x]=Res.analizador(total_time,y)
        if (ArritNum==4):
            D=res.cardiov(i)
            DF=D*T2
            print("D1: {}s".format(D))
            print("D: {}s".format(DF))
        F=60//60
        T=1//F
        t=np.linspace(0,3*T,3*T*100)
        N=int(30)
        ATotal=float(5)
        ECGSigns=ECG.ECGDualGuide(ATotal,BPM,N,t)
        bAlerta.place_forget()  
        
        fig2= Figure(figsize=(7,5))
        b = fig2.add_subplot(111)
        b.plot(t2[19:62]-t2[25],x[19:62])
    #     b.plot(x[15:])
                
        b.set_title ("Señal de Desfibrilación", fontsize=10,weight="bold")
        b.set_ylabel("Voltios (V)", fontsize=8)
        b.set_xlabel("Tiempo (s)", fontsize=8)
        
        canvas2 = FigureCanvasTkAgg(fig2,ale)
        canvas2.get_tk_widget().place(x=650,y=354)
         
            
        """Textbox """
        Energia.set("Energía:   " + str(round(E,4))+" (J)")
        Tension.set("Tensión:   " + str(round(V,4))+" (V)")
        Corriente.set("Corriente:   " + str(round(I,4))+" (A)")
        
        TextAmp=Label(ale,textvariable=Energia,font=Helvfont3, bg="white").place(x=1400,y=520)
        TextAmp=Label(ale,textvariable=Tension,font=Helvfont3, bg="white").place(x=1400,y=570)
        TextAmp=Label(ale,textvariable=Corriente,font=Helvfont3, bg="white").place(x=1400,y=620)

        ale.protocol("WM_DELETE_WINDOW",lambda:Stop("w3")) 
        print("Doit")
        threading.Thread(target=lambda:plotter3("1")).start()
    
     
    elif modo =="1":  
        """VALORES FINALES """
        [E, I, V, t2, x]=Res.analizador(total_time,y)
        if (ArritNum==4):
            D=Res.cardiov(i)
            DF=D*total_time
            print("Ind: {}ms".format(D))
            print("TT: {}ms".format(total_time))
            print("D: {}ms".format(DF*1000))
        F=60//60
        T=1//F
        t=np.linspace(0,3*T,3*T*100)
        N=int(30)
        ATotal=float(5)
        ECGSigns=ECG.ECGDualGuide(ATotal,BPM,N,t)
        bAlerta.place_forget()  

        fig2= Figure(figsize=(7,5))
        b = fig2.add_subplot(111)
        b.plot(t2[19:62]-t2[25],x[19:62])
    #     b.plot(x[15:])
                
        b.set_title ("Señal de Desfibrilación", fontsize=10,weight="bold")
        b.set_ylabel("Voltios (V)", fontsize=8)
        b.set_xlabel("Tiempo (s)", fontsize=8)
        
        canvas2 = FigureCanvasTkAgg(fig2,ing)
    #     canvas2 = FigureCanvasTkAgg(fig2,vent)
        canvas2.get_tk_widget().place(x=650,y=354)
         
    #     np.savetxt("test.txt",y)
            
        """Textbox """
        Energia.set("Energía:   " + str(round(E,4))+" (J)")
        Tension.set("Tensión:   " + str(round(V,4))+" (V)")
        Corriente.set("Corriente:   " + str(round(I,4))+" (A)")
        
        TextAmp=Label(ing,textvariable=Energia,font=Helvfont3, bg="white").place(x=1400,y=520)
        TextAmp=Label(ing,textvariable=Tension,font=Helvfont3, bg="white").place(x=1400,y=570)
        TextAmp=Label(ing,textvariable=Corriente,font=Helvfont3, bg="white").place(x=1400,y=620)

#         ing.protocol("WM_DELETE_WINDOW",lambda:Stop("w3")) 
        print("Doit")
        threading.Thread(target=lambda:plotter3("1")).start()

    
        
"""Raiz"""        
Guide=tk.Tk()
Guide.iconphoto(True, tk.PhotoImage(file="/home/pi/Desktop/Simulador/desfibrilador.png"))
Guide.title("Simulador de desfibrilación")
w=1920
h=1080

screen_width=Guide.winfo_screenwidth()
screen_height=Guide.winfo_screenheight()
x_cor= (screen_width/2 - w/2)
y_cor= (screen_height/2 - h/2)
Guide.attributes("-fullscreen",True)
background_image=tk.PhotoImage(file="/home/pi/Desktop/Simulador/Fondo Inicio.png")
background_label=tk.Label(Guide,image=background_image).place(x=0,y=0,relwidth=1,relheight=1)




"""CONFIGURACIÓN FUENTES"""

Helvfont = font.Font(family="Helvetica", size=18, weight="bold")
Helvfont2 = font.Font(family="Helvetica", size=12)
Helvfont3 = font.Font(family="Helvetica", size=14)
Helvfont4 = font.Font(family="Helvetica", size=20)
Helvfont5 = font.Font(family="Helvetica", size=40)
##===================================================================================================
##====================================================================================================

"""TEXTBOX"""
Energia=DoubleVar()
Tension=StringVar()
Corriente=StringVar()

AmplitudECG=StringVar()
FrecuenciaECG=StringVar()

# BoxAmp=Entry(Guide,textvariable=Amplitud).place(x=350,y=100,width = 50)
# BoxFrec=Entry(Guide,textvariable=FrecuenciaM).place(x=350,y=150, width = 50)
 
##====================================================================================================

"""CONFIGURACIÓN BOTONES"""
comenzar=PhotoImage(file="/home/pi/Desktop/Simulador/boton comenzar.png")
Boton=tk.Button(Guide,image=comenzar, width=311,height=85,relief="flat",activeforeground="black",activebackground="black",background="black",foreground="black",highlightthickness=0,bd=0,command=window1).place(x=1499,y=952)
cerrar=PhotoImage(file="/home/pi/Desktop/Simulador/cerrar_inicio.png")
boton=tk.Button(Guide,image=cerrar,command=lambda:Stop("G"),borderwidth=0,relief="flat",activeforeground="#9AE8CA",activebackground="#9AE8CA",background="#9AE8CA",foreground="#9AE8CA",highlightthickness=0,bd=0)
boton.place(x=1812,y=49)

tamaño=65
umbral=0.1

Guide.mainloop()


