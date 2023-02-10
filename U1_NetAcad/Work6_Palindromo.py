import random
def es_palindromo(entrada):
  entrada = entrada.replace(" ", "")
  entrada_reversa = entrada[::-1]
  if entrada == entrada_reversa:
    return True
  else:
    return False

entrada = input("Ingrese una palabra o número: ")

if entrada.isdigit():
  resultado = es_palindromo(entrada)
  if resultado:
    print("La entrada es un número capicúa.")
  else:
    print("La entrada no es un número capicúa.")
else:
  resultado = es_palindromo(entrada)
  if resultado:
    print("La entrada es una palabra palíndromo.")
  else:
    print("La entrada no es una palabra palíndromo.")
