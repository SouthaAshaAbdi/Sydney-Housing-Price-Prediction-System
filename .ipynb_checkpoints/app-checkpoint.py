import streamlit as st
import pandas as pd
import joblib

model = joblib.load("sydney_house_price_model.pkl")

st.title("Sydney Property Price Prediction")

st.write("Enter the property details below to estimate the sale price.")

suburb = st.selectbox(
    "Suburb",
    ["Surry Hills", "Parramatta", "Penrith"]
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=0,
    max_value=10,
    value=2
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=1,
    max_value=10,
    value=1
)

parking = st.number_input(
    "Parking",
    min_value=0,
    max_value=10,
    value=1
)

property_size = st.number_input(
    "Property Size (m²)",
    min_value=10,
    max_value=2000,
    value=100
)

property_type = st.selectbox(
    "Property Type",
    [
        "Apartment",
        "House",
        "Terrace",
        "Townhouse",
        "Villa",
        "Semi-detached",
        "Studio",
        "Retirement Living",
        "Duplex"
    ]
)

sale_method = st.selectbox(
    "Sale Method",
    [
        "Private treaty",
        "Auction",
        "Prior to auction"
    ]
)

if st.button("Predict Sale Price"):

    new_property = pd.DataFrame({
        "SUBURB": [suburb],
        "BEDROOMS": [bedrooms],
        "BATHROOMS": [bathrooms],
        "PARKING": [parking],
        "PROPERTY_SIZE_M2": [property_size],
        "PROPERTY_TYPE": [property_type],
        "SALE_METHOD": [sale_method]
    })

    prediction = model.predict(new_property)[0]

    st.success(
        f"Predicted Sale Price: ${prediction:,.0f}"
    )