from datetime import date

nome = input('Digite seu nome: ')
ano_nasc = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
idade_atual =  18 - idade

if idade >= 18:
    print(f'Parabens sua idade é {idade} e vôce está alistado !')
elif idade < 18:
    print(f'Alistamento negado sua idade é {idade} e ainda {idade_atual} anos.' )