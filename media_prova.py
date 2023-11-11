nota_atividade_1 = float(input("Digite a primeira nota da atividade:" ))
nota_atividade_2 = float(input("Digite a segunda nota da atividade: "))
nota_atividade_3 = float(input("Digite a terçeira nota da atividade: "))
nota_atividade_4 = float(input("Digite a quarta nota da atividade: "))
nota_prova = float(input(" Digite a nota da prova: "))

media_atividade = (nota_atividade_1 + nota_atividade_2 + nota_atividade_3 \
                   + nota_atividade_4) / 4

media_do_curso = (media_atividade * 0.4) + (nota_prova * 0.6)


print(f"A média das atividades são {media_atividade} e a nota da prova é {nota_prova}\
por tanto a média total é {media_do_curso}")

