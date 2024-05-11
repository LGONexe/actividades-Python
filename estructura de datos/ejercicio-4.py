#Calcular e imprimir la tabla de multiplicar de un número cualquiera, el cual se
#digitará por teclado. Imprimir el multiplicando, el multiplicador y el producto.

valor = int(input('que valor deseas multiplicar')) #solicita el valor a multiplicar 

for i in range(1,11):
    
    result = valor * i #realiza la multiplicacion 
    print(f'{valor} x {i} = {result}')