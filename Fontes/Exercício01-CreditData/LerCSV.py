# -*- coding: utf-8 -*-
"""
Exercícios do curso da Udemy Machine Learning e Data Mining
Calixto

"""

import pandas as pd 
base = pd.read_csv('credit-data.csv') #importa csv
base.describe() # mostra estatística dos arquivos

base.loc[base['age'] < 0] #busco na coluna age os valores < 0

# apagar coluna
# base.drop('coluna', 1->apagar coluna inteira , inplace=True -> sobreescrever base atual  )
base.drop('age', 1 , inplace=True )

# apagar somenta registro com problema com idade negativa
base.drop(base[base.age < 0].index, inplace=True)



# média de todas colunas
base.mean() 
# retorna média das idade da coluna age com exceção das idades negativas
base['age'][base.age > 0].mean() 
#preencher valores com a média
base.loc[base['age'] < 0, 'age'] = 40.92


#pegar todos registros nulos
pd.isnull(base['age'])

#localiza registro onde a coluna age é nula
base.loc[pd.isnull(base['age'])]

# Obs.:1 Para realizar a preparação para algoritimo de Machine L. é necessário
# separar os dados em duas variáveis, previsoras e classe
# Obs.:2 Retirar a coluna de id, por ser sequencial e única ira atrapalhar a 
# classificação
# base.iloc[<todas as linhas da coluna> ,<coluna inicial>:<coluna final>].values
# começa de 1 e nunca chega na coluna 4(1, 2, 3), no exemplo abaixo
previsores = base.iloc[:,1:4].values
classe = base.iloc[:,4].values

# realiza o tratamento de valores nulos, substitui pela média.
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(previsores[:, 0:3])
previsores[:,0:3] = imputer.transform(previsores[:,0:3]) 