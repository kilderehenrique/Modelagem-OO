from generico.InputNumber import inputNumber, inputNumberArray

# Solicita array de números tamanho 8
v = inputNumberArray("número", qtd=8)

def calcSoma():
    # Solicita número inteiro
    x = inputNumber("Valor X:", inteiro=True)
    # Solicita número inteiro
    y = inputNumber("Valor Y:", inteiro=True)

    # Se posicao x inválida
    if x < 0 or x > 7:   
        print("Posição X inválida!")
        return None
    
    # Se posicao y inválida
    if y < 0 or y > 7:
        print("Posição Y inválida!")
        return None

    return v[x] + v[y] 

print("Soma:", calcSoma())
