import numpy as np
import matplotlib.pyplot as plt

# 1. A rács létrehozása (a "térkép")
x = np.linspace(-0.5, 2.5, 400)
y = np.linspace(-0.5, 2.5, 400)
X, Y = np.meshgrid(x, y)

# 2. A célfüggvény: Z = x^2 + y^2 (a "völgy", amit minimalizálni akarunk)
Z = X**2 + Y**2

# 3. A korlátozás: x + y = 2 (a "kerítés", amin járnunk kell)
# Átrendezve: y = 2 - x
x_line = np.linspace(-0.5, 2.5, 100)
y_line = 2 - x_line

# 4. A megoldás (ahol a kettő érinti egymást): (1, 1) pont
sol_x, sol_y = 1, 1

# --- ÁBRÁZOLÁS ---
plt.figure(figsize=(8, 8))

# Szintvonalak (a körök)
contours = plt.contour(X, Y, Z, levels=15, cmap='Blues')
plt.clabel(contours, inline=True, fontsize=8)

# A korlátozás (a piros vonal)
plt.plot(x_line, y_line, 'r-', linewidth=3, label='Korlátozás (Rβ = r)')

# A megoldás (az érintési pont)
plt.plot(sol_x, sol_y, 'go', markersize=10, label='Restricted LS megoldás')

# A nyilak (Gradiens vektorok) - A LÉNYEG!
# Célfüggvény gradiense (merre emelkedik a völgy): [2x, 2y] -> [2, 2]
plt.arrow(sol_x, sol_y, 0.4, 0.4, head_width=0.05, color='blue', label='Célfüggvény gradiense')
# Korlátozás gradiense (merre merőleges a falra): [1, 1]
plt.arrow(sol_x, sol_y, 0.2, 0.2, head_width=0.05, color='red', label='Korlátozás gradiense')

plt.xlim(-0.5, 2.5)
plt.ylim(-0.5, 2.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('A Lagrange-multiplikátor geometriai jelentése')
plt.legend()
plt.grid(True)
plt.show()