import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
# from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.arima.model import ARIMA
import os

dataFrame = pd.read_excel('../dataset/clima.xlsx')
infoview = dataFrame.where(dataFrame['Ano'] >= 2023, other=np.nan)
infoview = infoview.dropna()
infoview = dataFrame.where(dataFrame['Mes'] == 12, other=np.nan)
infoview = infoview.dropna()
model = ARIMA(dataFrame['windspeed'], order=(5,1,0))
model_fit = model.fit()
data = []
for i in infoview['Dia']:
    data.append((str(i)+'/12/2023'))
forecast = model_fit.forecast(steps=10) # Forecast 10 passos no futuro -> nesse caso sao 10 dias
plt.plot(data,infoview['windspeed'], label='Original')
plt.plot([1,2,3,4,5,6,7,8,9,10],forecast, label='Forecast')
plt.legend()
plt.show()

# Conjunto de dados mais enxuto
# Envio de 2 matrizes
