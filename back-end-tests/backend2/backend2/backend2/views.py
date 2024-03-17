from django.shortcuts import render
from django.http import JsonResponse

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

from sklearn.model_selection import train_test_split

from sklearn.ensemble import ExtraTreesClassifier

modelWindSpeed = ExtraTreesClassifier()
modelUVIndex = ExtraTreesClassifier()
modelPrecipitation = ExtraTreesClassifier()

def back_end_ML_training(request):
    dia = request.GET.get('dia', 0)
    # VELOCIDADE DO VENTO
    
    arquivo = pd.read_excel("./static/clima.xlsx")
    
    arquivo.loc[arquivo['windspeed'] <= arquivo['windspeed'].describe()['25%'],'target'] = 0
    arquivo.loc[arquivo['windspeed'] > arquivo['windspeed'].describe()['25%'],'target'] = 1
    arquivo.loc[arquivo['windspeed'] > arquivo['windspeed'].describe()['50%'],'target'] = 2
    arquivo.loc[arquivo['windspeed'] > arquivo['windspeed'].describe()['75%'],'target'] = 3

    y = arquivo['target'] # variavel alvo
    x = arquivo.drop("windspeed", axis = 1)
    x = arquivo.drop("target", axis = 1) # variaveis preditoras
    y = y[:1951]
    x = x[:1951]

    x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.3)
    
    modelWindSpeed.fit(x_treino, y_treino)
    
    
    # PRECIPITAÇÃO
    
    arquivo = pd.read_excel("../dataset/clima.xlsx")
    
    aux = arquivo['precip']
    aux = aux.where(aux > 0, other=np.nan)
    aux = aux.dropna(how='all')
    arquivo.loc[arquivo['precip'] > (aux).median(),'target'] = 2
    arquivo.loc[arquivo['precip'] <= (aux).median(),'target'] = 1
    arquivo.loc[arquivo['precip'] == 0,'target'] = 0
    
    y = arquivo['target']
    x = arquivo.drop("precip", axis = 1)
    x = arquivo.drop("target", axis = 1)
    y = y[:1951]
    x = x[:1951]
    
    x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.3)
    
    modelPrecipitation.fit(x_treino, y_treino)
    
    
    # INDICE UV
    
    arquivo = pd.read_excel("../dataset/clima.xlsx")
    
    arquivo.loc[arquivo['uvindex'] <= arquivo['uvindex'].describe()['25%'],'target'] = 1
    arquivo.loc[arquivo['uvindex'] > arquivo['uvindex'].describe()['25%'],'target'] = 2
    arquivo.loc[arquivo['uvindex'] > arquivo['uvindex'].describe()['50%'],'target'] = 3
    arquivo.loc[arquivo['uvindex'] > arquivo['uvindex'].describe()['75%'],'target'] = 4

    y = arquivo["target"] # variavel alvo
    x = arquivo.drop("uvindex", axis = 1)
    x = arquivo.drop("target", axis = 1) # variaveis preditoras
    y = y[:1951]
    x = x[:1951]
    
    x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.3)
    
    modelUVIndex.fit(x_treino, y_treino)
    
    teste = arquivo['Dia' == 10]
    print(teste)
    
    return JsonResponse({teste})
    
    
# def wind_speed_ML(dia, arquivo):
#     teste = arquivo['Dia' == 10]
#     print(teste)
#     # previsaoWS = modelWindSpeed.predict(x_original[1901:2000])
#     # return previsaoWS   
    
# def UV_index_ML(dia, arquivo):
#     previsaoUV = modelUVIndex.predict(x_original[1901:2000])
#     return previsaoUV 
    
# def precipitation_ML(dia, arquivo):
#     previsaoPrec = modelPrecipitation.predict(x_original[1901:2000])
#     return previsaoPrec 
    



# Create your views here.
