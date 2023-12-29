frase = str(input('Digite uma frase: ')).strip(). upper()
palavra = frase.split()
juntar = '*'.join((palavra))
inverter = ''

for letras in range(len(juntar) - 1, -1, -1):
    inverter += juntar[letras]
if inverter == juntar:
    print(f'{juntar}')
    print(f' A palavra digita, {inverter} é um PALINDROMO')
else:
    print(f'{juntar}')
    print(f' A palavra digita invertida {inverter}, não é um PALINDROMO')  

