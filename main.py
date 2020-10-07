import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('input/resistor-simulacao.csv')
img_nome = 'grafico.png'
colunas = data.columns.tolist()
xlabel = colunas[0]
ylabel = colunas[1]

x_data = data[xlabel].to_numpy()
y_data = data[ylabel].to_numpy()

fig, ax = plt.subplots(figsize=(4.8,4))
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

ax.plot(x_data, y_data, marker='o', ls='', ms=3)
plt.yscale('linear')
plt.xscale('linear')
plt.title('Gráfico de corrente vs tensão (resistor)')

if len(colunas) == 4:
    xerr = colunas[2]
    yerr = colunas[3]
    xerr = data[xerr].to_numpy()
    yerr = data[yerr].to_numpy()
    ax.errorbar(x_data, y_data, yerr, xerr, linestyle='None', marker='')
# plt.show()
plt.savefig('output/'+img_nome)