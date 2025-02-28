import streamlit as st
import json
from streamlit_lottie import st_lottie

# Page Config
st.set_page_config(page_title="🔄 Ultimate Unit Converter Pro", page_icon="🔢", layout="centered")

# Custom CSS for Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        padding: 20px;
        border-radius: 10px;
    }
    .stButton > button {
        background: #ff9800;
        color: white;
        border-radius: 12px;
        padding: 12px;
        font-weight: bold;
        transition: all 0.3s ease-in-out;
    }
    .stButton > button:hover {
        background: #e65100;
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
    }
    </style>
""", unsafe_allow_html=True)

# Load Lottie Animation
def load_lottie_file(filepath):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

lottie_conversion = load_lottie_file("conversion_animation.json")

# Conversion Functions
def length_converter(value, from_unit, to_unit):
    units = {"Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000, "Inches": 39.3701, "Feet": 3.28084, "Yards": 1.09361, "Miles": 0.000621371}
    return value * (units[to_unit] / units[from_unit])

def weight_converter(value, from_unit, to_unit):
    units = {"Kilograms": 1, "Grams": 1000, "Milligrams": 1000000, "Pounds": 2.20462, "Ounces": 35.274}
    return value * (units[to_unit] / units[from_unit])

def temperature_converter(value, from_unit, to_unit):
    conversions = {
        ("Celsius", "Fahrenheit"): lambda v: (v * 9/5) + 32,
        ("Fahrenheit", "Celsius"): lambda v: (v - 32) * 5/9,
        ("Celsius", "Kelvin"): lambda v: v + 273.15,
        ("Kelvin", "Celsius"): lambda v: v - 273.15,
    }
    return conversions.get((from_unit, to_unit), lambda v: v)(value)

def time_converter(value, from_unit, to_unit):
    units = {"Seconds": 1, "Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400}
    return value * (units[to_unit] / units[from_unit])

def data_storage_converter(value, from_unit, to_unit):
    units = {"Bytes": 1, "Kilobytes": 1/1024, "Megabytes": 1/(1024**2), "Gigabytes": 1/(1024**3), "Terabytes": 1/(1024**4)}
    return value * (units[to_unit] / units[from_unit])

# Streamlit UI
st.title("🔄 Ultimate Unit Converter Pro")
st.markdown("<h3 style='color: #FFB400;'>Convert anything instantly! 🚀</h3>", unsafe_allow_html=True)

if lottie_conversion:
    st_lottie(lottie_conversion, height=200, key="conversion")

# Sidebar Options
conversion_type = st.sidebar.selectbox("🔀 Choose Conversion Type", ["📏 Length", "🏋️ Weight", "🔥 Temperature", "⏳ Time", "💾 Data Storage"])

value = st.number_input("🔴 Enter Value", value=0.0, format="%.2f")

if value:
    if conversion_type == "📏 Length":
        from_unit = st.selectbox("📐 From Unit", list(length_converter(1, "Meters", "Meters").keys()))
        to_unit = st.selectbox("📐 To Unit", list(length_converter(1, "Meters", "Meters").keys()))
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "🏋️ Weight":
        from_unit = st.selectbox("⚖️ From Unit", list(weight_converter(1, "Kilograms", "Kilograms").keys()))
        to_unit = st.selectbox("⚖️ To Unit", list(weight_converter(1, "Kilograms", "Kilograms").keys()))
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "🔥 Temperature":
        from_unit = st.selectbox("🌡 From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
        to_unit = st.selectbox("🌡 To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
        result = temperature_converter(value, from_unit, to_unit)
    elif conversion_type == "⏳ Time":
        from_unit = st.selectbox("⏱ From Unit", list(time_converter(1, "Seconds", "Seconds").keys()))
        to_unit = st.selectbox("⏱ To Unit", list(time_converter(1, "Seconds", "Seconds").keys()))
        result = time_converter(value, from_unit, to_unit)
    elif conversion_type == "💾 Data Storage":
        from_unit = st.selectbox("💽 From Unit", list(data_storage_converter(1, "Bytes", "Bytes").keys()))
        to_unit = st.selectbox("💽 To Unit", list(data_storage_converter(1, "Bytes", "Bytes").keys()))
        result = data_storage_converter(value, from_unit, to_unit)
    
    st.markdown(f"<div class='result-box'>✅ Converted Value: {result:.2f} {to_unit}</div>", unsafe_allow_html=True)
