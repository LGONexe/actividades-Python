# Escribir un programa que multiplique los 20 primeros números naturales. Ejemplo:
# (1*2*3*4*5…)
import random

resultado = 1

for i in range (1,21):
    resultado =resultado*i
    
print ("el resultado de multiplicar los primeros 20 numeros naturales es: " , resultado )
    
    