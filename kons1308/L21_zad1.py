import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

male = [-1700,-1900, -2300, -2600, -2800, -2400, -2600, -1700, -800]
female = [1700, 1800, 2200, 2500, 2700, 2400, 2650, 2050, 1400]
age_groups = ["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80+"]

plt.figure(figsize=(10, 6))
plt.barh(age_groups, male, label='Mężczyźni', color="blue")
plt.barh(age_groups, female, label='Kobiety', color="red")
plt.xlabel('Liczba osób (w tysiącach)')
plt.ylabel('Grupa wiekowa')
plt.title('Struktura ludności Polski - 2024')

ticks = np.arange(-3000, 3001, 500)
labels = np.abs(ticks)
plt.xticks(ticks, labels)

plt.legend()
plt.grid(axis='x', linestyle='solid', alpha=0.5)
plt.tight_layout()
plt.savefig("L22_zad2.svg")
plt.show()