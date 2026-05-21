def soma_elementos(lista):
    soma = 0

    for numero in lista:
        soma += numero
    
    return soma

def receber_numeros():
    quantidade = int(input("Quantos números você quer adicionar na lista?: "))

    lista = []

    for i in range(quantidade):
        numero = int(input(f"Digite um número ({i + 1}/{quantidade}): "))
        lista.append(numero)

    return lista

def main():
    lista = receber_numeros()
    resultado = soma_elementos(lista)

    print(f"Soma = {resultado}")

main()