"""
Neste exercício avançado de Python, 
você criará um programa que simula um sistema de controle de acesso a um prédio com diferentes níveis de acesso. 
Cada usuário terá um nível de acesso e só poderá acessar áreas específicas do prédio de acordo com seu nível.
"""

usuarios = {
    1: {"senha": "abc123", "nivel_acesso": "A"},
    2: {"senha": "xyz987", "nivel_acesso": "B"},
    3: {"senha": "mno456", "nivel_acesso": "C"},
    4: {"senha": "abc123", "nivel_acesso": "D"},
}

id_usuario = int(input("Digite seu ID de usuário: "))
senha = input("Digite sua senha: ")

if id_usuario in usuarios and usuarios[id_usuario]["senha"] == senha:
    andar = int(input("Digite o andar que deseja acessar (1-3): "))
    nivel_acesso = usuarios[id_usuario]["nivel_acesso"]

    if andar == 1:
        print("Acesso permitido.")
    elif andar == 2:
        if nivel_acesso == "A" or nivel_acesso == "B":
            print("Acesso permitido.")
        else:
            print("Acesso negado. Nível de acesso insuficiente.")
    elif andar == 3:
        if nivel_acesso == "A":
            print("Acesso permitido.")
        else:
            print("Acesso negado. Nível de acesso insuficiente.")
    else:
        print("Andar inválido.")
else:
    print("ID de usuário ou senha incorretos.")