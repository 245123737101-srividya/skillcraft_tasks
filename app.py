import pandas as pd
import pickle as pk
import streamlit as st

model = pk.load(open("C:\Users\raith\OneDrive\Desktop\House_price_prediction\House_prediction_model,pkl",'rb'))

st.header('Banglore House Prices Predictor')
data = pd.read_csv('C:\Users\raith\OneDrive\Desktop\House_price_prediction\Cleaned_data.csv')

loc = st.selectbox('choose the location',data['location'].unique())
sqft = st.number_input('enter total sqft')
beds = st.number_input('enter  no of bedrooms')
bath = st.number_input('enter  no of bathrooms')
balc = st.number_input('enter  no of balconies')

input = pd.DataFrame([['Electronic City Phase II',2000.0,3.0, 2.0,3]],columns=['location','total_sqft','bath','balcony','bedrooms'])

if st.button("Predict price"):
    output = model.predict(input)
    out_str = 'price of the House is '+ str(output[0]*100000)