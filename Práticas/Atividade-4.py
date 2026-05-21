def receber_numeros():
    num = [0] * 5
    for i in range(len(num)):
        num[i] = int(input(f"Digite um número({i+1}/{len(num)}): "))
    return num

def media(num):
    return sum(num) / len(num)

def main():
    numeros = receber_numeros()
    print(f"A média dos números é {media(numeros)}")

main()