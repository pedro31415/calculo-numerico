import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline

# Pontos conhecidos
x = np.array([0, 0.2, 0.4, 0.6, 0.8])
y = np.array([1.00000, 1.22140, 1.49182, 1.82212, 2.22554])

# Valor para aproximar
x_eval = 0.65

# Interpolação linear
linear_interp = interp1d(x,y, kind='linear')
y_linear = linear_interp(x_eval)

# Interpolação Quadrática
quadratic_interp = interp1d(x, y, kind='quadratic')
y_quadratic = quadratic_interp(x_eval)

# Interpolação Cúbica
cubic_interp = CubicSpline(x, y)
y_cubic = cubic_interp(x_eval)

# Pontos para plotagem das funções interpoladoras
x_new = np.linspace(0, 0.8, 100)

# Valores interpolados para plotagem
y_linear_new = linear_interp(x_new)
y_quadratic_new = quadratic_interp(x_new)
y_cubic_new = cubic_interp(x_new)

# Plotagem dos dados e das funções interpoladoras
plt.figure(figsize=(12, 8))

# Dados originais
plt.plot(x, y, 'ro', label='Dados Originais')

# Interpolação Linear
plt.plot(x_new, y_linear_new, 'b--', label='Interpolação Linear')

# Interpolação Quadrática
plt.plot(x_new, y_quadratic_new, 'g-.', label='Interpolação Quadrática')

# Interpolação Cúbica
plt.plot(x_new, y_cubic_new, 'm-', label='Interpolação Cúbica')

# Ponto de avaliação
plt.plot(x_eval, y_linear, 'bo', label=f'Linear: f(0.65) = {y_linear:.5f}')
plt.plot(x_eval, y_quadratic, 'go', label=f'Quadrática: f(0.65) = {y_quadratic:.5f}')
plt.plot(x_eval, y_cubic, 'mo', label=f'Cúbica: f(0.65) = {y_cubic:.5f}')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolação Linear, Quadrática e Cúbica')
plt.legend()
plt.grid(True)
plt.savefig("graphs.png")

