import streamlit as st
import json
from streamlit_lottie import st_lottie

# Page Config
st.set_page_config(page_title="🔄 Ultimate Unit Converter Pro", page_icon="🔢", layout="centered")

# Custom CSS for better styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: #f5f7fa;
            padding: 20px;
            border-radius: 10px;
        }
        .stButton > button {
            background: #4CAF50;
            color: white;
            font-weight: bold;
            padding: 12px;
            border-radius: 10px;
            transition: 0.3s;
        }
        .stButton > button:hover {
            background: #388E3C;
            transform: scale(1.05);
        }
        .result-box {
            background: #e3f2fd;
            color: #000;
            font-size: 18px;
            font-weight: bold;
            padding: 15px;
            border-radius: 12px;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

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
    units = {"Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000, "Inches": 39.37, "Feet": 3.281, "Yards": 1.094, "Miles": 0.000621}
    return value * (units[to_unit] / units[from_unit])

def weight_converter(value, from_unit, to_unit):
    units = {"Kilograms": 1, "Grams": 1000, "Milligrams": 1e6, "Pounds": 2.205, "Ounces": 35.274}
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

def speed_converter(value, from_unit, to_unit):
    units = {"Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.237, "Feet per second": 3.281}
    return value * (units[to_unit] / units[from_unit])

def time_converter(value, from_unit, to_unit):
    units = {"Seconds": 1, "Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400}
    return value * (units[to_unit] / units[from_unit])

# Streamlit UI
st.title("🔢 Ultimate Unit Converter Pro")
st.markdown("<h3 style='color: #FFB400;'>Convert anything instantly! 🚀</h3>", unsafe_allow_html=True)

if lottie_conversion:
    st_lottie(lottie_conversion, height=200, key="conversion")

# Sidebar Selection
conversion_type = st.sidebar.selectbox(
    "🔀 Choose Conversion Type",
    ["📏 Length", "🏋️ Weight", "🔥 Temperature", "💨 Speed", "⏳ Time"]
)

value = st.number_input("🎯 Enter Value", value=0.0, format="%.2f")

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
    elif conversion_type == "💨 Speed":
        from_unit = st.selectbox("🌪 From Unit", list(speed_converter(1, "Meters per second", "Meters per second").keys()))
        to_unit = st.selectbox("🌪 To Unit", list(speed_converter(1, "Meters per second", "Meters per second").keys()))
        result = speed_converter(value, from_unit, to_unit)
    elif conversion_type == "⏳ Time":
        from_unit = st.selectbox("⏱ From Unit", list(time_converter(1, "Seconds", "Seconds").keys()))
        to_unit = st.selectbox("⏱ To Unit", list(time_converter(1, "Seconds", "Seconds").keys()))
        result = time_converter(value, from_unit, to_unit)

    # Display Converted Result
    st.markdown(f"<div class='result-box'>✅ Converted Value: {result:.2f} {to_unit}</div>", unsafe_allow_html=True)
