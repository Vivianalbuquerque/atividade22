# Exercício Python 22: Faça um programa que mostre na tela os numeros pares entre 1 e 50 (dica estude range e seus paramentros)
numeros = list(range(1,51))
for pares in numeros:
    if pares % 2 == 0:
        print(f'{pares}')