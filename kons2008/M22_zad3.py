import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("wydatki_domowe.csv", sep=" ", index_col=0).T
kowalscy = data["Kowalskich"]
nowaccy = data["Nowackich"]
wisniewscy = data["Wiśniewskich"]
cmap = plt.colormaps['Set3']
kolory = [cmap(i) for i in range(6)]

plt.figure(figsize=(6,10))
etykiety = kowalscy.index
plt.subplot(3, 1,1)

plt.pie(kowalscy, colors=kolory, labels=etykiety, autopct="%1.1f%%")
plt.title("Kowalscy")
plt.subplot(3, 1,2)
plt.pie(nowaccy, colors=kolory, labels=etykiety, autopct="%1.1f%%")
plt.title("Nowaccy")
plt.subplot(3, 1,3)
plt.pie(wisniewscy, colors=kolory, labels=etykiety, autopct="%1.1f%%")
plt.title("Wiśniewscy")

plt.suptitle("Wydatki gospodarstw domowych")
plt.tight_layout()

plt.savefig("M22_zad3.svg")
plt.show()