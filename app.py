import streamlit as st
import pickle
import numpy as np
import datetime

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Dynamic Price Prediction for Flights")

# Split the layout into two columns
col1, col2 = st.columns(2)

# First column
with col1:
    airline = st.selectbox('Airline',df['airline'].unique())
    source_city = st.selectbox('Source City',df['source_city'].unique())
    destination_city = st.selectbox('Destination City',df['destination_city'].unique())
    departure_time = st.selectbox('Departure Time',df['departure_time'].unique())

# Second column
with col2:
    arrival_time = st.selectbox('Arrival Time',df['arrival_time'].unique())
    stops = st.selectbox('Stops',df['stops'].unique())
    travel_class = st.selectbox('Travel Class',df['travel_class'].unique())
    duration = st.number_input('Duration')
    days_left = st.number_input("Days Left")

# Predict Button
if st.button('Predict Price'):
    output = np.array([airline,source_city,destination_city,departure_time,arrival_time,stops,travel_class,duration,days_left])
    output = output.reshape(1,9)
    st.subheader("Flight Price : " + str(int(pipe.predict(output)[0])))


    base_price = int(pipe.predict(output)[0])
    current_day_of_week = datetime.datetime.now().weekday()
    if current_day_of_week == 2:  # wed
        dynamic_price = int(base_price * 1.1)
    else:
        dynamic_price = base_price

    st.subheader("Flight Price : " + str(dynamic_price))