import math

def calcular_parcela(valor_total, num_parcelas, taxa_juros):

    taxa_juros = taxa_juros / 100
    numerador = valor_total * taxa_juros * (1 + taxa_juros)**num_parcelas
    denominador = (1 + taxa_juros)**num_parcelas - 1
    parcela = numerador / denominador
    return parcela

def calcular_taxa_juros(montante, valor_total, tempo):
    taxa_juros = (montante / valor_total) ** (1 / tempo) - 1
    return taxa_juros * 100

def calcular_tempo(montante, valor_total, taxa_juros):
    taxa_juros = taxa_juros / 100
    tempo = math.log(montante / valor_total) / math.log(1 + taxa_juros)
    return tempo

while True:
    print("--------------------------------")
    print("|CALCULADORA DE JUROS COMPOSTOS|")
    print("--------------------------------")

    print("Escolha a operação:")
    print("1. Calcular valor futuro e parcelas")
    print("2. Calcular taxa de juros")
    print("3. Calcular tempo")
    opcao = input("Digite o número da opção: ")

    if opcao == '1':
        vt = float(input("Qual o valor total que deseja financiar? R$"))
        p = int(input("Qual a quantidade de prestações? "))
        j = float(input("Qual a taxa de juros ao mês? "))
        M = vt * (1 + (j / 100)) ** p
        parcela = calcular_parcela(vt, p, j)
        print(f"O valor total do financiamento será: R${M:.2f}")
        print(f"O valor de cada parcela será: R${parcela:.2f}")
    elif opcao == '2':
        vt = float(input("Qual o valor inicial? R$"))
        M = float(input("Qual o valor final? R$"))
        t = int(input("Qual o tempo em meses? "))
        j = calcular_taxa_juros(M, vt, t)
        print(f"A taxa de juros é de {j:.2f}% ao mês.")
    elif opcao == '3':
        vt = float(input("Qual o valor inicial? R$"))
        M = float(input("Qual o valor final? R$"))
        j = float(input("Qual a taxa de juros ao mês? "))
        t = calcular_tempo(M, vt, j)
        print(f"O tempo necessário é de {t:.0f} meses.")
    else:
        print("Opção inválida.")

    continuar = input("Deseja realizar outro cálculo? (s/n): ")
    if continuar.lower() != 's':
        break