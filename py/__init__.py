import pandas as panda
import matplotlib.pyplot as plt

dados = panda.read_csv(r"C:\Users\Janine\Documents\Mestrado - Cesar\Data Science\Dados - Folha de Pagamento Prefeitura de Fortaleza\VW_FINANCEIRO.csv")
salarios = dados['NR_VALOR']

plt.boxplot(dados.NR_VALOR)
plt.title('Árvore de salários')
plt.xlabel('Quantidade de Funcionários')

print('Janine Freitas')