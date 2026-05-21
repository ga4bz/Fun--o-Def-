def inverter(texto):
    invertido = ""

    for i in range(len(texto) - 1, -1, -1):
        invertido += texto[i]

    return invertido

def main():
    texto = input("Digite um texto: ")

    resultado = inverter(texto)
    print(resultado)

main()