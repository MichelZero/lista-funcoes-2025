#
# autor: Michel
# data: 28/06/2025

# 02)
# 	Em linguagem Python, faça um programa que efetue o cálculo da quantidade de litros de 
# combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. 
# Para realizar o cálculo, o usuário deve fornecer o tempo gasto na viagem e a 
# velocidade média durante ela. Desta forma, será possível obter a distância percorrida 
# com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular
# a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. 
# O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância 
# percorrida e a quantidade de litros utilizada na viagem.
#       OBS: o programa de conter quatro funções:
#	a) Função para ler os valores (não recebe parâmetro e retorna os dois valores);
#	b) Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância);
#	c) Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros);
#	d) Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado).

# -*- coding: utf-8 -*-

def ler_valores():
    """
    Lê o tempo e a velocidade da viagem inseridos pelo usuário.
    Não recebe parâmetros.
    Retorna:
        tuple: Uma tupla contendo o tempo (float) e a velocidade (float).
    """
    # Loop para garantir que o usuário digite um tempo válido
    while True:
        try:
            tempo = float(input("Digite o tempo gasto na viagem (em horas): "))
            if tempo >= 0:
                break  # Sai do loop se o valor for válido
            else:
                print("O tempo não pode ser negativo. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    # Loop para garantir que o usuário digite uma velocidade válida
    while True:
        try:
            velocidade = float(input("Digite a velocidade média (em Km/h): "))
            if velocidade >= 0:
                break  # Sai do loop se o valor for válido
            else:
                print("A velocidade não pode ser negativa. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    
    return tempo, velocidade


def calcular_distancia(tempo, velocidade):
    """
    Calcula a distância percorrida com base no tempo e na velocidade.
    Parâmetros:
        tempo (float): O tempo gasto na viagem.
        velocidade (float): A velocidade média.
    Retorna:
        float: A distância total percorrida.
    """
    distancia = tempo * velocidade
    return distancia


def calcular_litros(distancia):
    """
    Calcula a quantidade de litros de combustível gastos.
    O carro faz 12 Km por litro.
    Parâmetros:
        distancia (float): A distância total percorrida.
    Retorna:
        float: A quantidade de litros de combustível utilizados.
    """
    litros_usados = distancia / 12
    return litros_usados


def apresentar_resultado(velocidade, tempo, distancia, litros):
    """
    Exibe todos os dados da viagem de forma formatada.
    Parâmetros:
        velocidade (float): A velocidade média.
        tempo (float): O tempo gasto.
        distancia (float): A distância percorrida.
        litros (float): A quantidade de litros consumidos.
    """
    print("\n--- Resumo da Viagem ---")
    print(f"Velocidade média: {velocidade:.2f} Km/h") # .2f formata o número com duas casas decimais
    print(f"Tempo gasto: {tempo:.2f} horas")
    print(f"Distância percorrida: {distancia:.2f} Km")
    print(f"Litros de combustível consumidos: {litros:.2f} L")


# --- Bloco Principal do Programa ---
# Orquestra a execução, chamando cada função na ordem correta.
if __name__ == "__main__":
    # 1. Chama a função para ler os valores de entrada e os armazena em variáveis
    tempo_gasto, velocidade_media = ler_valores()

    # 2. Chama a função de cálculo da distância, passando os valores lidos
    distancia_percorrida = calcular_distancia(tempo_gasto, velocidade_media)

    # 3. Chama a função de cálculo de litros, passando a distância calculada
    litros_consumidos = calcular_litros(distancia_percorrida)

    # 4. Chama a função para exibir o resultado final, passando todos os valores
    apresentar_resultado(velocidade_media, tempo_gasto, distancia_percorrida, litros_consumidos)