import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x= ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek"]
y1 = [115,110,120, 125,130]
y2 = [205, 188, 198, 215, 268]
y3=[60, 60, 55, 65, 80]

plt.figure(figsize=(10,6))
plt.stackplot(x,y1, y2,y3, labels=["Chleb","Bułki", "Ciasta"],
              colors=["peru", "tan","darkorange"])
plt.title("Sprzedaż produktów w piekarni")
plt.legend()
plt.xlabel("Dzień tygodnia")
plt.ylabel("Liczba sprzedanych sztuk")
plt.grid(True)
plt.tight_layout()
plt.savefig("zad1.pdf")
plt.show()