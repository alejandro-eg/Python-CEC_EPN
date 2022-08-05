# -*- coding: utf-8 -*-
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
ciudad = input("Ingrese la ciudad donde vive: ")
space= " "
if  edad ==0 or edad <=5:
    msg="Es un niño"
elif edad ==6 or edad <=17:
    msg="Es un adolescente"
elif edad ==18 or edad <=64:
    msg="Es un adulto"
elif edad>=65:
    msg="Es un adulto mayor"
else:
    msg="Edad NO Válida"
print("Nombre: "+nombre+space+"Apellido: "+apellido+space+"Edad: "
+(str(edad)+space+msg+space+"Ciudad: "+ciudad))