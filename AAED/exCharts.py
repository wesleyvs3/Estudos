import matplotlib.pyplot as plt
import numpy as np

# Define o intervalo de n
n = np.linspace(1, 20, 500)

# Define as funções
g = 2**(n + 1)  # 2^(n+1)
cf = 2 * 2**n  # c * 2^n, onde c = 2

# Cria o gráfico
plt.figure(figsize=(10, 6))
plt.plot(n, g, label=r'$g(n) = 2^{n+1}$', color='blue')
plt.plot(n, cf, label=r'$2 \cdot 2^n$', color='red', linestyle='--')

# Adiciona títulos e legendas
plt.xlabel('n')
plt.ylabel('Valor da função')
plt.title('Comparação entre $2^{n+1}$ e $2 \cdot 2^n$')
plt.legend()
plt.grid(True)

# Exibe o gráfico
plt.show()
