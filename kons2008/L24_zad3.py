import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("wydatki_firm.csv", sep=";", decimal=",")

data2 = pd.wide_to_long(data, stubnames=["Marketing", "IT", "Szkolenia", "Wynagrodzenia", "Biuro"],
                        i="Firma", j="Rok", sep="_")

mediapro = data2.loc["MediaPro", :]

x = np.arange(3)

plt.scatter(x, mediapro["Marketing"], label="Marketing", color="blue", marker=">", s=75)
plt.scatter(x, mediapro["IT"], label="IT", color="green", marker="<", s=80)
plt.scatter(x, mediapro["Szkolenia"], label="Szkolenia", color="brown", marker="o", s=85)
plt.scatter(x, mediapro["Wynagrodzenia"], label="Wynagrodzenia", color="red", marker=".", s=90)
plt.scatter(x, mediapro["Biuro"], label="Biuro", color="orange", marker="^", s=95)

plt.xticks(x, mediapro.index)
plt.grid(True, alpha = 0.6)
plt.title("Dane o firmie MediaPro")
plt.legend()
plt.savefig("L24_zad3.tiff")
plt.show()