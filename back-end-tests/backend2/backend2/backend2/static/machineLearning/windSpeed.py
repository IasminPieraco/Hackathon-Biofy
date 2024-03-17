import pandas as pd
    arquivo = pd.read_excel("../dataset/clima.xlsx")
    # arquivo['target'] = (arquivo['windspeed'] >= arquivo['windspeed'].median()).astype(int)
    arquivo.loc[arquivo['windspeed'] <= arquivo['windspeed'].describe()['25%'],'target'] = 0
    arquivo.loc[arquivo['windspeed'] > arquivo['windspeed'].describe()['25%'],'target'] = 1
    arquivo.loc[arquivo['windspeed'] > arquivo['windspeed'].describe()['50%'],'target'] = 2
    arquivo.loc[arquivo['windspeed'] > arquivo['windspeed'].describe()['75%'],'target'] = 3

    print(arquivo['windspeed'].describe())
    print(arquivo)

    # nan_rows = arquivo.isna().any(axis=1)
    # print(nan_rows)

    # for i in range(arquivo.shape[0]): # Iterate over rows
    #     for j in range(arquivo.shape[1]): # Iterate over columns
    #         if pd.isna(arquivo.iloc[i, j]): # Check if the cell is NaN
    #             print(f"NaN found at row {i}, column {j}")




    y = arquivo['target'] # variavel alvo
    x = arquivo.drop("windspeed", axis = 1)
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

    max = arquivo['windspeed'].describe()['max']

    print(max)

    for i in range(len(previsoes)):
        previsoes[i] = (((previsoes[i]+1)/6)*max)

    print(previsoes)
