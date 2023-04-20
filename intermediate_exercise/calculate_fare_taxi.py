"""
Você foi contratado para criar um programa em Python que calcula a tarifa de um táxi com base na distância percorrida e no horário do dia. As regras para calcular a tarifa são as seguintes:

A tarifa inicial é de R$ 5,00.
A tarifa por quilômetro é de R$ 2,00.
Entre 22h e 6h, há um adicional noturno de 20% sobre o valor total da corrida (exceto a tarifa inicial).
O programa deve realizar as seguintes tarefas:

Peça ao usuário que insira a distância percorrida em quilômetros.
Peça ao usuário que insira o horário do início da corrida no formato 24 horas (ex: 14, 23, 6).
Calcule a tarifa base usando a distância percorrida e a tarifa por quilômetro.
Verifique se a corrida ocorreu durante o horário noturno (entre 22h e 6h) usando if, elif e else.
Caso a corrida tenha ocorrido no horário noturno, adicione o adicional noturno à tarifa base.
Some a tarifa inicial ao valor calculado e informe ao usuário o valor total da corrida.

"""

tarifa_inicial = 5
tarifa_por_km = 2

distancia = float(input("Digite a distância percorrida em quilômetros: "))
hora = int(input("Digite a hora do início da corrida no formato 24 horas (ex: 14, 23, 6): "))

tarifa_base = distancia * tarifa_por_km

if 22 <= hora < 24 or 0 <= hora < 6:
    adicional_noturno = tarifa_base * 0.20
    tarifa_base += adicional_noturno

tarifa_total = tarifa_inicial + tarifa_base
print(f"O valor total da corrida é R$ {tarifa_total:.2f}.")
