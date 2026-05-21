def maior_elemento(lista):
    return max(lista)

def receber_numeros():
    lista = [0] * 5
    for i in range(len(lista)):
        lista[i] = int(input(f"Digite um número({i+1}/{len(lista)}): "))
    return lista

def main():
    lista = receber_numeros()
    resultado = maior_elemento(lista)

    print(f"O maior número é {resultado}")

main()