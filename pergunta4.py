def completar_intervalo(arr):
    # Encontrar o maior número no array
    max_num = max(arr)

    # Criar um conjunto com todos os números no intervalo de 0 a n
    intervalo_completo = set(range(max_num + 1))

    # Encontrar os números que estão faltando
    numeros_faltando = list(intervalo_completo - set(arr))

    # Adicionar os números faltando ao array original
    arr.extend(numeros_faltando)

# Array de exemplo
arr = [9, 2, 3, 1, 4]

# Chamar a função para completar o intervalo e adicionar os números faltando
completar_intervalo(arr)

# Imprimir o array modificado
print(arr)
