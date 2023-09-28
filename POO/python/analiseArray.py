from generico.InputNumber import inputNumber, inputNumberArray

# Pega 10 números
v = inputNumberArray("número", qtd=10)
#v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def ver():
    # Iniciando vars
    menor = v[0]
    maior = v[0]
    soma = 0
    maiorIgual5 = 0

    # Percorre vetor
    for num in v[1:]:
        # Verifica se maior ou menor
        if(num > maior):
            maior = num
        elif(num < menor):
            menor = num
        
        # Verifica se >= 5
        if(num >= 5):
            maiorIgual5 += 1

        # Incrementa soma
        soma += num
    
    # Monta dicionário
    return {
        "menor": menor,
        "maior": maior,
        "soma": soma,
        "media": soma/10,
        "maiorIgual5": maiorIgual5,
    }
        
# Percorre dicionário e printa chave: valor
for key, value in ver().items():
    print(f"{key}: {value}")