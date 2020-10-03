import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv')
img_nome = 'grafico.png'
colunas = data.columns.tolist()
xlabel = colunas[1]
ylabel = colunas[0]
xerr = colunas[2]
yerr = colunas[3]
x_data = data[xlabel].to_numpy()
y_data = data[ylabel].to_numpy()

fig, ax = plt.subplots(figsize=(6.4, 4.9))
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.plot(x_data, y_data, marker='o', ls='', ms=5)
plt.text(10, -10, 'exemplo')

if len(colunas) == 4:
    xerr = data[xerr].to_numpy()
    yerr = data[yerr].to_numpy()
    ax.errorbar(x_data, y_data, yerr, xerr)
plt.show()