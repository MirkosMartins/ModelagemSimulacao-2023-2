# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 10:21:18 2023

@author: mirkos@gmail.com - Mirkos O. Martins  
"""
clientes = [7,20,4,49,7,25]
vAt1=3
vAt2=2
t1=0
t2=0
def atende():
    global t1,t2
    nrClientes=len(clientes)
    t0=clientes[0]/vAt1
    for i in range(len(clientes)):
        if(t1<=t2):
            t1+=clientes[i]/vAt1
        else:
            t2+=clientes[i]/vAt2
    if t1>t2:
        return t1
    else:
        return t2
print(atende())
