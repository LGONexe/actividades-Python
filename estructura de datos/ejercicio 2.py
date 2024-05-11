#Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos numeros
suma=0

for i in range (-10,0): #poner diez numeros negativos
    i *= -1 #convertir los numeros negaivos a positivos 
    print (i) #mostrar los numeros 
    suma += i #sumar los numeros e incremertarlos al contador 
    
print (suma)