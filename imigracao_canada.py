#!/usr/bin/env python
# coding: utf-8

# # 📊 Imigração da América do Sul para o Canadá (1980 - 2013)
# 
# Este projeto explora os dados de imigração dos países da América do Sul para o Canadá no período de 1980 a 2013, utilizando bibliotecas de visualização em Python.
# 
# Vamos investigar:
# - Quais países mais enviaram imigrantes para o Canadá?
# - Como foi a evolução ano a ano da imigração brasileira?
# - Comparação entre os maiores emissores de imigrantes.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go


# In[12]:


jupyter nbconvert --to script imigracao_canada.ipynb


# In[2]:


# Leitura do dataset
base = pd.read_csv('imigrantes_canada.csv')  # caminho encurtado

# Visualização inicial
base.head()


# In[3]:


# Ajuste do índice e colunas úteis
anos = list(map(str, range(1980, 2014)))
base = base.set_index('País')


# In[4]:


top5 = base.sort_values('Total', ascending=False).head()
top5


# In[5]:


sns.set_theme()
cores = ['#3366CC', '#109618', '#FF9900', '#DC3912', '#990099']
fig, ax = plt.subplots(figsize=(15,7))
sns.barplot(data=top5, y=top5.index, x='Total', orient='h', palette=cores, hue='País')
for p in ax.patches:
    # p.get_width() pega o valor da barra
    ax.text(p.get_width() + 500, p.get_y() + p.get_height() / 2,
            f'{p.get_width()}',  # Formatação do valor
            ha='left', va='center', fontsize=10, color='black')

ax.set_title('5 paises com mais imigracoes para o Canada\n1980-2013', color='black', fontsize=16, loc='left')
ax.set_xlabel('Quantidade de Imigrantes')
ax.set_ylabel('')
plt.tight_layout()
plt.show()


# # Vamos pegar o Brasil para observar como foi a evolucao das imigracoes

# In[6]:


brasil = base.loc['Brasil', anos].astype(int).to_frame().reset_index()
brasil.columns = ['Ano', 'Imigrantes']
brasil['Ano'] = brasil['Ano'].astype(int)


# In[7]:


fig, ax = plt.subplots(figsize=(10,7))
sns.lineplot(data=brasil, x='Ano', y='Imigrantes')
ax.set_ylabel('Quantidade de Imigrantes')
ax.set_xlabel('')
ax.set_title('Imigracao do Brasil para o Canadan\n1980-2013', fontsize=16, loc='left')


# ### Criando grafico interativo com plotly

# In[8]:


fig = px.line(data_frame=brasil, x='Ano', y='Imigrantes', markers='o')
fig.update_traces(line=dict(width=3))
fig.update_layout(
    title='Imigração do Brasil para o Canadá (1980-2013)'
)# engrossa a linha

fig.show()


# ### Comparacao entre paises da America dos Sul

# In[9]:


# Extraindo dados dos países mais relevantes
def preparar_pais(nome):
    df = base.query(f'País == "{nome}"')[anos].T.reset_index()
    df.columns = ['Ano', 'Imigrantes']
    df['Imigrantes'] = df['Imigrantes'].astype(int)
    df['Ano'] = df['Ano'].astype(int)
    return df

argentina = preparar_pais("Argentina")
colombia = preparar_pais("Colômbia")
peru = preparar_pais("Peru")


# In[10]:


# Comparativo
fig, ax = plt.subplots(figsize=(10, 6))
for df, nome, cor in zip([brasil, argentina, colombia, peru], ['Brasil', 'Argentina', 'Colômbia', 'Peru'], ['green', 'blue', 'red', 'orange']):
    ax.plot(df['Ano'], df['Imigrantes'], label=nome, lw=2, color=cor)

ax.set_title('Imigração dos principais países da América do Sul para o Canadá (1980 - 2013)')
ax.set_xlabel('Ano')
ax.set_ylabel('Imigrantes')
ax.legend()
plt.savefig('evolucao_imigracao_brasil.png', dpi=300, bbox_inches='tight')
ax.grid()
plt.show()


# In[11]:


# Filtra e reorganiza os dados
america_do_sul = base.query('Região == "América do Sul"').drop(['Continente', 'Região'], axis=1)
america_do_sul = america_do_sul.sort_values('Total', ascending=False)

# Gráfico horizontal
sns.barplot(data=america_do_sul.head(10), y=america_do_sul.head(10).index, x='Total', orient='h')
plt.title('Top países da América do Sul - Imigração total (1980 - 2013)')
plt.xlabel('Total de Imigrantes')
plt.show()


# ### Conclusões
# 
# - O Brasil foi o 4º maior emissor de imigrantes da América do Sul para o Canadá entre 1980 e 2013.
# - A imigração aumentou especialmente nos anos 2000.
# - A Colômbia e o Peru apresentaram também altos números, com tendências diferentes.
# - Ferramentas como Plotly e Matplotlib facilitam a visualização de padrões temporais e comparativos.
# 
# ---
# 
# 📌 Este projeto demonstrou habilidades com:
# - Análise de dados com Pandas
# - Visualização com Matplotlib, Seaborn e Plotly
# - Criação de gráficos animados
# - Storytelling de dados

# In[ ]:




