import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# 1. Փոփոխականը և ֆունկցիան 
x = sp.Symbol('x')
# f(x) = x^2 - 4 * ln(x) - 2
y_expr = x**2 - 4 * sp.log(x) - 2

dy = sp.diff(y_expr, x)
print(f"Ածանցյալը: {dy}")

# 2. Պարամետրեր 
e = 0.5
a, b = 0.5, 3
n = 5  

# 3. Ընտրանքների եղանակ
k = np.arange(n + 1)
x_k = a + k * (b - a) / n

y_k = x_k**2 - 4 * np.log(x_k) - 2

# Գրաֆիկի կառուցումը 

x_smooth = np.linspace(a, b, 200)
y_smooth = x_smooth**2 - 4 * np.log(x_smooth) - 2

plt.figure(figsize=(10, 6))

plt.plot(x_smooth, y_smooth, label=r'f(x) = x^2 - 4\ln(x) - 2', color='blue', linewidth=2)

plt.scatter(x_k, y_k, color='red', zorder=5, label=f'Հաշվարկային կետեր (n={n})')

plt.title('Ֆունկցիայի գրաֆիկը ', fontsize=14)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

plt.show()
