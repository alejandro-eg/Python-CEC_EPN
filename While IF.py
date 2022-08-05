# -*- coding: utf-8 -*-
while True:
    contar=input("Ingrese el # hasta el que quiere contar: ")
    if contar=='s' or contar=="salir":
        break
    contar=int(contar)
    contador=1
    while True:
        print(contador)
        contador=contador+1
        if contador>contar:
            break