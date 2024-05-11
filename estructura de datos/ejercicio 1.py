#Leer 20 números e imprimir cuantos son positivos, negativos y cuantos neutros
positivos=0
negativos=0
neutros=0

for i in range (-10, 11): #solicitud de 20 numeros 
    if i < 0: #evaluar numeros negativos
        negativos +=1 #incrementar los negativos
    elif i == 0: #evaluar nemeros neutros 
        neutros +=1 #incrementar los neutros 
    else: #evaluar los numeros positivos 
        positivos+=1 #incrementar los positivos 
    
print (f'{negativos} son negativos') 
print (f'{positivos}son positivos')
print (f'{neutros}son neutros')
    