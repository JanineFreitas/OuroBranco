import pandas as panda
import matplotlib.pyplot as plt

dados = panda.read_csv(r"C:\Users\Janine\Documents\Mestrado - Cesar\Data Science\Dados - Folha de Pagamento Prefeitura de Fortaleza\VW_FINANCEIRO2.csv")
'''dadosSalarioLiquido = dados[(dados["CD_VERBA"] == 998) & (dados["DT_REFER"] > 201902)]
salarios = dados['NR_VALOR']'''

dados201901 = dados[dados["DT_REFER"] == 201901].NR_VALOR
dados201902 = dados[dados["DT_REFER"] == 201902].NR_VALOR
dados201903 = dados[dados["DT_REFER"] == 201903].NR_VALOR
dadosInteiros = [dados201901, dados201902, dados201903]

plt.boxplot(dadosInteiros, notch=True, patch_artist= True)
plt.title('Árvore de salários')
plt.xlabel('Meses 201901 201902 e 201903')
plt.show()

print('Janine Freitas')