#
# autor: Michel
# data: 28/06/2025

# 01)
# 	 Em linguagem Python, faça um programa que lê uma temperatura em graus Celsius e, em seguida, 
# apresente-a convertida em graus Fahrenheit. A fórmula de conversão é F = (9 * C + 160) / 5, 
# na qual F é a temperatura em Fahrenheit e C é a temperatura em graus Celsius.
    # OBS: o programa deve conter três funções:
# a)  	Função para ler e retorna o valor da temperatura (não recebe parâmetro);
#	b)    Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius);
#	c)    Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão.

# -*- coding: utf-8 -*-

def ler_temperatura():
    """
    Lê a temperatura em graus Celsius inserida pelo usuário.
    Não recebe parâmetros.
    Retorna:
        float: A temperatura em graus Celsius.
    """
    # Usamos um loop para garantir que o usuário digite um número válido
    while True:
        try:
            celsius = float(input("Digite a temperatura em graus Celsius: "))
            return celsius
        except ValueError:
            print("Erro: Por favor, digite um valor numérico válido.")


def calcular_fahrenheit(celsius):
    """
    Converte a temperatura de Celsius para Fahrenheit usando a fórmula.
    Parâmetros:
        celsius (float): A temperatura em graus Celsius.
    Retorna:
        float: A temperatura convertida em graus Fahrenheit.
    """
    fahrenheit = (9 * celsius + 160) / 5
    return fahrenheit


def mostrar_resultado(fahrenheit):
    """
    Exibe o resultado da conversão de forma formatada.
    Parâmetros:
        fahrenheit (float): O valor da temperatura em Fahrenheit.
    """
    # Usamos :.2f para formatar o número com duas casas decimais
    print(f"\nA temperatura convertida é: {fahrenheit:.2f}°F")


# --- Bloco Principal do Programa ---
# Esta é a parte que orquestra a chamada das funções.
if __name__ == "__main__":
    # 1. Chama a função para ler o valor de entrada
    temp_celsius = ler_temperatura()

    # 2. Chama a função de cálculo, passando o valor lido como parâmetro
    temp_fahrenheit = calcular_fahrenheit(temp_celsius)

    # 3. Chama a função para exibir o resultado final
    mostrar_resultado(temp_fahrenheit)