"""
Crie um programa em Python que solicite ao usuário a sua idade e informe se ele é menor de idade, adulto ou idoso. As regras para classificar a idade são as seguintes:

Menor de idade: idade inferior a 18 anos.
Adulto: idade entre 18 e 59 anos, inclusive.
Idoso: idade igual ou superior a 60 anos.
O programa deve realizar as seguintes tarefas:

Peça ao usuário que insira sua idade.
Verifique em qual categoria de idade o usuário se encaixa, usando if, elif e else.
Exiba uma mensagem informando se o usuário é menor de idade, adulto ou idoso.

"""

idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Você é menor de idade.")
elif 18 <= idade <= 59:
    print("Você é adulto.")
else:
    print("Você é idoso.")