import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv')
img_nome = 'grafico.png'
colunas = data.columns.tolist()
print(colunas)

fig, ax = plt.subplots()
# plt.show()