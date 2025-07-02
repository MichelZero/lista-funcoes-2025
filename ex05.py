#
# autor: Michel
# data: 28/06/2025

# 05)
# Problema 5: Cálculo do Índice de Massa Corporal (IMC)
# Em linguagem Python, crie um programa que calcula o Índice de Massa 
# Corporal (IMC) de uma pessoa. O programa deve ler o peso da pessoa 
# (em Kg) e a sua altura (em metros). Após calcular o IMC, o 
# programa deve determinar a classificação da pessoa com base na tabela abaixo.
# Fórmula:
# IMC = PESO / (ALTURA ** 2)

# Tabela de Classificação:
#   Abaixo de 18.5: Abaixo do peso
#  Entre 18.5 e 24.9: Peso normal
#  Entre 25.0 e 29.9: Sobrepeso
#  Entre 30.0 e 34.9: Obesidade grau I
#  Acima de 35.0: Obesidade grau II ou superior

# O programa deve apresentar o peso, a altura, o valor do IMC e a sua respectiva classificação.
# OBS: o programa deve conter quatro funções:
# a) Função para ler os dados: não recebe parâmetro e retorna o peso e a altura da pessoa.
# b) Função para calcular o IMC: recebe o peso e a altura como parâmetros e retorna o valor do IMC.
# c) Função para obter a classificação: recebe o valor do IMC como parâmetro e retorna uma string com a classificação (ex: "Peso normal").
# d) Função para apresentar o diagnóstico: recebe o peso, a altura, o IMC e a string de classificação como parâmetros e apenas imprime o resultado.