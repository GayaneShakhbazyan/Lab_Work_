import numpy as np
import matplotlib.pyplot as plt

# 1. Ֆունկցիա
def f(x):
    return x**2 - 4 * np.log(x) - 2

# 2. Պարամետրերը 
a = 0.5
b = 3.0
e = 0.5  
phi = (1 + 5**0.5) / 2 

x_vals = []
f_vals = []
intervals = [(a, b)]

# 3. Սկզբնական կետեր
x1 = b - (b - a) / phi
x2 = a + (b - a) / phi

# 4. Հիմնական ցիկլ
while (b - a) > e:
    x_m = (a + b) / 2
    x_vals.append(f"{x_m:.4f}")
    f_vals.append(f"{f(x_m):.4f}")
    
    if f(x1) < f(x2):
        b = x2
        x2 = x1
        x1 = b - (b - a) / phi
    else:
        a = x1
        x1 = x2
        x2 = a + (b - a) / phi
    
    intervals.append((a, b))

# 5. Աղյուսակ
header_w = 25
col_w = 10
sep = "-" * (header_w + 3 + len(x_vals) * (col_w + 3))

print(f"{'xm = (ak + bk) / 2':<{header_w}} | {' | '.join([v.center(col_w) for v in x_vals])}")
print(sep)
print(f"{'f(xm)':<{header_w}} | {' | '.join([v.center(col_w) for v in f_vals])}")

final_x = (a + b) / 2
print(f"\nՄինիմումի մոտավոր կետը: x* ≈ {final_x:.4f}")

#  Գրաֆիկի կառուցում 
x_smooth = np.linspace(0.4, 3.1, 400)
y_smooth = f(x_smooth)

plt.figure(figsize=(12, 7))
plt.plot(x_smooth, y_smooth, label=r'f(x) = x^2 - 4\ln(x) - 2', color='blue', linewidth=2)

colors = plt.cm.plasma(np.linspace(0, 1, len(intervals)))
for i, (start, end) in enumerate(intervals):
    plt.axvspan(start, end, color=colors[i], alpha=0.2, label=f'Քայլ {i}')

plt.scatter(final_x, f(final_x), color='red', s=150, marker='*', zorder=5, label=f'Մինիմում x*={final_x:.2f}')

plt.title(fr'Ոսկե հատույթի մեթոդ', fontsize=14)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()
