"""Escreva um programa em Python que solicite ao usuário que insira três notas e seus respectivos pesos e, em seguida, calcule a média ponderada das notas.
O programa deve verificar se a soma dos pesos é igual a 100%. Se a soma dos pesos for diferente de 100%, o programa deve exibir uma mensagem de erro. 
Caso contrário, o programa deve calcular e exibir a média ponderada das notas e exibir uma mensagem de aprovação se a média for maior ou igual a 7, 
uma mensagem de recuperação se a média for maior ou igual a 5 e menor do que 7, ou uma mensagem de reprovação se a média for menor do que 5. 
O programa deve usar a estrutura if, else e elif para verificar a soma dos pesos e a média ponderada das notas."""


nota1 = float(input("Digite a primeira nota: "))
peso1 = float(input("Digite o peso da primeira nota (em porcentagem): "))
nota2 = float(input("Digite a segunda nota: "))
peso2 = float(input("Digite o peso da segunda nota (em porcentagem): "))
nota3 = float(input("Digite a terceira nota: "))
peso3 = float(input("Digite o peso da terceira nota (em porcentagem): "))

if peso1 + peso2 + peso3 != 100:
    print("Erro: a soma dos pesos deve ser igual a 100%.")
else:
    media = (nota1*peso1/100) + (nota2*peso2/100) + (nota3*peso3/100)

    if media >= 7:
        print(f"Parabéns! Sua média ponderada é {media} e você foi aprovado.")
    elif media >= 5:
        print(f"Sua média ponderada é {media} e você está em recuperação.")
    else:
        print(f"Sua média ponderada é {media} e você foi reprovado.")
