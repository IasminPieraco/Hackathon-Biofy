import pandas as pd
import numpy as np
arquivo = pd.read_excel("../dataset/clima.xlsx")
aux = arquivo['precip']
aux = aux.where(aux > 0, other=np.nan)
aux = aux.dropna(how='all')
print(aux.median())
#arquivo['target'] = (arquivo['precip'] >= (aux).median()).astype(int)
arquivo.loc[arquivo['precip'] > (aux).median(),'target'] = 2
arquivo.loc[arquivo['precip'] <= (aux).median(),'target'] = 1
arquivo.loc[arquivo['precip'] == 0,'target'] = 0

print((aux).median())

y = arquivo['target'] # variavel alvo
x = arquivo.drop("precip", axis = 1)
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
previsoes = modelo.predict(x_original[1901:2000])
print(previsoes)