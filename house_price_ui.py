import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open("C:/Users/matha/Downloads/house_price_model.pkl", 'rb'))

# Load the feature columns
feature_columns = pickle.load(open("C:/Users/matha/Downloads/feature_columns.pkl", 'rb'))

# Title for the app
st.title("House Price Prediction")

# Sidebar inputs for user features
st.sidebar.header('Input House Features')

def user_input_features():
    location = st.sidebar.selectbox('Location', ['Urban', 'Suburban', 'Rural'])
    house_type = st.sidebar.selectbox('House Type', ['Detached', 'Semi-Detached', 'Apartment', 'Townhouse'])
    bedrooms = st.sidebar.slider('Bedrooms', 1, 10, 3)
    bathrooms = st.sidebar.slider('Bathrooms', 1, 5, 2)
    square_footage = st.sidebar.number_input('Square Footage', min_value=500, max_value=10000, value=1500)
    year_built = st.sidebar.slider('Year Built', 1800, 2024, 2000)
    garage = st.sidebar.selectbox('Garage', ['Yes', 'No'])
    garden = st.sidebar.selectbox('Garden', ['Yes', 'No'])
    basement = st.sidebar.selectbox('Basement', ['Yes', 'No'])
    nearby_schools = st.sidebar.slider('Nearby Schools (within 2 miles)', 0, 10, 3)
    crime_rate = st.sidebar.slider('Crime Rate (1-10)', 1, 10, 5)
    distance_to_city_center = st.sidebar.slider('Distance to City Center (miles)', 0, 50, 10)

    # Prepare the data based on the input
    data = {'Location_Urban': int(location == 'Urban'),
            'Location_Suburban': int(location == 'Suburban'),
            'Location_Rural': int(location == 'Rural'),
            'HouseType_Detached': int(house_type == 'Detached'),
            'HouseType_Semi-Detached': int(house_type == 'Semi-Detached'),
            'HouseType_Apartment': int(house_type == 'Apartment'),
            'HouseType_Townhouse': int(house_type == 'Townhouse'),
            'Bedrooms': bedrooms,
            'Bathrooms': bathrooms,
            'SquareFootage': square_footage,
            'YearBuilt': year_built,
            'Garage_Yes': int(garage == 'Yes'),
            'Garden_Yes': int(garden == 'Yes'),
            'Basement_Yes': int(basement == 'Yes'),
            'NearbySchools': nearby_schools,
            'CrimeRate': crime_rate,
            'DistanceToCityCenter': distance_to_city_center}
    
    # Convert data into DataFrame
    features = pd.DataFrame(data, index=[0])
    
    return features

# Input from the user
input_df = user_input_features()

# Reorder the input_df columns to match the feature_columns
input_df = input_df.reindex(columns=feature_columns, fill_value=0)

# Display user input features
st.subheader('User Input Features')
st.write(input_df)

# Predict house price
prediction = model.predict(input_df)

# Display predictions
st.subheader('Predicted House Price')
st.title(f"${ prediction[0]:,.2f}")
