import numpy as np

def calculate(list_in):
    # 1. Validar se a lista tem exatamente 9 elementos
    if len(list_in) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # 2. Converter a lista em uma matriz 3x3 do NumPy
    matrix = np.array(list_in).reshape(3, 3)
    
    # 3. Criar o dicionário com os cálculos estruturados
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(), 
            matrix.mean(axis=1).tolist(), 
            matrix.mean().tolist()
        ],
        'variance': [
            matrix.var(axis=0).tolist(), 
            matrix.var(axis=1).tolist(), 
            matrix.var().tolist()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(), 
            matrix.std(axis=1).tolist(), 
            matrix.std().tolist()
        ],
        'max': [
            matrix.max(axis=0).tolist(), 
            matrix.max(axis=1).tolist(), 
            matrix.max().tolist()
        ],
        'min': [
            matrix.min(axis=0).tolist(), 
            matrix.min(axis=1).tolist(), 
            matrix.min().tolist()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(), 
            matrix.sum(axis=1).tolist(), 
            matrix.sum().tolist()
        ]
    }

    return calculations

# ==========================================
# CHAMADA DIRETA (Força o print na tela)
# ==========================================
print("\n=== EXECUTANDO O TESTE MANUAL ===")

lista_para_testar = [0, 1, 2, 3, 4, 5, 6, 7, 8]
resultado_final = calculate(lista_para_testar)

import pprint
pprint.pprint(resultado_final)

print("==================================\n")