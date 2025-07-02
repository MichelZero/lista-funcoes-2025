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
# SALARIO_BRUTO = HORAS_TRABALHADAS * VALOR_HORA
# DESCONTO_IR = SALARIO_BRUTO * 0.11
# DESCONTO_INSS = SALARIO_BRUTO * 0.08
# SALARIO_LIQUIDO = SALARIO_BRUTO - DESCONTO_IR - DESCONTO_INSS

# O programa deve apresentar um resumo (holerite) contendo o salário bruto, o
# valor descontado do IR, o valor descontado do INSS e o salário líquido final.

# OBS: o programa deve conter quatro funções:
# a) Função para ler os dados de trabalho: não recebe parâmetros e retorna as horas trabalhadas e o valor por hora.
# b) Função para calcular o salário bruto: recebe as horas e o valor por hora como parâmetros e retorna o salário bruto.
# c) Função para calcular os descontos e o salário líquido: recebe o salário bruto como parâmetro e retorna os três valores calculados (desconto do IR, desconto do INSS e salário líquido).
# d) Função para apresentar o holerite: recebe todos os valores relevantes (salário bruto, descontos, salário líquido) e apenas imprime o resultado formatado.

def ler_dados_trabalho():
    """
    Função para ler os dados de trabalho.
    Não recebe parâmetros e retorna as horas trabalhadas e o valor por hora.
    """
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
    valor_hora = float(input("Digite o valor que recebe por hora (R$): "))
    return horas_trabalhadas, valor_hora

def calcular_salario_bruto(horas, valor_hora):
    """
    Função para calcular o salário bruto.
    Recebe as horas e o valor por hora como parâmetros e retorna o salário bruto.
    """
    salario_bruto = horas * valor_hora
    return salario_bruto

def calcular_descontos_e_salario_liquido(salario_bruto):
    """
    Função para calcular os descontos e o salário líquido.
    Recebe o salário bruto como parâmetro e retorna os três valores calculados
    (desconto do IR, desconto do INSS e salário líquido).
    """
    desconto_ir = salario_bruto * 0.11
    desconto_inss = salario_bruto * 0.08
    salario_liquido = salario_bruto - desconto_ir - desconto_inss
    return desconto_ir, desconto_inss, salario_liquido

def apresentar_holerite(salario_bruto, desconto_ir, desconto_inss, salario_liquido):
    """
    Função para apresentar o holerite.
    Recebe todos os valores relevantes (salário bruto, descontos, salário líquido)
    e apenas imprime o resultado formatado.
    """
    print("\n" + "="*50)
    print("                  HOLERITE")
    print("="*50)
    print(f"Salário Bruto:        R$ {salario_bruto:.2f}")
    print(f"Desconto IR (11%):    R$ {desconto_ir:.2f}")
    print(f"Desconto INSS (8%):   R$ {desconto_inss:.2f}")
    print("-"*50)
    print(f"Salário Líquido:      R$ {salario_liquido:.2f}")
    print("="*50)

def main():
    """
    Função principal que coordena a execução do programa.
    """
    print("=== CÁLCULO DE SALÁRIO LÍQUIDO ===\n")
    
    # Ler dados de trabalho
    horas, valor_hora = ler_dados_trabalho()
    
    # Calcular salário bruto
    salario_bruto = calcular_salario_bruto(horas, valor_hora)
    
    # Calcular descontos e salário líquido
    desconto_ir, desconto_inss, salario_liquido = calcular_descontos_e_salario_liquido(salario_bruto)
    
    # Apresentar holerite
    apresentar_holerite(salario_bruto, desconto_ir, desconto_inss, salario_liquido)

if __name__ == "__main__":
    main()