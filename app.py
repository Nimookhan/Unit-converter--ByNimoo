import streamlit as st
import json
from streamlit_lottie import st_lottie

##       Page Configuration     ##
st.set_page_config(page_title="🎨 Dynamic Unit Converter", page_icon="🔄", layout="centered")

##        Custom CSS Styling for Modern Animated UI        ##
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #2a2a72, #009ffd);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
    }
    .stButton > button {
        background: #ffb400;
        color: white;
        border-radius: 12px;
        padding: 12px;
        font-weight: bold;
        box-shadow: 0 0 10px rgba(255, 180, 0, 0.5);
        transition: all 0.3s ease-in-out;
    }
    .stButton > button:hover {
        background: #ff9800;
        transform: scale(1.08);
    }
    .result-box {
        background: linear-gradient(135deg, #00c9ff, #92fe9d);
        color: #fff;
        font-size: 20px;
        font-weight: bold;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# Function to Load Lottie Animations
def load_lottie_file(filepath):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

# Load Animation
lottie_conversion = load_lottie_file("conversion_animation.json")

# Conversion functions
def length_converter(value, from_unit, to_unit):
    length_units = {"Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000, "Inches": 39.3701, "Feet": 3.28084, "Yards": 1.09361, "Miles": 0.000621371}
    return value * (length_units[to_unit] / length_units[from_unit])

def weight_converter(value, from_unit, to_unit):
    weight_units = {"Kilograms": 1, "Grams": 1000, "Milligrams": 1000000, "Pounds": 2.20462, "Ounces": 35.274}
    return value * (weight_units[to_unit] / weight_units[from_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    conversions = {
        ("Celsius", "Fahrenheit"): lambda v: (v * 9/5) + 32,
        ("Fahrenheit", "Celsius"): lambda v: (v - 32) * 5/9,
        ("Celsius", "Kelvin"): lambda v: v + 273.15,
        ("Kelvin", "Celsius"): lambda v: v - 273.15,
        ("Fahrenheit", "Kelvin"): lambda v: (v - 32) * 5/9 + 273.15,
        ("Kelvin", "Fahrenheit"): lambda v: (v - 273.15) * 9/5 + 32
    }
    return conversions.get((from_unit, to_unit), lambda v: v)(value)

# Streamlit UI
st.title("🌍 *Dynamic & Animated Unit Converter App*")
st.markdown("<h3 style='color: #6C63FF;'>Convert different units with a sleek UI! ✨</h3>", unsafe_allow_html=True)

# Display Animation
if lottie_conversion:
    st_lottie(lottie_conversion, height=200, key="conversion")

# Sidebar
conversion_type = st.sidebar.selectbox("*🔄 Choose Conversion Type*", ["📏 Length", "🏋️ Weight", "🔥 Temperature"])

value = st.number_input("🎯 *Enter Value*", value=0.0, format="%.2f")

if value:
    if conversion_type == "📏 Length":
        from_unit = st.selectbox("📐 *From Unit*", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet", "Yards", "Miles"])
        to_unit = st.selectbox("📐 *To Unit*", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet", "Yards", "Miles"])
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "🏋️ Weight":
        from_unit = st.selectbox("⚖️ *From Unit*", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
        to_unit = st.selectbox("⚖️ *To Unit*", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "🔥 Temperature":
        from_unit = st.selectbox("🌡 *From Unit*", ["Celsius", "Fahrenheit", "Kelvin"])
        to_unit = st.selectbox("🌡 *To Unit*", ["Celsius", "Fahrenheit", "Kelvin"])
        result = temperature_converter(value, from_unit, to_unit)

    # Display Converted Result
    st.markdown(f"<div class='result-box'>✅ Converted Value: {result:.2f} {to_unit}</div>", unsafe_allow_html=True)
