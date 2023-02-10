import array
import os
import time
import math
ticket = int(input("Ingresa la cantidad de dinero que tiene para los boletos: "))
suma=0
c=0
while True:
    c+=1
    if ticket>=c:
        suma=suma+c
    elif ticket<c:
        print("Es todo")
        break
print("La total de la suma fue: ",suma)
print("Los tickets que se ajustaron fue: ",c-1)
