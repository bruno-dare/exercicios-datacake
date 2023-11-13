class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def build_tree():
    # Construir a árvore conforme a descrição fornecida
    tree = TreeNode('maça',
        left=TreeNode('morango',
            left=TreeNode('goiaba'),
            right=TreeNode('limão')
        ),
        right=TreeNode('pera',
            left=TreeNode('abacaxi',
                right=TreeNode('laranja',
                    left=TreeNode('banana'),
                    right=TreeNode('cebola')
                )
            )
        )
    )
    return tree

def search_word(root, word):
    # Função para buscar a palavra na árvore
    def search_helper(node, target, path):
        if not node:
            return None
        path.append(node.key)
        if node.key == target:
            return path
        left_path = search_helper(node.left, target, path.copy())
        right_path = search_helper(node.right, target, path.copy())
        return left_path or right_path

    return search_helper(root, word, [])

# Construir a árvore
tree = build_tree()

# Solicitar entrada do usuário
search_target = input("Digite o nome da fruta para encontrar o caminho até ela: ")

# Buscar a palavra na árvore
result = search_word(tree, search_target)

# Exibir o resultado
if result:
    print(' -> '.join(result))
else:
    print(f'Fruta "{search_target}" não encontrada na árvore.')
