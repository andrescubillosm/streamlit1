##################################################
## {Description: Capstone project for DS4A Colombia and Eficacia S.A.}
##################################################
## {License_info: Restricted For educational proporses}
##################################################
## Author: {Team 108 DS4A Colombia}
## Copyright: Copyright {2022}, {Efficacia DS APP}
## Credits: [{credit_list: Team 108 :Andres Felipe Garcia, Camilo Gomez, Carlos Andres Cubillos, Ilan Almaza, Luis Miguel Puerto, Ricardo Leon, Ricardo Rodriguez, ; Data from eficacia S.A.; soport Correlation one DS4A colombia}]
## License: {license}
## Version: {mayor}.{minor}.{rel}
## Maintainer: {Unmaintained}
## Email: {contact_email}
## Status: {dev_status: under development}
##################################################



#import libraries

#from turtle import width
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from streamlit_folium import folium_static
import folium
from folium.plugins import HeatMap
import pandas as pd
import branca.colormap as cmp

#SUBMENUS
ANTIOQUIA = 'Medellin','Caucasia','El Bagre','Zaragoza','La Ceja','Rionegro','Bello','Copacabana','Marinilla','Itagui','Envigado','Caldas','Sabaneta','Turbo','Apartadó','Carepa','La Estrella','San Jerónimo','Barbosa','Fredonia','Amagá','Necoclí','La Unión','Carmen De Viboral','Retiro'
#ARAUCA = "Arauca"
ATLANTICO = 'Barranquilla','Soledad','Malambo','Sabanalarga','Candelaria','Galapa','Puerto Colombia','Santo Tomás','Sabanagrande','Palmar De Varela','Baranoa'
#BOGOTADC = "Bogotá"
BOLIVAR = 'Cartagena','Magangue','Arjona','Turbaco','San Juan Nepomuceno','Mompos','Carmen De Bolívar'
BOYACA ='Tunja','Duitama','Sogamoso','Paipa','Chiquinquirá','Villa De Leyva','Samacá','Puerto Boyacá'
CALDAS = 'Manizales','La Dorada','Villamaría','Chinchiná'
#CAQUETA= 'Florencia'
CASANARE = 'Yopal'
CAUCA = 'Popayán','Santander De Quilichao','Puerto Tejada'
CESAR = 'Valledupar','Aguachica','Bosconia','Curumaní'
CHOCO= 'Quibdó'
CORDOBA = 'Montería','Cereté','La Apartada','Lorica','Planeta Rica','Sahagún','Ciénaga De Oro','Tierralta'
CUNDINAMARCA= 'Chía','Girardot','Facatativá','Mosquera','Soacha','Zipaquirá','Madrid','Cajicá','Fusagasugá','La Calera','Ricaurte','Cota','La Mesa','Villeta','Villa De San Diego De Ubate','Chocontá','Funza','Gachancipá','Pacho','Tocancipá','Villa Pinzón','Tocaima'
HUILA = 'Neiva','Pitalito','San Agustín','Campoalegre'
LAGUAJIRA = 'Riohacha','Albania','Fonseca','Maicao','San Juan Del Cesar'
MAGDALENA= 'Santa Marta','Aracataca','Pivijay','El Banco','Ciénaga','Fundación'
META = 'Villavicencio','Restrepo','Acacías'
NARINO = 'Pasto','Ipiales'
NORTEDESANTANDER = 'Cúcuta','Ocaña'
QUINDIO = 'Armenia','Calarca','Montenegro','Quimbaya','La Tebaida','Circasia'
RISARALDA = 'Pereira','Dosquebradas','Santa Rosa De Cabal'
SANTANDER = 'Floridablanca','Bucaramanga','Barrancabermeja','Piedecuesta','San Gil','Cerrito','San Miguel'
SUCRE ='Sincelejo','Corozal','Toluviejo','Coveñas','Sampués','San Onofre'
TOLIMA ='Flandes','Ibagué','Espinal','Melgar'
VALLEDELCAUCA ='Santiago De Cali','Palmira','Jamundí','Guadalajara De Buga','Cartago','Tulúa','Buenaventura','Guacarí','Caicedonia','Zarzal','Yumbo','Bugalagrande','Ginebra','Roldanillo','Sevilla'


#creating horizontal containers
head_dash= st.container()
stats_dash= st.container()
map_dash= st.container()

#addind a description
with head_dash:
    st.image('https://www.eficacia.com.co/wp-content/uploads/2020/05/logo.svg')
    st.title(":card_file_box: Out of Stock Eficacia")
    st.markdown("This dashboard will show information analyzed with the data provided. See each of the sections or tabs on the right side, such as general information, exploratory data analysis, the analysis model used and the conclusions. ")
    st.markdown("The team 108 work with 7 datasets in CSV format were received from the company Eficacia. As show the following table")
    code_table = """
    <table>
<thead>
<tr>
<th style="text-align:left">File</th>
<th>Size in kB</th>
<th>Columns</th>
<th>Rows</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left">Agotados.csv</td>
<td>88553</td>
<td>11</td>
<td>1&#39;364.563</td>
</tr>
<tr>
<td style="text-align:left">Exhibiciones.csv</td>
<td>8456</td>
<td>11</td>
<td>87.357</td>
</tr>
<tr>
<td style="text-align:left">Inventarios.csv</td>
<td>2728</td>
<td>6</td>
<td>62.166</td>
</tr>
<tr>
<td style="text-align:left">Precios.csv</td>
<td>2095</td>
<td>8</td>
<td>32.287</td>
</tr>
<tr>
<td style="text-align:left">Productos.csv</td>
<td>17</td>
<td>7</td>
<td>233</td>
</tr>
<tr>
<td style="text-align:left">PuntosVenta.csv</td>
<td>241</td>
<td>19</td>
<td>1.702</td>
</tr>
<tr>
<td style="text-align:left">Ventas.csv</td>
<td>95767</td>
<td>8</td>
<td>1&#39;397.331</td>
</tr>
</tbody>
</table>

    """
    st.markdown(code_table,unsafe_allow_html=True)
    st.markdown("With this data, several exploratory analysis processes were carried out, resulting in the elimination of columns and some of the data sets, and other datasets were also joined to have a better visualization of the data as shown below.")



#sidebar
st.sidebar.title("Business problem")
st.sidebar.markdown("Business problem: Ensuring product availability on the shelf is essential for today's retail sector, so much so that it is considered a measure of retail performance. Retail is a highly competitive industry, and it is imperative to ensure that products are on the shelf when the customer is buying them.")
st.sidebar.markdown(" Business Impact: Out-of-stocks is a major problem in retailing, as it leads to lost sales and reduced customer loyalty, because the term 'out-of-stocks' is used to describe a situation where a consumer cannot find the product on the shelf at the time, he or she wants to buy it.")
st.sidebar.markdown("Developed by team 108 :globe_with_meridians: for DS4A Colombia cohort 6.")
st.sidebar.markdown(" :copyright: 2022 &copy;")

#Adding datasets
#url_1 = 'https://eficaciadata.s3.amazonaws.com/geodata.csv' # Data of geographic points of the stores
#url_2 = 'https://eficaciadata.s3.amazonaws.com/pro_pre_pdv.csv' # Data of products-Prices-stores
#url_3 = 'https://eficaciadata.s3.amazonaws.com/pre.csv'# Data of prices
#url_4 = 'https://eficaciadata.s3.amazonaws.com/pro.csv' # DATA DE PRODUCTOS
#url_5 = 'https://eficaciadata.s3.amazonaws.com/ago_pdv_pro.csv' # Data of products out stock for store and type of product
#url_6 = 'https://eficaciadata.s3.amazonaws.com/ago.csv' # DATA DE AGOTADOS

url_1 = 'csv/geodata.csv' # Data of geographic points of the stores
url_2 = 'csv/pro_pre_pdv.csv' # Data of products-Prices-stores
url_3 = 'csv/pre.csv'# Data of prices
url_4 = 'csv/pro.csv' # DATA DE PRODUCTOS
url_5 = 'csv/ago_pdv_pro.csv' # Data of products out stock for store and type of product
url_6 = 'csv/ago.csv' # DATA DE AGOTADOS
#uses this instruccion it the data change @st.cache(persist=True)( If you have a different use case where the data does not change so very often, you can simply use this)


#loading data
gea = pd.read_csv(url_1)
data_2 = pd.read_csv(url_2)
data_3 = pd.read_csv(url_3)
data_4 = pd.read_csv(url_4)
data_5 = pd.read_csv(url_5)
data_6 = pd.read_csv(url_6)

#creating selector of data at side bar

#st.sidebar.checkbox("Show Analysis by State or city", True, key=1)

