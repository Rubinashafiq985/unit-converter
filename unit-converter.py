import streamlit as st
st.title("UNITCONVERTER APP")

st.markdown("### CNVERTS LENGTH ,WEIGHT AND TIME Instantly ")

category = st.selectbox("choose a category",["LENGTH" ,"WEIGHT","TIME"])

def convert_units(category, value, units):import streamlit as st

# Define unit conversion functions
def length_converter(value, from_unit, to_unit):
    conversions = {
        'meters': 1,
        'kilometers': 0.001,
        'centimeters': 100,
        'millimeters': 1000,
        'miles': 0.000621371,
        'yards': 1.09361,
        'feet': 3.28084,
        'inches': 39.3701
    }
    return value * conversions[to_unit] / conversions[from_unit]

def weight_converter(value, from_unit, to_unit):
    conversions = {
        'kilograms': 1,
        'grams': 1000,
        'pounds': 2.20462,
        'ounces': 35.274
    }
    return value * conversions[to_unit] / conversions[from_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return value * 9/5 + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        return (value - 273.15) * 9/5 + 32
    else:
        return value

# Streamlit UI
st.title("Unit Converter")

# Choose conversion type
conversion_type = st.selectbox('Choose a conversion type:', ['Length', 'Weight', 'Temperature'])

# Length conversion
if conversion_type == 'Length':
    value = st.number_input('Enter the value to convert:')
    from_unit = st.selectbox('From unit:', ['meters', 'kilometers', 'centimeters', 'millimeters', 'miles', 'yards', 'feet', 'inches'])
    to_unit = st.selectbox('To unit:', ['meters', 'kilometers', 'centimeters', 'millimeters', 'miles', 'yards', 'feet', 'inches'])
    if st.button('Convert'):
        result = length_converter(value, from_unit, to_unit)
        st.success(f'{value} {from_unit} = {result:.4f} {to_unit}')

# Weight conversion
elif conversion_type == 'Weight':
    value = st.number_input('Enter the value to convert:')
    from_unit = st.selectbox('From unit:', ['kilograms', 'grams', 'pounds', 'ounces'])
    to_unit = st.selectbox('To unit:', ['kilograms', 'grams', 'pounds', 'ounces'])
    if st.button('Convert'):
        result = weight_converter(value, from_unit, to_unit)
        st.success(f'{value} {from_unit} = {result:.4f} {to_unit}')

# Temperature conversion
elif conversion_type == 'Temperature':
    value = st.number_input('Enter the temperature value:')
    from_unit = st.selectbox('From unit:', ['Celsius', 'Fahrenheit', 'Kelvin'])
    to_unit = st.selectbox('To unit:', ['Celsius', 'Fahrenheit', 'Kelvin'])
    if st.button('Convert'):
        result = temperature_converter(value, from_unit, to_unit)
        st.success(f'{value} {from_unit} = {result:.2f} {to_unit}')
