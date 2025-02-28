import streamlit as st

# Light Theme CSS
st.markdown(
    """
    <style>
        body {
            background-color: #f8f9fa;
            color: #333;
        }
        .stApp {
            background-color: #f8f9fa;
        }
        .title {
            color: #007bff;
            font-size: 30px;
            font-weight: bold;
        }
        .subtitle {
            color: #666;
            font-size: 18px;
        }
        .emoji {
            font-size: 22px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="title">🔢 Unit Converter</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Convert Length, Temperature, and Weight easily! ⚡</p>', unsafe_allow_html=True)

# Length Converter
def length_converter():
    units = {
        'Meters (m)': 1, 'Centimeters (cm)': 0.01, 'Kilometers (km)': 1000,
        'Inches (in)': 0.0254, 'Feet (ft)': 0.3048
    }
    
    st.subheader("📏 Length Converter")
    from_unit = st.selectbox("Convert from:", list(units.keys()))
    to_unit = st.selectbox("Convert to:", list(units.keys()))
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

    if st.button("Convert"):
        meters = value * units[from_unit]
        result = meters / units[to_unit]
        st.success(f"✅ {value} {from_unit} = {result:.2f} {to_unit}")

# Temperature Converter
def temperature_converter():
    st.subheader("🌡️ Temperature Converter")
    temp_units = {"Celsius (°C)": 'c', "Fahrenheit (°F)": 'f', "Kelvin (K)": 'k'}
    
    from_unit = st.selectbox("Convert from:", list(temp_units.keys()))
    to_unit = st.selectbox("Convert to:", list(temp_units.keys()))
    temp = st.number_input("Enter temperature:", format="%.2f")

    if st.button("Convert"):
        f_unit = temp_units[from_unit]
        t_unit = temp_units[to_unit]
        
        if f_unit == 'c':
            result = (temp * 9/5) + 32 if t_unit == 'f' else temp + 273.15 if t_unit == 'k' else temp
        elif f_unit == 'f':
            result = (temp - 32) * 5/9 if t_unit == 'c' else (temp - 32) * 5/9 + 273.15 if t_unit == 'k' else temp
        elif f_unit == 'k':
            result = temp - 273.15 if t_unit == 'c' else (temp - 273.15) * 9/5 + 32 if t_unit == 'f' else temp

        st.success(f"✅ {temp} {from_unit} = {result:.2f} {to_unit}")

# Weight Converter
def weight_converter():
    units = {
        'Kilograms (kg)': 1, 'Grams (g)': 0.001, 'Pounds (lb)': 0.453592,
        'Ounces (oz)': 0.0283495
    }
    
    st.subheader("⚖️ Weight Converter")
    from_unit = st.selectbox("Convert from:", list(units.keys()))
    to_unit = st.selectbox("Convert to:", list(units.keys()))
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

    if st.button("Convert"):
        kg = value * units[from_unit]
        result = kg / units[to_unit]
        st.success(f"✅ {value} {from_unit} = {result:.2f} {to_unit}")

# Main Menu
st.sidebar.title("🛠️ Choose Converter")
option = st.sidebar.radio("", ["📏 Length Converter", "🌡️ Temperature Converter", "⚖️ Weight Converter"])

if option == "📏 Length Converter":
    length_converter()
elif option == "🌡️ Temperature Converter":
    temperature_converter()
elif option == "⚖️ Weight Converter":
    weight_converter()


