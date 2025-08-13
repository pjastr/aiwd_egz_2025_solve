import matplotlib.pyplot as plt
import numpy as np
miesiace = ['Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Cze']
temp = [-2.5, -1, 8, 14, 20, 24]

plt.figure(figsize=(10,6))

plt.plot(miesiace, temp, linewidth=2, markersize=8, marker="o", color="red")
plt.grid(True, linestyle=':', alpha=0.7)
plt.title('Średnia temperatura w pierwszym półroczu 2025', fontweight="bold")
plt.xlabel('Miesiąc')
plt.ylabel(r'Temperatura ($^{\circ}$C)')
plt.ylim([-5, 30])
plt.fill_between(miesiace, temp, -5, alpha=0.2, color='orange')
plt.axhline(y=15, color='green', linestyle='--')
plt.text(0, 16, r'Próg ciepły (15 ($^{\circ}$C))', color='green')
plt.tight_layout()
plt.savefig("L31_zad1.svg")
plt.show()