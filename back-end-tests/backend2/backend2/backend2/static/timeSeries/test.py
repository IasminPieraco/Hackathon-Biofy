import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.arima.model import ARIMA

dataFrame = pd.read_excel('../dataset/clima.xlsx')
print(dataFrame)
# infoview = dataFrame.where(dataFrame['Ano'] >= 2023, other=np.nan)
# infoview = infoview.dropna()
# infoview = dataFrame.where(dataFrame['Mes'] == 12, other=np.nan)
# infoview = infoview.dropna()
infoview = dataFrame[1900:2000]
model = ARIMA(dataFrame['windspeed'], order=(5,1,0))
model_fit = model.fit()
# data = []
# for i in infoview['Dia']:
#     data.append((str(i)+'/12/2023'))
forecast = model_fit.forecast(steps=10) # Forecast 10 passos no futuro -> nesse caso sao 10 dias
# plt.plot(data,infoview['windspeed'], label='Original')
plt.plot(infoview['windspeed'], label='Original')
plt.plot(forecast, label='Forecast')
plt.legend()
plt.show()

# Conjunto de dados mais enxuto
# Envio de 2 matrizes
