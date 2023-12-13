soma = 0
cont = 0

for c in range(1, 7):
    num = int(input(f'Digite um valor {c}°: ' ))
    soma = num + soma
    cont = cont +1

print(f'{cont, soma}')