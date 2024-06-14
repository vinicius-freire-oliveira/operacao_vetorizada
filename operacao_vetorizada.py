import numpy as np

# Definindo x como uma lista de números de 0 a 10
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Convertendo x em um array NumPy
x = np.array(x)

# Calculando y usando operações vetorizadas do NumPy
y = x + 3 / 2

# Imprimindo o resultado
print(y)
