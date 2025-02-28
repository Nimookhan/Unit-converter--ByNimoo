import streamlit as st

def convert_length(value, from_unit, to_unit):
    units = {
        'Meters': 1,
        'Centimeters': 100,
        'Kilometers': 0.001,
        'Inches': 39.3701,
        'Feet': 3.28084
    }
    return value * (units[to_unit] / units[from_unit])

# Streamlit UI
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

st.title("Unit Converter 🔄")
st.write("Convert Length Easily, Google-Style!")

st.markdown("---")

value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

col1, col2 = st.columns(2)

with col1:
    from_unit = st.selectbox("From Unit", ["Meters", "Centimeters", "Kilometers", "Inches", "Feet"], index=0)

with col2:
    to_unit = st.selectbox("To Unit", ["Meters", "Centimeters", "Kilometers", "Inches", "Feet"], index=1)

if st.button("Convert 🛠"):
    result = convert_length(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit} 🚀")
