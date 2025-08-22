import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sqlite3 import connect

conn = connect('ceny_chleb.db')
data = pd.read_sql("SELECT * FROM ceny_produktow", con=conn)
x = data["Rok"].astype(int)
y = data["Wartość"]
plt.annotate(text="14.08.2025", xy=(2010,2.4))
plt.plot(x,y)
plt.title("Ceny chleba")
plt.xlabel("Lata")
plt.ylabel("Cena w zł")
plt.grid(True)
plt.tight_layout()
plt.savefig("M31_zad2.png")
plt.show()