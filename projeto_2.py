import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Previsão Renda",
     page_icon=":bar_chart:",
     layout="wide",
)

st.write('# Análise exploratória da previsão de renda')

renda = pd.read_csv('./input/previsao_de_renda.csv')



#plots
st.write('## Gráficos ao longo do tempo')
fig, ax = plt.subplots(2,2,figsize=(30,15))
sns.lineplot(x='data_ref',y='renda', hue='posse_de_imovel',data=renda, ax=ax[0,0])
ax[0, 0].tick_params(axis='x', rotation=33)
sns.lineplot(x='data_ref',y='renda', hue='tipo_renda',data=renda, ax=ax[0, 1])
ax[0, 1].tick_params(axis='x', rotation=33)
sns.lineplot(x='data_ref',y='renda', hue='posse_de_veiculo',data=renda, ax=ax[1, 0])
ax[1, 0].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='tipo_residencia',data=renda, ax=ax[1, 1])
ax[1, 1].tick_params(axis='x', rotation=45)
sns.despine()
st.pyplot(plt)

st.write('## Gráficos bivariada')
fig, ax = plt.subplots(figsize=(20,10))
sns.barplot(x='tempo_emprego',y='renda',data=renda)
#sns.barplot(x='posse_de_veiculo',y='renda',data=renda, ax=ax[1])
#sns.barplot(x='qtd_filhos',y='renda',data=renda, ax=ax[2])
#sns.barplot(x='tipo_renda',y='renda',data=renda, ax=ax[3])
#sns.barplot(x='educacao',y='renda',data=renda, ax=ax[4])
#sns.barplot(x='estado_civil',y='renda',data=renda, ax=ax[5])
#sns.barplot(x='tipo_residencia',y='renda',data=renda, ax=ax[6])
sns.despine()
st.pyplot(plt)





