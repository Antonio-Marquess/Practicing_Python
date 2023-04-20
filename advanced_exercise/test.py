import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Função para verificar se um número é primo
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Função para extrair características dos sorteios
def extrair_caracteristicas(sorteio):
    primos = [n for n in sorteio if eh_primo(n)]
    pares = [n for n in sorteio if n % 2 == 0]
    impares = [n for n in sorteio if n % 2 == 1]
    
    return [
        len(primos),
        len(pares),
        len(impares),
        np.mean(sorteio),
        np.median(sorteio),
        np.std(sorteio)
    ]

# Função para preparar os dados
def preparar_dados(historico_sorteios):
    X, y = [], []
    
    for sorteio in historico_sorteios:
        X.append(extrair_caracteristicas(sorteio[:-1]))
        y.append(sorteio[-1])
        
    return np.array(X), np.array(y)

# Função principal
def main():
    historico_sorteios = np.array([
        # Exemplos de sorteios passados (cada linha representa um sorteio)
        [3, 7, 19, 24, 32, 48],
        [8, 15, 22, 28, 33, 46],
        # ...
    ])
    
    # Preparar os dados
    X, y = preparar_dados(historico_sorteios)
    
    # Treinar o modelo
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X, y)
    
    # Prever o próximo sorteio (exemplo de entrada)
    proximo_sorteio = [1, 10, 20, 30, 40]
    caracteristicas_proximo_sorteio = extrair_caracteristicas(proximo_sorteio)
    previsao = modelo.predict([caracteristicas_proximo_sorteio])
    
    print("Número previsto:", previsao[0])

if __name__ == "__main__":
    main()