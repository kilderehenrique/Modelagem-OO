from generico.InputNumber import inputNumber

def calcDesconto():
    # Solicita número
    preco = inputNumber("Digite o preço:")
    # Solicita número
    desconto = inputNumber("Qual desconto (quantos %)?")

    #  ValorProd * ValorDesc
    return preco * desconto/100

# Printa desconto calculado com 2 casas decimais
print("Desconto: R$ %.2f" %calcDesconto())
