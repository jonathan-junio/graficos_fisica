import matplotlib.pyplot as plt
import pandas as pd

# ---------------------CONFIGURAÇÕES---------------------
titulo = 'Gráfico de corrente vs tensão (Resistor)'
x_label = 'Tensão em V'
y_label = 'Corrente em A'
log = False
file = 'input/resistor_lab.csv'
output = 'output/grafico.png'

#-----------------------GERAÇÃO DO GRAFICO-----------------

data = pd.read_csv(file)
colunas = data.columns.tolist()
fig, ax = plt.subplots(figsize=(6,6))
plt.title(titulo)
ax.set_xlabel(x_label)
ax.set_ylabel(y_label)

x_data = data[colunas[0]].to_numpy()
y_data = data[colunas[1]].to_numpy()
ax.plot(x_data, y_data, marker='o', ls='', ms=2)

if log:
    plt.yscale('log', nonpositive='clip')
    plt.xscale('log', nonpositive='clip')
else:
    plt.yscale('linear')
    plt.xscale('linear')

if len(colunas) == 4:
    xerr = colunas[2]
    yerr = colunas[3]
    xerr = data[xerr].to_numpy()
    yerr = data[yerr].to_numpy()
    if log:
        xerr = [0.434*x for x in xerr]
        yerr = [0.434*y for y in yerr]
    ax.errorbar(x_data, y_data, yerr, xerr, linestyle='None', marker='', color='black')
plt.savefig(output)