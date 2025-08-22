import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("kultura.csv", sep=";")
pomorskie = data[data["Nazwa"] == "POMORSKIE"]
opolskie = data[data["Nazwa"] == "OPOLSKIE"]
x= np.arange(4)
plt.bar(x-0.165, pomorskie["Wartość"], width=0.33)
plt.bar(x+0.165, opolskie["Wartość"], width=0.33)
plt.xticks(x, pomorskie["Kategoria"])
plt.title("Dane dotyczące kultury")
plt.xlabel("Kategorie")
plt.ylabel("Wartość")
plt.tight_layout()
plt.savefig("M34_zad3.tiff")
plt.show()