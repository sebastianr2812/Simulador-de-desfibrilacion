import numpy as np

def Norm(Max,Min,Signal):
    Norma=np.zeros([len(Signal),1],dtype=np.float64)
    for j in range(0,len(Signal)):
        Norma[j]=8*(Signal[j])+127

    return Norma