import array
import os
import time
import math
#secret_number = int(input("Ingresa el numero secreto: "))
secret_number=777
while True:
    num = int(input("Ingresa un numero para verificar que es igual al que buscamos: "))
    if num==secret_number:
        print("Bingo")
        break;
    elif num<secret_number:
        print("Subele")
    elif num>secret_number:
        print("Bajale")
