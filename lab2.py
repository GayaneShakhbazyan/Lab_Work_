import numpy as np
import matplotlib.pyplot as plt

# 1. Ֆունկցիան
def f(x):
    # x-ը դրական 
    return np.where(x > 0, x**2 - 4 * np.log(x) - 2, np.inf)

# 2. Պարամետրերը 
a = 0.5
b = 3.0
e = 0.5    
d = 0.125  

x_vals = []
f_vals = []
intervals = [(a, b)] 

# 3. Հաշվարկային ցիկլ
while (b - a) > e:
    x1 = (a + b - d) / 2
    x2 = (a + b + d) / 2
    
    x_m = 0.5 * (a + b)
    x_vals.append(f"{x_m:.4f}")
    f_vals.append(f"{f(x_m):.4f}")

    if f(x1) <= f(x2):
        b = x2
    else:
        a = x1
    intervals.append((a, b))

# 4. Արդյունքներ
header_w = 25
col_w = 10
sep = "-" * (header_w + 3 + len(x_vals) * (col_w + 3))

print(f"{'xm = 0,5 * (ak + bk)':<{header_w}} | {' | '.join([v.center(col_w) for v in x_vals])}")
print(sep)
print(f"{'f(xm)':<{header_w}} | {' | '.join([v.center(col_w) for v in f_vals])}")

final_xm = 0.5 * (a + b)
print(f"\n Մինիմումի մոտավոր կետը: x* ≈ {final_xm:.4f}")

#  Գրաֆիկի կառուցումը 

x_smooth = np.linspace(0.4, 3.1, 400) 
y_smooth = f(x_smooth)

plt.figure(figsize=(12, 8))

plt.plot(x_smooth, y_smooth, label=r'f(x) = x^2 - 4\ln(x) - 2', color='blue', linewidth=2.5)

colors = plt.cm.viridis(np.linspace(0, 1, len(intervals))) 

for i, (start, end) in enumerate(intervals):
    plt.axvspan(start, end, color=colors[i], alpha=0.3, label=f'Քայլ {i}' if i < 5 else None)
plt.scatter(final_xm, f(final_xm), color='red', s=100, zorder=10, marker='*', label=f'Մոտավոր մինիմում (x*={final_xm:.2f})')
plt.title(fr'Հատվածի կիսման մեթոդ', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.xlim(0.4, 3.1)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

plt.show()
