
# checar os passos
def binary_search(lista, alvo):
    inicio, fim = 0, len(lista) - 1
    passos = 0  

    while inicio <= fim:
        meio = (inicio + fim) // 2
        passos += 1 
        if lista[meio] == alvo:
            return meio, passos 

        elif lista[meio] > alvo:
            fim = meio - 1

        else:
            inicio = meio + 1

    return -1, passos 

# generate a liste with itens
my_list = list(range(0, 51))

lista_nomes = [
    "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hank", "Ivy", "Jack",
    "Kelly", "Liam", "Mia", "Noah", "Olivia", "Penny", "Quinn", "Ryan", "Sophia", "Tom",
    "Uma", "Violet", "William", "Xander", "Yara", "Zane"
]

alvo = "Uma"
resultado, passos = binary_search(lista_nomes, alvo)

print(f"O nome esta na lista: {resultado}, passos usados: {passos}")

resultado, passos = binary_search(my_list, 5)
print(f"O numero esta na posicao: {resultado}, passos usados: {passos}")