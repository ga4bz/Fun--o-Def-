def receber_numeros():
    num = [0] * 3
    for i in range(len(num)):
        num[i] = int(input(f"Digite um número({i+1}/{len(num)}): "))
    return num

def maior(num):
    return max(num)

def main():
    numeros = receber_numeros()
    print(f"O maior número é {maior(numeros)}")

main()
