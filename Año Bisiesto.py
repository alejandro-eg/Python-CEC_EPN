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
    
    
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result =es_bisiesto(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")