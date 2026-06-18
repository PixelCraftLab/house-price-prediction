import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🏠 House Price Prediction")

bedrooms = st.number_input("Bedrooms", min_value=1.0, value=3.0)

bathrooms = st.number_input("Bathrooms", min_value=1.0, value=2.0)

sqft_living = st.number_input("Sqft Living", min_value=100, value=1500)

sqft_lot = st.number_input("Sqft Lot", min_value=100, value=5000)

floors = st.number_input("Floors", min_value=1.0, value=1.0)

condition = st.slider("Condition", 1, 5, 3)

view = st.slider("View", 0, 4, 0)

house_age = st.number_input("House Age", min_value=0, value=20)

if st.button("Predict Price"):

    features = np.array([[
        bedrooms,
        bathrooms,
        sqft_living,
        sqft_lot,
        floors,
        condition,
        view,
        house_age
    ]])

    prediction = model.predict(features)

    st.success(
        f"Predicted House Price: ${prediction[0]:,.2f}"
    )