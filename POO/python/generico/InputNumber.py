def inputNumber(frase, inteiro=False):
    # Pega input
    value = input(f"{frase} ")

    # Pede novo input
    # Enquanto (não for número) ou (precisa de inteiro E não é inteiro)
    while(not value.isnumeric or (inteiro and float(value)%1 != 0)):
        # Frase notificação
        print("Digite um número", " inteiro!" if inteiro else "!")
        # Pega input
        value = input(f"{frase} ")
    
    # Converte para número
    value = float(value)

    # Converte para inteiro
    # Se precisar de inteiro
    return int(value) if inteiro else value

def inputNumberArray(nomeUnidade, qtd= None, inteiro=False):
    # Array de resposta
    values = []
    
    #Se não tiver qtd informada
    if qtd == None:
        # Informe a quantidade
        qtd = int(inputNumber(f"Qual a quantidade de {nomeUnidade}s?"), inteiro)
    
    # Solicita números
    for i in range(qtd):
        # Solicita número, inteiro se precisar
        num = inputNumber(f"Digite {nomeUnidade}{i+1}:", inteiro)
        # Adiciona número
        values.append(num)
    
    return values
