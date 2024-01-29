import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Previsão Renda",
     page_icon=":bar_chart:",
     layout="wide",
)

renda = pd.read_csv('./input/previsao_de_renda.csv')
col1, col2 = st.columns([1, 3])

# Coluna 1: Adiciona a imagem
with col1:
    st.image('sunrise.jpg', caption='Vizualização simplificada!', width=145)

# Coluna 2: Adiciona o título e os balões
with col2:
    st.write('# Análise exploratória da previsão de renda')
    st.balloons()

st.write('## Gráficos bivariada')
renda['data_ref'] = pd.to_datetime(renda['data_ref'])
renda['data_ref'] = pd.to_datetime(renda['data_ref'])
media_tempo_emprego = renda.groupby('data_ref')[['tempo_emprego', 'renda']].mean().reset_index()
media_tempo_emprego2 = media_tempo_emprego[0:12].copy()
media_tempo_emprego2['tempo_emprego'] = media_tempo_emprego2['tempo_emprego'].round(2)

plt.figure(figsize=(20, 6))
sns.barplot(x='data_ref', y='renda', hue='tempo_emprego', data=media_tempo_emprego2,palette='viridis', linewidth=2)

tick_labs = renda['data_ref'].dt.strftime("%m-%Y").unique()
ticks = plt.xticks(list(range(renda['data_ref'].nunique())), labels=tick_labs, rotation=0)

sns.despine()
st.pyplot(plt)

st.write('# Análise dos dados')
st.write('Ao expandir o conjunto de variáveis no meu modelo de regressão linear, percebi que o coeficiente de determinação (R²) aumentou, '
         'indicando uma melhoria na capacidade de explicar a variação na renda. Contudo, observei que esse aumento foi acompanhado por coeficientes mais altos para as variáveis incluídas.'
          'Essa relação sugere que a inclusão de mais variáveis está contribuindo para uma explicação mais abrangente da renda, mas também destaca a necessidade de avaliar cuidadosamente a '
          'interpretação dos coeficientes, considerando possíveis problemas como multicolinearidade.'
          'Ao testar o modelo com apenas algumas variáveis, destaco que a variável "tempo_emprego" emergiu como a mais significativa na explicação dos níveis de renda. '
          'Essa descoberta ressalta a importância do tempo de emprego como um fator chave que influencia os rendimentos, indicando que, quanto mais tempo alguém permanece empregado, maior é a tendência de ter uma renda mais elevada.'
          'Além disso, ao aplicar a transformação logarítmica na variável de renda, obtive resultados que indicam uma melhoria na modelagem. Essa abordagem é particularmente útil para lidar com assimetria nos dados, '
          'especialmente em distribuições de renda onde há uma concentração significativa em faixas mais baixas.'
          'Para aprofundar minha análise, estou planejando verificar se as premissas fundamentais do modelo de regressão linear estão sendo atendidas. '
          'Isso inclui a avaliação da normalidade dos resíduos, a verificação da linearidade da relação entre variáveis e renda, a análise da homocedasticidade (variância constante dos resíduos) '
          'e a investigação da presença de multicolinearidade entre as variáveis independentes.'
          'Além disso, estou considerando realizar validação cruzada para avaliar a robustez do modelo em dados não utilizados e conduzir testes de hipóteses para confirmar a significância estatística dos coeficientes.'
          'Essas observações e passos adicionais buscam aprimorar minha compreensão da relação entre variáveis e renda, proporcionando uma análise mais abrangente e confiável do meu modelo de regressão.')

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









