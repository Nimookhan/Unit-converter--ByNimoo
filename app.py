import streamlit as st
import json
from streamlit_lottie import st_lottie

# Page Configuration
st.set_page_config(page_title="🌀 Ultimate Unit Converter Pro", page_icon="🔢", layout="wide")

# Custom CSS for Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f0f9ff, #e0f2f1);
        padding: 20px;
    }
    .stButton > button {
        background: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 12px 18px;
        font-weight: bold;
        transition: 0.3s;
        border: none;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
    }
    .stButton > button:hover {
        background: #388E3C;
        transform: scale(1.05);
    }
    .result-box {
        background: linear-gradient(135deg, #e0f7fa, #80deea);
        color: #004d40;
        font-size: 22px;
        font-weight: bold;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        margin-top: 10px;
    }
    .header {
        text-align: center;
        color: #2E7D32;
        font-weight: bold;
        font-size: 30px;
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
        ("Fahrenheit", "Kelvin"): lambda v: (v - 32) * 5/9 + 273.15,
        ("Kelvin", "Fahrenheit"): lambda v: (v - 273.15) * 9/5 + 32
    }
    return conversions.get((from_unit, to_unit), lambda v: v)(value)

def time_converter(value, from_unit, to_unit):
    units = {"Seconds": 1, "Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400}
    return value * (units[to_unit] / units[from_unit])

def speed_converter(value, from_unit, to_unit):
    units = {"m/s": 1, "km/h": 3.6, "mph": 2.23694}
    return value * (units[to_unit] / units[from_unit])

def volume_converter(value, from_unit, to_unit):
    units = {"Liters": 1, "Milliliters": 1000, "Cubic Meters": 0.001, "Gallons": 0.264172}
    return value * (units[to_unit] / units[from_unit])

def storage_converter(value, from_unit, to_unit):
    units = {"Bytes": 1, "Kilobytes": 1/1024, "Megabytes": 1/(1024**2), "Gigabytes": 1/(1024**3), "Terabytes": 1/(1024**4)}
    return value * (units[to_unit] / units[from_unit])

# UI Header
st.markdown("<h1 class='header'>🌀 Ultimate Unit Converter Pro</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #388E3C; text-align: center;'>📏⚖️🌡️⏳⚡💾 Convert anything instantly! 🚀</h3>", unsafe_allow_html=True)

# Display Animation
if lottie_conversion:
    from streamlit_lottie import st_lottie
    st_lottie(lottie_conversion, height=180, key="conversion")

# Sidebar
st.sidebar.title("⚙️ Settings")
conversion_type = st.sidebar.radio("🔀 Choose Conversion Type", ["📏 Length", "🏋️ Weight", "🔥 Temperature", "⏳ Time", "⚡ Speed", "🛢️ Volume", "💾 Storage"])

# Main Layout with Columns
col1, col2 = st.columns([2, 2])

with col1:
    value = st.number_input("🎯 Enter Value", value=0.0, format="%.2f")

with col2:
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
        from_unit = st.selectbox("⏰ From Unit", ["Seconds", "Minutes", "Hours", "Days"])
        to_unit = st.selectbox("⏰ To Unit", ["Seconds", "Minutes", "Hours", "Days"])
        result = time_converter(value, from_unit, to_unit)
    elif conversion_type == "⚡ Speed":
        from_unit = st.selectbox("🚀 From Unit", ["m/s", "km/h", "mph"])
        to_unit = st.selectbox("🚀 To Unit", ["m/s", "km/h", "mph"])
        result = speed_converter(value, from_unit, to_unit)

st.markdown(f"<div class='result-box'>✅ 🎯 Converted Value: {result:.2f} {to_unit} </div>", unsafe_allow_html=True)
