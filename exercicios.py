casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite seu salario: "))
qtd_ano = float(input("Quantidade de anos: "))

qtd_parc = qtd_ano * 12

parc_casa = casa / qtd_parc

ret = 0.3 * salario

porc = (parc_casa / salario) * 100

if parc_casa <= ret:
    print(f' Aprovado a parcela da casa é {parc_casa:.2f}')
    print(f'A parcela é referente {porc :.2f}% do seu salario')
    print(f'Quantidade será de {qtd_parc} parcelas ou {qtd_ano:.0f} anos.')
else:
    print(f'O emprestimo foi negado a parcela de {parc_casa:.2f} excedeu os 30% do seu salario sendo {porc:.2f}% do seu salario.')
