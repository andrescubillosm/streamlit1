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

st.title(":blue_book: Conclusions and  Closing Remarks")
st.markdown("More data to show")

#sidebar
st.sidebar.markdown("Developed by team 108 :globe_with_meridians: for DS4A Colombia cohort 6.")
st.sidebar.markdown(" &copy; 2022 &copy;")


#creating horizontal containers
data_exp=st.container()
why_mod= st.container()
error_ex= st.container()
conclud_final= st.container()



#conclusions about data
with data_exp:
    st.title("Data")
    st.markdown("We are grateful in advance for the efforts made by the company Eficacia and its willingness to assist in the process. ")
    st.markdown("In conclusion, the data show problems with some stores in the collection or updating of information, particularly the small chains, which report products out of stock for longer periods of time than the other chains; the inventory data are necessary for analysis or the possible application of more complex models, but in this case they were discarded because it was not possible to relate them for various reasons.")
    st.markdown("There is a general imbalance in the data, but as mentioned above, it seems to be caused by the point at which the information is collected or reports inventories, prices and others, or by the fact that when data is processed (filtering, cleaning, organizing and joining), there are errors by specific city, by category and by chain, so it is suggested that processes be standardized and automated to eliminate this imbalance and make it easier to implement data management mechanisms.")



#why we used that model
with why_mod:
    st.title("why that model")
    st.markdown("why that model, why dont other")

#error explanation
with error_ex:
    st.title("Error explanation")
    st.markdown("Error explanation")

#conclusions
with error_ex:
    st.title("Conclusions")
    st.markdown("Conclusions")