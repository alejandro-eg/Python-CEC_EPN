# -*- coding: utf-8 -*-
def es_bisiesto(anio):
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False
    
    
def dias_mes(anio, mes):
    diasMes = [31,28,31,30,31,30,31,31,30,31,30,31]
    if es_bisiesto(anio):
        if diasMes[mes - 1] == 28:
            return 29
        else:
            return diasMes[mes - 1]
    else:
        return diasMes[mes - 1]
    return None

def dias_anio(anio,mes,dia):
    diastotales = 0
    if ((mes > 12) | (mes<1) | (dia>dias_mes(anio,mes)) | (dia<1)):
        return None
    for x in range (mes-1):
        diastotales += dias_mes(anio,x+1)
    diastotales += dia
    return(diastotales)
print(dias_anio(2022, 8, 7))