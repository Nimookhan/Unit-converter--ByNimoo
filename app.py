import streamlit as st

# Length conversion function
def length_converter(amount, source_unit, target_unit):
    conversion_factors = {
        'Meters': 1,
        'Centimeters': 100,
        'Kilometers': 0.001,
        'Inches': 39.3701,
        'Feet': 3.28084,
        'Yards': 1.09361,
        'Miles': 0.000621371
    }
    return amount * (conversion_factors[target_unit] / conversion_factors[source_unit])

# Streamlit UI Setup
st.set_page_config(page_title="Smart Unit Converter", page_icon="🔢", layout="centered")

st.title("Smart Unit Converter 🎯")
st.write("Easily convert different measurement units!")

st.markdown("---")

# User input for value
amount = st.number_input("Enter Value:", min_value=0.0, format="%.2f")

# Creating columns for unit selection
col1, col2 = st.columns(2)

with col1:
    source_unit = st.selectbox("From Unit:", ["Meters", "Centimeters", "Kilometers", "Inches", "Feet", "Yards", "Miles"], index=0)

with col2:
    target_unit = st.selectbox("To Unit:", ["Meters", "Centimeters", "Kilometers", "Inches", "Feet", "Yards", "Miles"], index=1)

# Convert button with custom UI
if st.button("Convert 🔄"):
    converted_value = length_converter(amount, source_unit, target_unit)
    st.success(f"✅ {amount} {source_unit} = {converted_value:.2f} {target_unit}")
