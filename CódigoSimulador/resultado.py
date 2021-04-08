import lut as lut
from scipy import signal
import numpy as np
def analizador(total_time,y):
    primera=y
    rl=66
    fs=1/total_time                                     
    T2= 1/fs
    print(fs)
    f0=60
    Q=1000
    w0=f0/(fs/2)
    b,a = signal.iirnotch(w0,Q)
    yf= signal.filtfilt(b,a,y)
    yv=np.array(yf)
    yv=yv-yv[1]
    x=yv
    t=np.arange(0,len(x)/fs,1/fs)
    t2=t-t[19]
    comp=len(t2)-len(yv)
    if comp>0:
        t2=t2[0:len(yv)]
    elif comp<0:
        yv=yv[0:len(t2)]
    
    Yf=[]
    for i in range(len(yv)):
        if yv[i] < 0.0028102:
            y=0
       
        else:
            y = -177.48*x[i]**6 + 1586.1*x[i]**5 - 5275.8*x[i]**4 + 7977.7*x[i]**3 - 5308.6*x[i]**2 + 1842.5*x[i] - 5.1359
        Yf.append(y)
    y=np.array(Yf)
    xi=np.append(y[0:44],y[44:58]*-1)
    plot=np.append(xi,y[58:])
    V=np.amax(y)
    rl=lut.resL(V)
    E= np.trapz(np.array(y[25:])**2/rl,t2[25:])
    I=V/50
    print(E)
    np.savetxt("test.txt",primera)
    np.savetxt("test2.txt",t2)
    return E, I, V, t2, plot
def cardiov(i):
    ind=0
    print("i: {}".format(i))
    print(type(i))
    if i>=3222:
        ind=i-3222
    elif 3222>i>=1908:
        ind=i-1908
    elif 1908>i>=810:
        ind=i-810
    return ind
    