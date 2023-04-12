""" Escreva um programa em Python que solicite ao usuário para digitar um número e, em seguida,
verifique se o número é positivo, negativo ou zero. Se o número for positivo, o programa deve 
exibir a mensagem "O número é positivo." Se o número for zero, o programa deve exibir a mensagem 
"O número é zero." Se o número for negativo, o programa deve exibir a mensagem "O número é negativo." 
O programa deve usar a estrutura if, else e elif para verificar o valor do número. """

nun = int(input("Digite um número: "))

if nun > 0:
    print("O número é positivo.")
elif nun == 0:
    print("O número é zero.")
else:
    print("O número é negativo.")