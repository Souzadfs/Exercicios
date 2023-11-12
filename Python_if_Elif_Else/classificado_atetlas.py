from datetime import date

idade_atleta = int(input("Qual é o seu ano de nascimento? "))
ano_atual = date.today().year
idade_atual = ano_atual - idade_atleta

if 16 <= idade_atual <= 18:
    print(f" sua idade é {idade_atual} anos, e você está na categoria JUNIOR !!")
elif 18 < idade_atual <= 29:
    print(f"Sua idade é {idade_atual} anos, e sua categoria é PLENO !!")
elif 29 < idade_atual <= 50:
    print(f"Sua idade é {idade_atual} anos, e sua categoria é SENIOR !!")
elif idade_atual > 50:
    print(f"Sua idade é {idade_atual} anos, e você já esta APOSENTADO !!")    
else:
    print(f"Sua idade é {idade_atual}, e você não tem categoria.")    


