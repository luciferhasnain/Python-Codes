import streamlit as st

# Set up the title and description for the calculator
st.title("Simple Calculator from Muhammad Hasnain abbasi")
st.write("This calculator can perform basic arithmetic operations: addition, subtraction, multiplication, and division.")

# Input fields for numbers
number1 = st.text_input("Enter the first number:")
number2 = st.text_input("Enter the second number:")

# Function to validate input and convert to float
def validate_input(value):
    try:
        return float(value), None
    except ValueError:
        return None, "Please enter a valid number."

# Validate inputs
num1, error1 = validate_input(number1)
num2, error2 = validate_input(number2)

# Display error messages if the inputs are invalid
if error1:
    st.error(error1)
if error2:
    st.error(error2)

# Dropdown for selecting an operation
operation = st.selectbox("Select an operation:", ("Add", "Subtract", "Multiply", "Divide"))

# Perform the calculation based on the selected operation, if inputs are valid
if st.button("Calculate"):
    if error1 or error2:
        st.warning("Please make sure both inputs are valid numbers.")
    else:
        if operation == "Add":
            result = num1 + num2
            st.success(f"The result of addition is: {result}")
        elif operation == "Subtract":
            result = num1 - num2
            st.success(f"The result of subtraction is: {result}")
        elif operation == "Multiply":
            result = num1 * num2
            st.success(f"The result of multiplication is: {result}")
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
                st.success(f"The result of division is: {result}")
            else:
                st.error("Error: Division by zero is not allowed.")

        # Generate a simple bar chart to visualize the numbers and result using Streamlit's native plotting
        st.bar_chart({"Values": [num1, num2, result]}, width=0.7)