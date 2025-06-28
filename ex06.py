#
# autor: Michel
# data: 28/06/2025

# 06)
# Problema 6: Cálculo de Salário Líquido
#Em linguagem Python, faça um programa que calcule o salário de um funcionário. 
# O programa deve ler o número de horas trabalhadas no mês e o valor 
# que ele recebe por hora. A partir disso, calcule o salário bruto. Em 
# seguida, calcule os descontos: 11% para o Imposto de Renda e 8% para 
# o INSS, ambos sobre o salário bruto. Por fim, calcule o salário líquido.
#Fórmulas:
SALARIO_BRUTO = HORAS_TRABALHADAS * VALOR_HORA
DESCONTO_IR = SALARIO_BRUTO * 0.11
DESCONTO_INSS = SALARIO_BRUTO * 0.08
SALARIO_LIQUIDO = SALARIO_BRUTO - DESCONTO_IR - DESCONTO_INSS

# O programa deve apresentar um resumo (holerite) contendo o salário bruto, o
# valor descontado do IR, o valor descontado do INSS e o salário líquido final.

# OBS: o programa deve conter quatro funções:
# a) Função para ler os dados de trabalho: não recebe parâmetros e retorna as horas trabalhadas e o valor por hora.
# b) Função para calcular o salário bruto: recebe as horas e o valor por hora como parâmetros e retorna o salário bruto.
# c) Função para calcular os descontos e o salário líquido: recebe o salário bruto como parâmetro e retorna os três valores calculados (desconto do IR, desconto do INSS e salário líquido).
# d) Função para apresentar o holerite: recebe todos os valores relevantes (salário bruto, descontos, salário líquido) e apenas imprime o resultado formatado.