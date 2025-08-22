import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data =  pd.read_excel("wynagrodzenia.xlsx")

minimalna = data[data["Rodzaje"] == "Płaca minimalna - miesięcznie"]
srednia = data[data["Rodzaje"] == "Płaca średnia krajowa - miesięcznie"]

rok = minimalna["Rok"]

plt.barh(rok-0.165, minimalna["Wartosc"], height=0.33, label="Minimalne")
plt.barh(rok+0.165, srednia["Wartosc"], height=0.33,label="Średnie")
plt.legend(loc=4)
plt.grid(True, alpha = 0.7)
plt.title("Porównanie wynagrodzeń")
plt.ylabel("Rok")
plt.xlabel("Wartość")
plt.tight_layout()
plt.savefig("M24_zad.jpg")
plt.show()