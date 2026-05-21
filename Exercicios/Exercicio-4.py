def contar_caracteres(texto, caractere):
    contador = 0

    texto = texto.lower()
    caractere = caractere.lower()

    for letra in texto:
        if letra == caractere:
            contador += 1

    return contador

def texto_caractere():
    texto = input("Digite um texto: ")
    caractere = input("Digite um caractere para contar quantas vezes ele aparece no texto: ")
    
    return texto, caractere

def main():
    texto, caractere = texto_caractere()

    resultado = contar_caracteres(texto, caractere)
    print(f"A letra '{caractere}' aparece {resultado} vezes")

main()