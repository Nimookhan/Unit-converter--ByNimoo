import streamlit as st
import json

# Page Configuration
st.set_page_config(page_title="Google-Style Unit Converter", page_icon="🔢", layout="centered")

# Custom CSS for Google-like UI
st.markdown(
    """
    <style>
        .stApp {
            background-color: #ffffff;
            font-family: Arial, sans-serif;
        }
        .converter-box {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
        .formula-box {
            background: #fff3cd;
            padding: 10px;
            border-radius: 5px;
            font-size: 16px;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Conversion Dictionaries
length_units = {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Inch": 39.37, "Foot": 3.281, "Yard": 1.094, "Mile": 0.000621}
weight_units = {"Kilogram": 1, "Gram": 1000, "Milligram": 1e6, "Pound": 2.205, "Ounce": 35.274}
time_units = {"Second": 1, "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400}

def convert(value, from_unit, to_unit, unit_dict):
    return value * (unit_dict[to_unit] / unit_dict[from_unit])

# UI Elements
st.title("🔢 Google-Style Unit Converter")
st.write("Quickly convert units just like Google!")

conversion_type = st.selectbox("Choose Conversion Type", ["Length", "Weight", "Time"])

if conversion_type == "Length":
    units = length_units
elif conversion_type == "Weight":
    units = weight_units
elif conversion_type == "Time":
    units = time_units

value = st.number_input("Enter Value", value=1.0, format="%.2f")
from_unit = st.selectbox("From", list(units.keys()))
to_unit = st.selectbox("To", list(units.keys()))

if st.button("Convert"):
    result = convert(value, from_unit, to_unit, units)
    formula = f"Multiply the {conversion_type.lower()} value by {units[to_unit] / units[from_unit]:.4f}"
    
    st.markdown(f"""
        <div class='converter-box'>
            <h2>{value} {from_unit} = {result:.2f} {to_unit}</h2>
            <div class='formula-box'>Formula: {formula}</div>
        </div>
    """, unsafe_allow_html=True)
