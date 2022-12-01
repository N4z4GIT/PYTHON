# Escribir un programa que muestre en pantalla los numeros del 1 al 100.
# Sustituyendo los multiplos de 3 por la palabra "Fizz", los múltiplos 
# de 5 por la palabra "Buzz" y los múltiplos de ambos, es decir, los 
# múltiplos de 3 y 5 (o de 15), por la palabra "FizzBuzz". 
# TU CODIGO AQUI:

for number in range (1,101):
    if (number % 15==0):
        print("FizzBuzz")
    elif(number % 3==0):
        print("Fizz")
    elif(number % 5==0):
        print("Buzz")
    else:
        print(number)