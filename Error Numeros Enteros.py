# -*- coding: utf-8 -*-
def validarNum(men, nmin, nmax):
    while (True):
        try:
            print("Ingrese un valor entre ",nmin," y ",nmax)
            num = int(input(men))
            assert num >= nmin and num <= nmax
            return num
        
        except ValueError:
            print("Ingresar solo numeros")
        except:
            print("Error, el valor debe estar dentro del RANGO ")
    
n = validarNum("Ingrese un valor en el rango:", -100, 100)

print("El número es:", n)
