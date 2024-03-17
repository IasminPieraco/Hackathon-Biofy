import pandas as pd
arquivo = pd.read_excel("../dataset/clima.xlsx")

arquivo.loc[arquivo['uvindex'] <= arquivo['uvindex'].describe()['25%'],'target'] = 1
arquivo.loc[arquivo['uvindex'] > arquivo['uvindex'].describe()['25%'],'target'] = 2
arquivo.loc[arquivo['uvindex'] > arquivo['uvindex'].describe()['50%'],'target'] = 3
arquivo.loc[arquivo['uvindex'] > arquivo['uvindex'].describe()['75%'],'target'] = 4

y = arquivo["target"] # variavel alvo
x = arquivo.drop("uvindex", axis = 1)
x = arquivo.drop("target", axis = 1) # variaveis preditoras
x_original = x
y = y[:1901]
x = x[:1901]


print(x.shape)
print()
print(y.shape)

from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.3)

from sklearn.ensemble import ExtraTreesClassifier
# Criacao do modelo:
modelo = ExtraTreesClassifier()
modelo.fit(x_treino, y_treino)

# Imprimindo resultados
resultado = modelo.score(x_teste, y_teste)
print("Acurácia: ", resultado)
print(x.shape)
previsoes = modelo.predict(x_original[1701:2000])
print(previsoes)
