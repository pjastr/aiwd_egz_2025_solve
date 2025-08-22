import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sprzedaz_produktow.csv", sep="#", decimal=",")
elektronika = data[data["Kategoria"] == "Elektronika"]
odziez = data[data["Kategoria"] == "Odzież"]
dom = data[data["Kategoria"] == "Dom_i_Ogród"]
sport = data[data["Kategoria"] == "Sport"]
ksiazki = data[data["Kategoria"] == "Książki"]

x = elektronika["Kwartał"]
plt.scatter(x, elektronika["Wartość"], marker="^", color="blue", label="Elektronika")
plt.scatter(x, odziez["Wartość"], marker="o", color="green", label="Odzież")
plt.scatter(x, dom["Wartość"], marker=">", color="orange", label="Dom i ogród")
plt.scatter(x, sport["Wartość"], marker="*", color="pink", label="Sport")
plt.scatter(x, ksiazki["Wartość"], marker="<", color="violet", label="Książki")
plt.grid(True, alpha = 0.6)
plt.ylim(0,2000)
plt.xlabel("Rok")
plt.ylabel("Wartość")
plt.title("Dane o sprzedaży")
plt.legend()
plt.tight_layout()
plt.savefig("zad3.png")

plt.show()