"""Programa para saber si el numero es Par o Impar"""

print("_____________________________________________________")
print("---Programa para saber si el numero es Par o Impar---")
print("_____________________________________________________")

# input
 
X=int(input(" Ingrese el numero: " ))

# processing

if X % 2 == 0:
    msj = "es par ";

else:
    msj = " es impar ";

# output

print(" el Numero que digito: " + msj )