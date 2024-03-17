import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder



writerClima = pd.ExcelWriter('dataset/clima.xlsx')
writerCorrelacao = pd.ExcelWriter('dataset/correlacao.xlsx')


clima = pd.read_excel("dataset/weather.xlsx")

preciptype = clima['preciptype'].unique()

ohe = OneHotEncoder()
array = ohe.fit_transform(clima[['preciptype']]).toarray()

label = np.array(ohe.categories_).ravel()

for i in range(len(label)):
    label[i] = 'preciptype-'+str(label[i])

DF = pd.DataFrame(array, columns = label)
DF = DF.drop('preciptype-nan',axis=1)

clima = pd.concat([clima, DF],axis=1)
clima = clima.drop("preciptype", axis=1)

conditions = clima['conditions'].unique()


array = ohe.fit_transform(clima[['conditions']]).toarray()

label = np.array(ohe.categories_).ravel()

for i in range(len(label)):
    label[i] = 'conditions-'+str(label[i])

DF = pd.DataFrame(array, columns = label)

clima = pd.concat([clima, DF],axis=1)
clima = clima.drop("conditions", axis=1)


clima = clima.drop("description", axis=1)
clima = clima.drop("icon", axis=1)
clima = clima.drop("stations", axis=1)

clima[['Dia', 'Mes', 'Ano']] = clima['datetime'].str.split('/', expand=True)
clima[['trash', 'hora']] = clima['sunrise'].str.split('T', expand=True)
clima[['Sunrise-Hora', 'Sunrise-Minuto', 'Sunrise-Segundo']] = clima['hora'].str.split(':', expand=True)


clima = clima.drop("datetime", axis=1)
clima = clima.drop("sunrise", axis=1)
clima = clima.drop("trash", axis=1)
clima = clima.drop("hora", axis=1)


clima[['trash', 'hora']] = clima['sunset'].str.split('T', expand=True)
clima[['Sunset-Hora', 'Sunset-Minuto', 'Sunset-Segundo']] = clima['hora'].str.split(':', expand=True)

clima = clima.drop("sunset", axis=1)
clima = clima.drop("trash", axis=1)
clima = clima.drop("hora", axis=1)


clima = clima.fillna(0)

correlacao = clima.corr(method='pearson')

print(correlacao)

print(clima)

clima.to_excel('dataset/clima.xlsx', index=False)

correlacao.to_excel('dataset/correlacao.xlsx', index=False)
