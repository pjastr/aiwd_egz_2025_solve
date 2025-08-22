import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sqlite3 import connect


conn = connect('struktura_wiekowa.db')
data = pd.read_sql("SELECT * FROM grupy_wiekowe", con=conn)

osoby = data["liczba_osob_tys"]

cmap = plt.colormaps['Set3']
kolory = [cmap(i) for i in range(len(osoby))]
e = [0,0,0.1,0,0,0]
plt.pie(osoby, colors=kolory, startangle=45, counterclock=True,
        labels=data["grupa_wiekowa"], explode=e, autopct="%1.2f%%")
plt.savefig("m13_zad.jpg")
plt.show()