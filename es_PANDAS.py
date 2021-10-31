# importare librerie e leggere il file CSV dentro un “pandas dataframe”
import pandas as pd
df = pd.read_csv("Churn_Modelling.csv")
print(df.shape)
# (10000,14) = n° righe e n° colonne
print(df.columns, '\n')
# Index(['RowNumber', 'CustomerId', 'Surname', 'CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard','IsActiveMember','EstimatedSalary', 'Exited'], dtype='object')


# buttare via righe o colonne
df.drop(['RowNumber', 'CustomerId', 'Surname', 'CreditScore'], axis=1, inplace=True) # axis 1 imposta il drop delle colonne (ne cancello 4) // inplace True rende possible salvare le modifiche
print(df.shape, '\n')
# (10000,10)

# selezionare in lettura solo particolari colonne
df_spec = pd.read_csv("Churn_Modelling.csv", usecols=['Gender', 'Age', 'Tenure', 'Balance'])
print(df_spec.head(), '\n')

# leggere solo alcune righe (le prime 5.000)
df_partial = pd.read_csv("Churn_Modelling.csv", nrows=5000)
print(df_partial.shape, '\n')
# (5000,14)

# creare un campione più piccolo di dati
df_sample = df.sample(n=1000) # n° righe nel campione - vale anche df_sample = df.sample(frac=0.1) una percentuale del 10% dell’intero dataset
print(df_sample.shape, '\n')
# (1000,10)

# verifico se ci sono valori mancanti (NA None or numpy.NaN) per ogni colonna (non in questo caso)
print(df.isna().sum(), '\n')
# se ci fossero stati avrei potuto cancellare le righe incriminate con df.dropna(axis=0, how='any', inplace=True) 
# oppure riempirle con criteri di media o conteggio ES:
# avg = df['Balance'].mean()
# df['Balance'].fillna(value=avg, inplace=True)
# ----
# mode = df['Geography'].value_counts().index[0]
# df['Geography'].fillna(value=mode, inplace=True)

# faccio query selettive per righe che rispettano certe condizioni
france_churn = df[(df.Geography == 'France') & (df.Exited == 1)] # clienti che vivono in Francia ed hanno cambiato fornitore
print(france_churn.Geography.value_counts(), '\n') 
# France    810
balance_churn = df.query('80000 < Balance < 100000')
# usando query posso passare più flessibilmente condizioni tramite stringhe: clienti con bilancio tra 80 e 100k
print(balance_churn.Balance, '\n')

age_churn = df[df['Age'].isin([29, 40, 65, 30])] # clienti con età pari a 29, 40, 65 o 30
print(age_churn[:3], '\n') # primi 3 record

# groupby per avere un’overview sui dati ed esplorare relazioni tra variabili
df_summary = df[['Geography','Gender','Exited']].groupby(['Geography','Gender']).mean()
print(df_summary, '\n')
# media dei clienti fuoriusciti (exited) per stato e sesso
df_summary = df[['Geography','Gender','Exited']].groupby(['Geography','Gender']).agg(['mean','count'])
print(df_summary, '\n')



