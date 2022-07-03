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
from autots import AutoTS
import matplotlib.pyplot as plt
import pandas as pd

st.title(":chart_with_upwards_trend: MODEL")
st.markdown("More data to show")
st.set_option('deprecation.showPyplotGlobalUse', False)

#sidebar
st.sidebar.markdown("Developed by team 108 :globe_with_meridians: for DS4A Colombia cohort 6.")
st.sidebar.markdown(" :copyright: 2022 &copy;")

#creating horizontal containers
Formula_us= st.container()
Model_exp= st.container()
Data__in= st.container()
ga_model= st.container()

#Adding datasets
#url_5 = 'https://eficaciadata.s3.amazonaws.com/ago_pdv_pro.csv' # Data of products out stock for store and type of product
url_5 = 'csv/ago_pdv_pro.csv' # Data of products out stock for store and type of product
#loading data
data_5 = pd.read_csv(url_5)


#formula used
with Formula_us:
     st.title("The Theta Model(statmodels) ")
     st.markdown("For the development of the model, several models were evaluated to identify in which sites or warehouses there could be depleted elements in the inventories of the warehouses, the theta model was selected in the one implemented in the package [statsmodels](https://www.statsmodels.org/devel/index.html) this module is consumed in the package [AutoTS](https://github.com/winedarksea/AutoTS) which is a module for the modeling of time series, this module allows to choose manually or automatically models that allow to establish predictions based on time or date, the models tested are briefly described below. Their results are very similar, for this reason the Theta model was selected, since it presents clearer variations in the predictions.")
     st.markdown("A straightforward forecasting technique is the Theta model of Assimakopoulos and Nikolopoulos (2000), which entails fitting two lines, smoothing the lines with a Simple Exponential Smoother, and then combining the forecasts from the two lines to produce the final forecast.")
     st.markdown(" for more information [model theta](https://www.statsmodels.org/devel/examples/notebooks/generated/theta-model.html)")


#data in
with Data__in:
     st.title("data used ")
     st.markdown("data in ...")




#model explanation
with Model_exp:
    st.title("Time series using AutoTS")
    st.markdown("WHY")
    data_5.Agotado = data_5.Agotado.replace({True: 1, False: 0})
    st.write(data_5.head(3))
    #creating modeles, autoTS tries and get the best model
    #model_list = ['LastValueNaive', 'GLS', 'GLM', 'ETS', 'AverageValueNaive', 'ARIMA', 'Theta', 'ARDL']
    model_list = ['Theta']
    #for performance the max values of tries are 1 and a 1 validation(zero value makes one validation), predidtions for 60 days the frecuency its automatic selected with the data
    model = AutoTS(forecast_length=100, frequency='infer', prediction_interval=0.90, ensemble='simple', model_list=model_list, transformer_list='all', max_generations=1, num_validations=0)
    model = model.fit(data_5, date_col='Fecha', value_col='Agotado', id_col=None)
    prediction = model.predict()
    forecast = prediction.forecast
    # Print the description of the best model
    st.markdown("following thr options of the best model selected")
    st.write(model)
    st.markdown("Out Stock Prediction")
    st.write(forecast)


#graph of the model
with ga_model:
     st.title("Graph of results ")
     st.markdown("Explanation ...")

     #st.subheader('Out Stock Prediction:100 days ahead')
     #fig_mpl, ax_mpl = plt.subplots()
     #data_5['Agotado'].plot(figsize=(15,8), title= 'Out Stock Prediction', fontsize=18, label='Original Data', ax_mpl=ax_mpl)
     #forecast['Agotado'].plot(figsize=(15,8), title= 'Out Stock Prediction', fontsize=18, label='Prediction', ax_mpl=ax_mpl)
     #plt.legend()
     #plt.grid()
     #st.pyplot(fig_mpl)

     st.subheader('Prediction Chart model Theta')

     fig_m2 = prediction.plot(model.df_wide_numeric, remove_zeroes=False)
     st.pyplot(fig_m2)

     st.subheader('Iterations Chart of model Theta' )
     fig_m3 = model.plot_generation_loss()
     st.pyplot(fig_m3)













