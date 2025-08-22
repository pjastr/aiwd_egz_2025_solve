import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sqlite3 import connect


conn = connect('budzet_domowy.db')
data = pd.read_sql("SELECT * FROM wydatki", con=conn)

cmap = plt.colormaps['Set3']
kolory = [cmap(i) for i in range(9)]
e = [0.05, 0,0,0,0,0,0,0,0]

plt.figure(figsize=(10,6))
plt.pie(data["kwota_zl"], labels=data["kategoria"], colors=kolory, startangle=45,
        counterclock=True, explode=e, autopct="%1.2f%%")
plt.title("Wydatki domowe")
plt.axis("equal")
plt.savefig("zad2.jpg")
plt.show()