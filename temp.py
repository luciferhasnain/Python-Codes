import streamlit as st

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function to convert Celsius to Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Function to convert Fahrenheit to Kelvin
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

# Function to convert Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Streamlit app
st.title("Temperature Converter")

# Select the conversion type
conversion_type = st.selectbox(
    "Select the conversion type:",
    [
        "Celsius to Fahrenheit",
        "Fahrenheit to Celsius",
        "Celsius to Kelvin",
        "Kelvin to Celsius",
        "Fahrenheit to Kelvin",
        "Kelvin to Fahrenheit"
    ]
)

# Input field for the temperature value
temp_value = st.number_input("Enter the temperature value:", step=0.1)

# Perform the conversion
if temp_value is not None:
    if conversion_type == "Celsius to Fahrenheit":
        result = celsius_to_fahrenheit(temp_value)
        st.write(f"{temp_value} Celsius is equal to {result} Fahrenheit")
        
    elif conversion_type == "Fahrenheit to Celsius":
        result = fahrenheit_to_celsius(temp_value)
        st.write(f"{temp_value} Fahrenheit is equal to {result} Celsius")
        
    elif conversion_type == "Celsius to Kelvin":
        result = celsius_to_kelvin(temp_value)
        st.write(f"{temp_value} Celsius is equal to {result} Kelvin")
        
    elif conversion_type == "Kelvin to Celsius":
        result = kelvin_to_celsius(temp_value)
        st.write(f"{temp_value} Kelvin is equal to {result} Celsius")
        
    elif conversion_type == "Fahrenheit to Kelvin":
        result = fahrenheit_to_kelvin(temp_value)
        st.write(f"{temp_value} Fahrenheit is equal to {result} Kelvin")
        
    elif conversion_type == "Kelvin to Fahrenheit":
        result = kelvin_to_fahrenheit(temp_value)
        st.write(f"{temp_value} Kelvin is equal to {result} Fahrenheit")
