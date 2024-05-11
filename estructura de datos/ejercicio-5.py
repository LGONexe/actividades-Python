# Una persona debe realizar un muestreo con 50 personas para determinar el
# promedio de peso de los niños, jóvenes, adultos y ancianos que existen en su zona. 
import random

# NIÑOS
sumaNiños = 0
numNiños = 0

#JOVENES
sumaJovenes = 0
numJovenes = 0

#ADULTOS
sumaAdultos = 0
numAdultos = 0

#ANCIANOS
sumaAncianos = 0
numAncianos = 0

for i in range(50):

    edad = random.randint(1,70)

    pesoNiños = random.randint(30, 45)
    pesoJoven = random.randint(45, 60)
    pesoAdulto = random.randint(50, 70)
    pesoAnciano = random.randint(40, 65)

    if edad <= 12 :
        sumaNiños += pesoNiños
        numNiños += 1
    elif edad >= 13 and i <= 29:
        sumaJovenes += pesoJoven
        numJovenes += 1
    elif edad >= 30 and i <= 59:
        sumaAdultos += pesoAdulto
        numAdultos += 1
    else:
        sumaAncianos += pesoAnciano
        numAncianos += 1


promedioNiños = int(sumaNiños / numNiños)
promedioJovenes = int(sumaJovenes / numJovenes)
promedioAdultos = int(sumaAdultos / numAdultos)
promedioAncianos = int(sumaAncianos / numAncianos)

print(f'el peso promedio de los niños es: {promedioNiños} kg');
print(f'el peso promedio de los jovenes es: {promedioJovenes} kg');
print(f'el peso promedio de los adultos es: {promedioAdultos} kg');
print(f'el peso promedio de los ancianos es: {promedioAncianos} kg');

