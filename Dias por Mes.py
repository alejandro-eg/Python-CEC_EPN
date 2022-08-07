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


testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = dias_mes(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
