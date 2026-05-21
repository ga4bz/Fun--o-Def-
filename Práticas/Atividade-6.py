def imprime_diagonal(matriz):
    for i in range(len(matriz)):
        print(matriz[i][i])

def main():
    matriz = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    
    imprime_diagonal(matriz)

main()