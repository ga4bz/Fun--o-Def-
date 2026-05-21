import os
import time

def soma():
    print("--- SOMA ---")
    x = ler_numero()
    y = ler_numero()
    return x + y

def sub():
    print("--- SUBTRAÇÃO ---")
    x = ler_numero()
    y = ler_numero()
    return x - y

def mult():
    print("--- MULTIPLICAÇÃO ---")
    x = ler_numero()
    y = ler_numero()
    return x * y

def div():
    print("--- DIVISÃO ---")
    x = ler_numero()
    while True:
         y = ler_numero()

         if y != 0:
             break
         print("Não é possível dividir por 0.")
    return x / y

def menu():
    os.system("cls")
    while True:
        print("--- CALCULADORA ---\n1. SOMA\n2. SUBTRAÇÃO\n3. MULTIPLICAÇÃO\n4. DIVISÃO\n0. SAIR")

        try:
            escolha = int(input("Escolha uma operação matemática: "))


            if 0 <= escolha <= 4:
                return escolha
            print("Escolha uma opção válida!")

        except ValueError:
            print("Digite apenas números!")

def ler_numero():
    while True:
        try:
            numero = float(input("Digite um número: "))
            return numero
        except ValueError:
            print("Digite apenas números!")

def main():
    escolha = menu()
    time.sleep(1)

    while escolha != 0:
        if escolha == 1:
            resultado = soma()

        elif escolha == 2:
            resultado = sub()
        
        elif escolha == 3:
            resultado = mult()
        
        elif escolha == 4:
            resultado = div()
             
        print(f"Resultado: {resultado}")
        
        input("\nPressione ENTER para continuar...")

        time.sleep(1)
        
        escolha = menu()

    print("Calculadora encerrada.")
    
main()