#. Pedir los datos de los alumnos, estos son: sexo, edad y altura. Al final del programa
#se deberá mostrar la cantidad de hombres, la cantidad de mujeres, la altura promedio
#,la cantidad de alumnos que tienen una altura mayor a 1.70 cm, la cantidad de alumnos
#que tiene una altura menor o igual a 1.50 cm. El programa debe finalizar cuando la edad
#sea igual a 0.

import random

rango = 2

total_hombres=0
total_mujeres=0
altura_suma=0
mayor_170=0
menor_150=0

for i in range (rango):
    sexo = input('Cual es su sexo: ')
    if sexo == "masculino":
       total_hombres +=1
    else:
        total_mujeres +=1
    
    edad = int(input('ingrese su edad: '))
    
    altura = int(input('ingrese su altura: '))
    
    if altura >= 170 :
        mayor_170 += 1
    
    elif altura <= 150 :
        menor_150 += 1
        
    altura_suma = altura + altura_suma
    
    if edad == 0 : break
    
altura_promedio = altura_suma / rango
print(f'la altura promedio es {altura_promedio}') 
   
        
print(total_hombres)
print(total_mujeres)
print(f'la altura menor o igual a 150 es: {menor_150}') 
    
    
    
     
        
    
 
    
    

