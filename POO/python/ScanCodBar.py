from generico.InputNumber import inputNumber

# Iniciando var precos
precos = [0.5, 1, 4, 7, 8]

def scanCodBar():
    # Iniciando var quantidades compradas
    compra = [0, 0, 0, 0, 0]

    while(True):
        # Solicita número(inteiro) do código
        codProduto = inputNumber("Qual o cod. do produto?", inteiro=True)
        
        # Para de escanear se digitar 0
        if(codProduto == 0):
            break;
        
        # Solicita número(inteiro) da quantidade de produtos
        qtdProduto = inputNumber("qtd do produto", inteiro=True)
        
        # Se código inválido
        if(codProduto < 0 or codProduto >= 5):
            print("Código inválido!")
            break
        
        # Adiciona qtd de produtos a compra
        compra[codProduto] += qtdProduto
    
    # Calcula Total
    total = 0
    for i in range(5):
        total += compra[i] * precos[i]

    return {
        "compra": compra,
        "total": total
    }

# Quarda informações da compra
compra = scanCodBar()
print("Total: ", compra["total"])
