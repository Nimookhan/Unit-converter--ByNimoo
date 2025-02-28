import streamlit as st

# Conversion Functions
def length_converter(amount, source_unit, target_unit):
    conversion_factors = {
        'Meters': 1, 'Centimeters': 100, 'Kilometers': 0.001,
        'Inches': 39.3701, 'Feet': 3.28084, 'Yards': 1.09361, 'Miles': 0.000621371
    }
    return amount * (conversion_factors[target_unit] / conversion_factors[source_unit])

def weight_converter(amount, source_unit, target_unit):
    conversion_factors = {
        'Kilograms': 1, 'Grams': 1000, 'Pounds': 2.20462, 'Ounces': 35.274
    }
    return amount * (conversion_factors[target_unit] / conversion_factors[source_unit])

def temperature_converter(amount, source_unit, target_unit):
    if source_unit == target_unit:
        return amount
    if source_unit == "Celsius":
        return (amount * 9/5 + 32) if target_unit == "Fahrenheit" else amount + 273.15
    if source_unit == "Fahrenheit":
        return (amount - 32) * 5/9 if target_unit == "Celsius" else (amount - 32) * 5/9 + 273.15
    if source_unit == "Kelvin":
        return (amount - 273.15) if target_unit == "Celsius" else (amount - 273.15) * 9/5 + 32

def time_converter(amount, source_unit, target_unit):
    conversion_factors = {
        'Seconds': 1, 'Minutes': 1/60, 'Hours': 1/3600, 'Days': 1/86400
    }
    return amount * (conversion_factors[target_unit] / conversion_factors[source_unit])

def speed_converter(amount, source_unit, target_unit):
    conversion_factors = {
        'm/s': 1, 'km/h': 3.6, 'mph': 2.23694, 'knots': 1.94384
    }
    return amount * (conversion_factors[target_unit] / conversion_factors[source_unit])

# Streamlit UI
st.set_page_config(page_title="All-in-One Converter", page_icon="🔄", layout="centered")

st.title("All-in-One Unit Converter 🎯")
st.write("Easily convert between different measurement units!")

st.markdown("---")

# Choose Conversion Type
conversion_type = st.radio("Select Conversion Type:", ["Length", "Weight", "Temperature", "Time", "Speed"])

# User input for value
amount = st.number_input("Enter Value:", min_value=0.0, format="%.2f")

# Defining conversion options
conversion_options = {
    "Length": ["Meters", "Centimeters", "Kilometers", "Inches", "Feet", "Yards", "Miles"],
    "Weight": ["Kilograms", "Grams", "Pounds", "Ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Time": ["Seconds", "Minutes", "Hours", "Days"],
    "Speed": ["m/s", "km/h", "mph", "knots"]
}

# Creating columns for unit selection
col1, col2 = st.columns(2)

with col1:
    source_unit = st.selectbox("From Unit:", conversion_options[conversion_type])

with col2:
    target_unit = st.selectbox("To Unit:", conversion_options[conversion_type])

# Convert button with custom UI
if st.button("Convert 🔄"):
    if conversion_type == "Length":
        converted_value = length_converter(amount, source_unit, target_unit)
    elif conversion_type == "Weight":
        converted_value = weight_converter(amount, source_unit, target_unit)
    elif conversion_type == "Temperature":
        converted_value = temperature_converter(amount, source_unit, target_unit)
    elif conversion_type == "Time":
        converted_value = time_converter(amount, source_unit, target_unit)
    elif conversion_type == "Speed":
        converted_value = speed_converter(amount, source_unit, target_unit)

    st.success(f"✅ {amount} {source_unit} = {converted_value:.2f} {target_unit}")
