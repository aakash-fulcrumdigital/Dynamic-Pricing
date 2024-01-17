import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Dynamic Price Prediction for Flights")

airline = st.selectbox('Airline',df['airline'].unique())

source_city = st.selectbox('Source City',df['source_city'].unique())

destination_city = st.selectbox('Destination City',df['destination_city'].unique())

departure_time = st.selectbox('Departure Time',df['departure_time'].unique())

arrival_time = st.selectbox('Arrival Time',df['arrival_time'].unique())

stops = st.selectbox('Stops',df['stops'].unique())

travel_class = st.selectbox('Travel Class',df['travel_class'].unique())

duration = st.number_input('Duration')

days_left = st.number_input("Days Left")

if st.button('Predict Price'):
    query = np.array([airline,source_city,destination_city,departure_time,arrival_time,stops,travel_class,duration,days_left])

    query = query.reshape(1,9)
    st.title("Flight Price : " + str(int(pipe.predict(query)[0])))


# ===============================================================

# # Dynamic Pricing Logic
# # def dynamic_price_recommendation(model, input_data):

# #     predicted_price = model.predict(input_data)
    
# #     input_data['Dynamic Price'] = predicted_price

# #     input_data.loc[input_data['Class_Business'] == 1, 'Dynamic Price'] *= 1.1  
# #     return input_data['Dynamic Price']


# # input_data_for_dynamic_pricing = X_test.head(5)  
# # dynamic_prices = dynamic_price_recommendation(model, input_data_for_dynamic_pricing)


# # print("\nDynamic Pricing Recommendations:")
# # print(dynamic_prices)

# # ----------------------------------------------------------

# # # Dynamic Pricing Logic
# # def dynamic_price_recommendation(model, input_data):
# #     # Assuming input_data is a DataFrame with features similar to X
# #     predicted_price = model.predict(input_data)
    
# #     # You can add your own logic here for dynamic pricing adjustments
# #     # Example: Increase price during peak hours
# #     input_data['Dynamic Price'] = predicted_price * 1.2  # 20% increase
    
# #     return input_data['Dynamic Price']

# # # Example usage
# # input_data_for_dynamic_pricing = X_test.head(5)  # Use actual data here
# # dynamic_prices = dynamic_price_recommendation(model, input_data_for_dynamic_pricing)

# # # Display the dynamic pricing recommendations
# # print("\nDynamic Pricing Recommendations:")
# # print(dynamic_prices)









# Flask App
# --------------------------------------------------------------------------------------------
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)
