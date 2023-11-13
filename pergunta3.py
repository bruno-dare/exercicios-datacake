def has_sum_pair(arr, target):
    seen_numbers = set()

    for num in arr:
        complement = target - num
        if complement in seen_numbers:
            return True
        seen_numbers.add(num)

    return False

# Exemplo de uso
array = [1, 15, 2, 7, 2, 5, 7, 1, 4]
target_value = int(input("Digite o valor alvo (X): "))

result = has_sum_pair(array, target_value)

print(f"Existe uma combinação de soma para {target_value}: {result}")
