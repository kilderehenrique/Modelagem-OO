from generico.InputNumber import inputNumber

# Crie um dicionário que é uma agenda e coloque nele os seguintes dados: chave (cpf), 
# nome, idade, telefone. O programa deve ler um número indeterminado de dados, criar a 
# agenda e imprimir todos os itens do dicionário no formato chave: nome, idade, fone.

def continuar():
    return input("Deseja continuar? (s/n): ") == "s"

def main():
    # Cria um dicionário vazio
    agenda = {}

    while True:
        # Lê informações
        cpf = input("Digite o CPF: ")
        nome = input("Digite o nome: ")
        idade = inputNumber("Digite a idade: ", inteiro=True)
        telefone = input("Digite o telefone: ")

        # Adiciona os informações no dicionário
        agenda[cpf] = {
            "nome": nome,
            "idade": idade,
            "telefone": telefone,
        }

        # Se quiser continuar
        if continuar():
            break;

    # Imprime os itens do dicionário
    print(agenda)

if __name__ == "__main__":
    main()
