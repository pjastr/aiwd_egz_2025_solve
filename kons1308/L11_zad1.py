import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

miesiace = ["Kwiecień", "Maj", "Czerwiec", "Lipiec"]
y1 = [12.5, 18.1, 21.9, 23.6]
y2 = [11.8, 17.6, 21.5, 23.1]
y3 = [9.6, 15.4, 19.3, 20.9]

plt.plot(miesiace, y1, "red", marker="o", label="Warszawa")
plt.plot(miesiace, y2, "green", marker="D", label="Kraków")
plt.plot(miesiace, y3, "blue", marker="s", label="Gdańsk")
plt.ylim(8,25)
plt.ylabel(r"Temperatura ($^{\circ}$C)")
plt.xlabel("Miesiąc")
plt.legend()
plt.grid(True, alpha=0.4, linestyle = "dotted")
plt.title("Średnia temperatura w polskich miastach (2024)", fontweight = "bold")
plt.savefig("l11_zad1.svg")
plt.show()