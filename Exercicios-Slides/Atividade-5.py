def inverter(texto):
    return texto[::-1]

def main():
    texto = input("Digite um texto: ")

    resultado = inverter(texto)
    print(resultado)

main()