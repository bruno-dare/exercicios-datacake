def ordenar_com_um_a_esquerda(arr):
    # Conta o número de ocorrências do número "1"
    count_ones = arr.count(1)

    # Move os números "1" para o início do array
    arr[:count_ones] = [1] * count_ones

# Array de exemplo
arr = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]

# Chama a função para ordenar o array com os "1" à esquerda
ordenar_com_um_a_esquerda(arr)

# mostra o array modificado
print(arr)