cont = 0
soma = 0
for c in range( 1 , 3):
    ano_nasc = int(input(f'Digite o ano de nascimento : {c}° '))
    soma = ano_nasc + soma
    cont = cont + 1
    if ano_nasc >= 2010:
        print(f'{ano_nasc} é jovem')
    else:
        print(f'{ano_nasc} é velho')    
    print(ano_nasc, soma)