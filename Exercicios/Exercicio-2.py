def inverter(texto):
    return texto[::-1]

def e_palindromo(texto):
    texto_invertido = inverter(texto)

    if texto == texto_invertido:
        return True
    else:
        return False
    
def main():
    palavra = input("Digite uma palavra e veja se ela é um palíndromo: ")

    resultado = e_palindromo(palavra)

    print(resultado)

main()