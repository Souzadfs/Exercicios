from datetime import date

idade_atleta = int(input("Qual é o seu ano de nascimento? "))
ano_atual = date.today().year
idade_atual = ano_atual - idade_atleta

if 12 <= idade_atual <= 15:
    print(f"sua idade é {idade_atual} anos, e você está na categoria MIRIM ! ")   
elif 16 < idade_atual <= 20:
    print(f" sua idade é {idade_atual} anos, e você está na categoria JUNIOR !!")
elif 20 < idade_atual <= 29:
    print(f"Sua idade é {idade_atual} anos, e sua categoria é PLENO !!")
elif 29 < idade_atual <= 40:
    print(f"Sua idade é {idade_atual} anos, e sua categoria é SENIOR !!")
elif idade_atual > 40:
    print(f"Sua idade é {idade_atual} anos, e você já esta MASTER !!")    
else:
    print(f"Sua idade é {idade_atual}, e você não tem categoria.")    


