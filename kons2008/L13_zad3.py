import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("sprzedaz_regionalna.csv", sep=";", index_col=0).T

pomorskie = data["Pomorskie"]
lodzkie = data["Łódzkie"]

cmap = plt.colormaps['Set3']
kolory = [cmap(i) for i in range(5)]

plt.figure(figsize=(10,6))

plt.subplot(1,2,1)
plt.pie(pomorskie, colors=kolory, autopct="%1.1f%%", labels=pomorskie.index)
circle = plt.Circle((0, 0), 0.5, color='white')
p = plt.gcf()
p.gca().add_artist(circle)
plt.title("Dane za woj. pomorskie")
plt.subplot(1,2,2)
plt.pie(lodzkie, colors=kolory, autopct="%1.1f%%", labels=lodzkie.index)
circle = plt.Circle((0, 0), 0.5, color='white')
p = plt.gcf()
p.gca().add_artist(circle)
plt.title("Dane za woj. łódzkie")

plt.tight_layout()

plt.savefig("L13_zad3.png")
plt.show()