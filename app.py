import streamlit as st
import json

# Page Configuration
st.set_page_config(page_title="Ultimate Unit Converter", page_icon="🔢", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
        .container {
            background: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
            width: 60%;
            margin: auto;
            text-align: center;
        }
        .formula-box {
            background: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            display: inline-block;
            margin-top: 10px;
            font-weight: bold;
        }
        select, input {
            padding: 8px;
            font-size: 16px;
            border-radius: 5px;
            border: 1px solid #ddd;
        }
        .result {
            font-size: 24px;
            font-weight: bold;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Unit conversion logic
def length_converter(value, from_unit, to_unit):
    units = {
        "Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000,
        "Inches": 39.37, "Feet": 3.281, "Yards": 1.094, "Miles": 0.000621
    }
    return value * (units[to_unit] / units[from_unit])

# UI Layout
st.markdown("<div class='container'>", unsafe_allow_html=True)
st.markdown("## Unit Converter")

# Dropdowns for unit selection
conversion_type = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter Value", value=1.0, format="%.2f")

if conversion_type == "Length":
    from_unit = st.selectbox("From Unit", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet", "Yards", "Miles"])
    to_unit = st.selectbox("To Unit", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet", "Yards", "Miles"])
    result = length_converter(value, from_unit, to_unit)
    formula = f"Multiply the length value by {round((length_converter(1, from_unit, to_unit)), 4)}"
    
    # Display result
    st.markdown(f"<div class='result'>{value} {from_unit} = {round(result, 2)} {to_unit}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='formula-box'>Formula: {formula}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
