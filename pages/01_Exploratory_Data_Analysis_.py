##################################################
## {Description: Capstone project for DS4A Colombia and Eficacia S.A.}
##################################################
## {License_info: Restricted For educational proporses}
##################################################
## Author: {Team 108 DS4A Colombia}
## Copyright: Copyright {2022}, {Efficacia DS APP}
## Credits: [{credit_list: Team 108 :Andres Felipe Garcia, Camilo Gomez, Carlos Andres Cubillos , Ilan Almaza, Luis Miguel Puerto, Ricardo Leon, Ricardo Rodriguez, ; Data from eficacia S.A.; soport Correlation one DS4A colombia}]
## License: {license}
## Version: {mayor}.{minor}.{rel}
## Maintainer: {Unmaintained}
## Email: {contact_email}
## Status: {dev_status: under development}
##################################################
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.title(":bar_chart: EXPLORATORY DATA ANALYSIS")
st.markdown("More data to show")

#sidebar
st.sidebar.markdown("Developed by team 108 :globe_with_meridians: for DS4A Colombia cohort 6.")
st.sidebar.markdown(" :copyright: 2022 &copy;")


#creating horizontal containers
Expo_1= st.container()
Expo_2= st.container()
Expo_3= st.container()
Expo_4= st.container()


#Adding datasets
#url_1 = 'https://eficaciadata.s3.amazonaws.com/geodata.csv' # Data of geographic points of the stores
#url_2 = 'https://eficaciadata.s3.amazonaws.com/pro_pre_pdv.csv' # Data of products-Prices-stores
#url_3 = 'https://eficaciadata.s3.amazonaws.com/pre.csv'# Data of prices
#url_4 = 'https://eficaciadata.s3.amazonaws.com/pro.csv' # DATA DE PRODUCTOS
url_5 = 'https://eficaciadata.s3.amazonaws.com/ago_pdv_pro.csv' # Data of products out stock for store and type of product
#url_6 = 'https://eficaciadata.s3.amazonaws.com/ago.csv' # DATA DE AGOTADOS

url_1 = 'csv/geodata.csv' # Data of geographic points of the stores
url_2 = 'csv/pro_pre_pdv.csv' # Data of products-Prices-stores
url_3 = 'csv/pre.csv'# Data of prices
url_4 = 'csv/pro.csv' # DATA DE PRODUCTOS
#url_5 = 'csv/ago_pdv_pro.csv' # Data of products out stock for store and type of product
#url_6 = 'csv/ago.csv' # DATA DE AGOTADOS
#uses this instruccion it the data change @st.cache(persist=True)( If you have a different use case where the data does not change so very often, you can simply use this)

#loading data
gea = pd.read_csv(url_1, sep=';')
data_2 = pd.read_csv(url_2)
data_3 = pd.read_csv(url_3)
data_4 = pd.read_csv(url_4)
data_5 = pd.read_csv(url_5)
#data_6 = pd.read_csv(url_6)


with Expo_1:
    st.title("Exploratory graphs")
    # Grafica del número de eventos de productos agotados registrados por fecha y ciudad (solo las 10 ciudades con más agotados)



top_ciudades = data_5.groupby("Ciudad")['Agotado'].sum().sort_values(ascending= False).head(10).index
agotados_top_ciudades = data_5.loc[data_5['Ciudad'].isin(top_ciudades)]
fig, ax = plt.subplots(figsize = (15,10))
asd = data_5.loc[data_5['Ciudad'].isin(top_ciudades)].pivot_table(
    index = 'Fecha',
    columns = 'Ciudad',
    values = 'Agotado',
    aggfunc = np.sum
).plot(kind = 'line', ax = ax)
ax.set(
    ylabel = 'number',
    title = 'Registered number of stockouts by city and date'
)
st.pyplot(fig)
# Grafica del número de eventos de productos agotados registrados por fecha y Cadena (solo las 10 Cadenas con más agotados)


top_cadenas = data_5.groupby("Cadena")['Agotado'].sum().sort_values(ascending= False).head(10).index
agotados_top_cadenas = data_5.loc[data_5['Cadena'].isin(top_cadenas)]
fig, ax = plt.subplots(figsize = (15,10))
agotados_cadenas = agotados_top_cadenas.loc[data_5['Cadena'].isin(top_cadenas)].pivot_table(
    index = 'Fecha',
    columns = 'Cadena',
    values = 'Agotado',
    aggfunc = np.sum
).plot(kind = 'line', ax = ax)
ax.set(
    ylabel = 'number',
    title = 'Registered number of stockouts by retailer and date'
)
st.pyplot(fig)

#data_7 = data_6.merge(data_4, on = "IDProducto")
#data_7 = data_7.dropna()
st.write(data_2.head(3))

#no trae el atributo linea en el merge revisar datos

#fig, ax = plt.subplots(figsize = (18,10))
#data_7.pivot_table(
#    index = 'Fecha',
#    columns = 'Linea',
#    values = 'Agotado',
#    aggfunc = np.sum
#).plot(kind = 'line', ax = ax)

#st.pyplot(fig)



fig, ax = plt.subplots(figsize = (18,10))
agotados = data_5.loc[data_5['Agotado'] == True]
agotados.pivot_table(
    index = 'Fecha',
    columns ='SubCausal',
    values = 'Agotado',
    aggfunc = np.sum

).plot(kind = 'line', ax = ax)


st.pyplot(fig)
# no es clara esta funcion
#def stockouts_rate(agotados, idpuntoventa):
#    num_total_productos = agotados.loc[agotados['IDPdv'] == idpuntoventa]['IDProducto'].nunique()
#    result = agotados.loc[(agotados['Agotado'] == True)&(agotados['IDPdv'] == idpuntoventa)].groupby('Fecha').apply(lambda df : 100*df['IDProducto'].nunique()/num_total_productos)
#    return result


# Gráfica de tasas de agotados para los 5 puntos de venta con más registros de agotados.
# no se cuales son los datasets usados en esta funcion o si los modificaron generan un error
#number_plots = 5
#pdv_ago = data_6.groupby('IDPdv')['Agotado'].sum().sort_values(ascending = False).head(number_plots).index
#fig, axs = plt.subplots(figsize = (18,25) ,nrows = number_plots)
#for index, pdv in enumerate(pdv_ago):
#    stockouts_rate(data_6,gea).plot(kind = 'line', ax = axs[index])
#    axs[index].set(
#        xlabel = 'Date',
#        ylabel = 'Percentage',
#        title = f'Stockouts rates for shop with id : {data_4}'
#    )
#fig.tight_layout()
#st.pyplot(fig)