#select_depto = st.sidebar.selectbox('Select a State',pd.unique(gea['Depto']))
#select_ciudad = st.sidebar.selectbox('Select a city',pd.unique(gea['Ciudad']))

#get the state selected in the selectbox
#state_data = data_2[data_2['Depto']]



#location_selection = locations.query("Depto == @select_depto & Ciudad == select_ciudad")
#st.dataframe(location_selection)


#st.write()
with stats_dash:
    st.header('Statistics of principal features from eficacia data')
    st.markdown("The department and city filter affects the graphs and tables displayed in this main section which is intended to give context to the information used. To see more information and project development you can also scroll through the other tabs of this dashboard.")
    st.text('Summary of data of products-prices-stores')
    select_depto = st.selectbox('Select a department of Colombia',
                                ('ANTIOQUIA','ARAUCA','ATLÁNTICO',
                                 'BOGOTA D.C','BOLIVAR','BOYACA',
                                 'CALDAS','CAQUETA','CASANARE',
                                 'CAUCA','CESAR','CHOCO','CORDOBA',
                                 'CUNDINAMARCA','HUILA','LA GUAJIRA',
                                 'MAGDALENA','META','NARIÑO','NORTE DE SANTANDER',
                                 'QUINDÍO','RISARALDA','SANTANDER','SUCRE','TOLIMA','VALLE DEL CAUCA'))
    #select_depto =st.multiselect('Select a State:', options=pd.unique(gea['Depto']))
    #select_ciudad = st.multiselect('Select a city:', options=pd.unique(gea['Ciudad']))
    if select_depto == 'ANTIOQUIA' :
       select_ciudad = st.selectbox(
       'Select a city',(ANTIOQUIA))
    elif select_depto == 'ARAUCA' :
         select_ciudad = 'Arauca'
    elif select_depto == 'ATLÁNTICO':
         select_ciudad = st.selectbox(
         'Select a city',(ATLANTICO))
    elif select_depto == 'BOGOTA D.C' :
         select_ciudad="Bogota"
    elif select_depto == 'BOLIVAR' :
         select_ciudad = st.selectbox(
         'Select a city',(BOLIVAR))
    elif select_depto == 'BOYACA' :
         select_ciudad = st.selectbox(
         'Select a city',(BOYACA))
    elif select_depto == 'CALDAS' :
         select_ciudad = st.selectbox(
         'Select a city',(CALDAS))
    elif select_depto == 'CAQUETA' :
         select_ciudad="Florencia"
    elif select_depto == 'CASANARE' :
         select_ciudad = st.selectbox(
         'Select a city',"Yopal")
    elif select_depto == 'CAUCA' :
         select_ciudad = st.selectbox(
         'Select a city',(CAUCA))
    elif select_depto == 'CESAR' :
         select_ciudad = st.selectbox(
         'Select a city',(CESAR))
    elif select_depto == 'CHOCO' :
         select_ciudad = st.selectbox(
         'Select a city',(CHOCO))
    elif select_depto == 'CORDOBA' :
         select_ciudad = st.selectbox(
         'Select a city',(CORDOBA))
    elif select_depto == 'CUNDINAMARCA' :
         select_ciudad = st.selectbox(
         'Select a city',(CUNDINAMARCA))
    elif select_depto == 'LA GUAJIRA' :
         select_ciudad = st.selectbox(
         'Select a city',(LAGUAJIRA))
    elif select_depto == 'MAGDALENA' :
         select_ciudad = st.selectbox(
         'Select a city',(MAGDALENA))
    elif select_depto == 'META' :
         select_ciudad = st.selectbox(
         'Select a city',(META))
    elif select_depto == 'NARIÑO' :
         select_ciudad = st.selectbox(
         'Select a city',(NARINO))
    elif select_depto == 'NORTE DE SANTANDER' :
         select_ciudad = st.selectbox(
         'Select a city',(NORTEDESANTANDER))
    elif select_depto == 'QUINDÍO' :
         select_ciudad = st.selectbox(
         'Select a city',(QUINDIO))
    elif select_depto == 'RISARALDA' :
         select_ciudad = st.selectbox(
         'Select a city',(RISARALDA))
    elif select_depto == 'SANTANDER':
         select_ciudad = st.selectbox(
         'Select a city',(SANTANDER))
    elif select_depto == 'SUCRE' :
         select_ciudad = st.selectbox(
         'Select a city',(SUCRE))
    elif select_depto == 'TOLIMA' :
         select_ciudad = st.selectbox(
         'Select a city',(TOLIMA))
    elif select_depto == 'VALLE DEL CAUCA' :
         select_ciudad = st.selectbox(
         'Select a city',(VALLEDELCAUCA))

    data_2_fil= data_2.loc[data_2['Ciudad'] == select_ciudad]

    st.write(data_2_fil.head(10))
    st.write(data_2_fil.describe())
    distribution_categ = pd.DataFrame(data_2_fil['Categoria'].value_counts())   #creating a dataframe
    st.bar_chart(distribution_categ)
    st.text('Summary of data of products out stock for store and type of product')
    data_5_fil= data_5.loc[data_5['Ciudad'] == select_ciudad]
    st.write(data_5_fil.describe())
    distribution_ago = pd.DataFrame(data_5_fil['Agotado'].value_counts())   #creating a dataframe
    st.bar_chart(distribution_ago)


