import streamlit as st
import pickle
import numpy as np
import datetime
import gdown
import os

if not os.path.exists('model.pkl'):
    gdown.download('https://drive.google.com/uc?id=18bXgJn2BJdlgTYEVAprIXxTl-GB1Gq5i', 'model.pkl', quiet=False)

pipe = pickle.load(open('model.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Function to get or initialize user session data
def get_user_session():
    user_session = st.session_state.get('user_session', {'session_start_time': datetime.datetime.now(), 'total_time_spent': 0})
    return user_session

# Update user session data
def update_user_session():
    user_session = get_user_session()
    current_time = datetime.datetime.now()
    session_duration_minutes = (current_time - user_session['session_start_time']).seconds / 60  # Convert to minutes
    user_session['total_time_spent'] += session_duration_minutes
    user_session['session_start_time'] = current_time
    st.session_state.user_session = user_session


st.title("Dynamic Price Prediction for Flights")

col1, col2 = st.columns(2)

with col1:
    airline = st.selectbox('Airline', df['airline'].unique())
    source_city = st.selectbox('Source City', df['source_city'].unique())
    destination_city = st.selectbox('Destination City', df['destination_city'].unique())
    departure_time = st.selectbox('Departure Time', df['departure_time'].unique())

with col2:
    arrival_time = st.selectbox('Arrival Time', df['arrival_time'].unique())
    stops = st.selectbox('Stops', df['stops'].unique())
    travel_class = st.selectbox('Travel Class', df['travel_class'].unique())
    duration = st.number_input('Duration')
    days_left = st.number_input("Days Left")

# Function to calculate dynamic pricing based on user session time
def calculate_dynamic_price(base_price, total_time_spent):
    # Example: Increase price by 1% for every minute spent on the app
    percentage_increase = total_time_spent / 100
    dynamic_price = int(base_price * (1 + percentage_increase))
    return dynamic_price

update_user_session()  # Update user session data on each interaction

if st.button('Predict Price'):
    output = np.array([airline, source_city, destination_city, departure_time, arrival_time, stops, travel_class, duration, days_left])
    output = output.reshape(1, 9)
    st.subheader("Flight Price : " + str(int(pipe.predict(output)[0])))

    base_price = int(pipe.predict(output)[0])
    
    # Calculate dynamic price based on user session time
    user_session = get_user_session()
    total_time_spent = user_session['total_time_spent']
    dynamic_price = calculate_dynamic_price(base_price, total_time_spent)

    st.subheader("Dynamic Flight Price : " + str(dynamic_price))
