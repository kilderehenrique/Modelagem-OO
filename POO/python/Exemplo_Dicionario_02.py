from generico.InputNumber import inputNumber

# Construa um dicionário com nome, salariobruto, salario liquido, 
# para número indeterminado de pessoas, nele será calculado o 
# desconto de 8% do INSS e de 10% para IRPF. Preciso que o 
# programa seja escrito na Linguagem Python de forma Otimizada..

def continuar():
    return input("Deseja continuar? (s/n): ") == "s"

def main():
    # Cria um dicionário vazio
    folha_de_pagamento = {}

    # Enquanto agenda vazia e quiser continuar
    while True:
        # Lê o nome e o salário bruto
        nome = input("Digite o nome: ")
        salario_bruto = inputNumber("Digite o salário bruto: ")

        # Calcula o desconto do INSS -> 8%
        desconto_inss = salario_bruto * 0.08

        # Calcula o desconto do IRPF
        if salario_bruto > 1903.98:
            desconto_irpf = salario_bruto * 0.10
        else:
            desconto_irpf = 0

        # Calcula o salário líquido
        salario_liquido = salario_bruto - desconto_inss - desconto_irpf

        # Adiciona os dados ao dicionário
        folha_de_pagamento[nome] = {
            "salario_bruto": salario_bruto,
            "desconto_inss": desconto_inss,
            "desconto_irpf": desconto_irpf,
            "salario_liquido": salario_liquido,
        }

        # Se quiser continuar
        if continuar():
            break;

    # Imprime os itens do dicionário
    print(folha_de_pagamento)

if __name__ == "__main__":
    main()
