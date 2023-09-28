from generico.InputNumber import inputNumberArray

# Calcula media por um array(lista) de notas 
def calcMedia(notas):
    # Inicia com primeira nota
    soma = notas[0]
    # qtd de notas
    qtdN = len(notas)

    for n in notas[1:]:
        soma += n

    # Calcula e retorna media
    return soma/qtdN

print("Média: %.1f" %calcMedia(inputNumberArray("nota")))