#locations = [data_2,data_5]



#map of stores
#token
#px.set_mapbox_access_token(open("https://api.mapbox.com/tokens/v2/risharky?access_token=sk.eyJ1IjoicmlzaGFya3kiLCJhIjoiY2w0eW04cXQ2MzBycTNjcGEyZzdldmo5bSJ9.84xlbi4AmGkF09XOJOGlBw").read())

#giving format to coordinates
gea_2= gea.loc[gea['Ciudad'] == select_ciudad]
gea_2["Lat"] = gea_2["Lat"].apply(lambda x: x.replace(',', '.'))
gea_2["Lon"] = gea_2["Lon"].apply(lambda x: x.replace(',', '.'))
gea_2['Lat'] = gea_2['Lat'].astype(float)
gea_2['Lon'] = gea_2['Lon'].astype(float)
gea_2['latitude'] = gea_2['Lat']
gea_2['longitude'] = gea_2['Lon']


# defing map function

with map_dash:
    st.header('Map of stores from the city ' + select_ciudad.title())
    st.markdown("The dataset of points of sale or 'puntos de venta', given the need for them to have a cartographic representation, several processes were carried out to clean coordinates and assign generic coordinates to points of sale that did not have known coordinates, so that in some cases the locations are accurate to a municipal or city scale, but not the exact location of the store.")



# función del mapa

with map_dash:



    t=(max(gea_2['latitude']))
    g=(max(gea_2['longitude']))

    lat = list(gea_2['latitude'] )
    lon = list(gea_2['longitude'] )
    cadena = list(gea_2["Cadena"])
    ciudad = list(gea_2["Ciudad"])

    base_map = folium.Map(location=[t,g], zoom_start=10)
    linear = cmp.LinearColormap(
    ['#fef0d9', '#fec44f', '#ffff33','#ff7f00','#de2d26'],
    index=[0,100, 500, 1000, 3000],
    vmin=1, vmax=3000,
    caption='Number of Stores' #Caption for Color scale or Legend
    )
    fg = folium.FeatureGroup(name="My Map")
    for lt, ln,sale,ciu in zip(lat, lon, cadena,ciudad):
        fg.add_child(folium.Marker(location=[lt, ln], popup=str(sale)))



    base_map.add_child(fg)

    # call to render Folium map in Streamlit
    linear.add_to(base_map)
    folium_static(base_map)

#def mapa():
#
#    from folium.plugins import MarkerCluster

#    latitude = 5
#    longitude = -73

#    map_tiendas = folium.Map(location=[latitude, longitude], zoom_start=6, tiles="Stamen Toner")

#    marker_cluster = MarkerCluster().add_to(map_tiendas)

#    for Lat, Lon, Ciudad, Cadena in list(
#            zip(
#                gea["Lat"],
#                gea["Lon"],
#                gea["Ciudad"],
#                gea["Cadena"]
#            )
#    ):
#        folium.Marker(location=(Lat, Lon),
#                      popup=f"lat: {Lat}, lon : {Lon}, ciudad: {Ciudad}, cadena : {Cadena}").add_to(marker_cluster)

#    minimap = plugins.MiniMap()
#    map_tiendas.add_child(minimap)
#    folium.LayerControl().add_to(map_tiendas)

    #rendering map in streamlit

#    st_map =st_folium(map_tiendas, width=600)

#st.write(mapa)

