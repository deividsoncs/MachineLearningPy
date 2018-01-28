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


#preencher valores com a média
base.mean() # média de todas colunas
base['age'][base.age > 0].mean() # retorna média das idade da coluna age com exceção das idades negativas
base.loc[base['age'] < 0, 'age'] = 40.92
