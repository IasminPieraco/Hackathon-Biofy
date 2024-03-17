import pandas as pd

venda = {'data': ['15/02/2024', '16/02/2024'],
         'valor': [500, 300],
         'produto': ['feijao', 'arroz'],
         'qnt':[50,70]}

vendas_df = pd.DataFrame(venda)
venda_teste = pd.read_excel("dataset/weather.xlsx")

print(vendas_df)
print(venda_teste)
print(venda_teste.describe())
print(venda_teste.loc[2])
print(venda_teste.loc[venda_teste['conditions'] == 'Partially cloudy'])

#Para Add linhas novas na matriz:
#venda_teste = venda_teste.append(linha)
#Para excluir:
#venda_teste = venda_teste.drop('tempmin',axis=1)
#correlacao = venda_teste.corr(method='pearson')

#print(correlacao)