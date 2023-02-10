import random

def llenar_matriz(n):
  matriz = []
  for i in range(n):
    fila = []
    for j in range(n):
      fila.append(random.randint(1, 100))
    matriz.append(fila)
  return matriz

def main():
  n = int(input("Ingrese la dimensión de la matriz NxN: "))
  matriz = llenar_matriz(n)
  for fila in matriz:
    print(fila)

if __name__ == "__main__":
  main()
