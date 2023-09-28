from generico.InputNumber import inputNumber

def tempoPerdido(quantos_por_dia, qtdAnos):
    #               unidade min
    tempo_por_cigarro = 10

    #         (365 dias/ano) + (1 dia por bisexto              )
    qtdDias = (qtdAnos * 365 + round((qtdAnos / 4) - 0.5, 0))
    qtdCigarros = qtdDias * quantos_por_dia
    
    qtdMPerdidos = qtdCigarros * tempo_por_cigarro
    qtdHPerdidas = qtdMPerdidos / 60
    qtdDPerdidos = qtdHPerdidas / 24

    return round(qtdDPerdidos, 1)

# Solicita quantos fumados por dia
qpDia = inputNumber("Quantos por dia:", inteiro=True)
# Solicita quantos anos fumando
qAnos = inputNumber("Quantos anos:", inteiro=True)

# Printa resultado calculado por tempoPerdido()
print("Dias perdidos:", tempoPerdido(qpDia, qAnos))
