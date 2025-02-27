import streamlit as st

# Page Configuration
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

# Styling
st.markdown(
    """
    <style>
        .stTitle {
            text-align: center;
            color: #007BFF;
        }
        .stSidebar {
            background-color: #f8f9fa;
            padding: 10px;
            border-radius: 10px;
        }
        .bmi-result {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            padding: 10px;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1 class='stTitle'>BMI Calculator</h1>", unsafe_allow_html=True)

# Sidebar for input
st.sidebar.header("User Input")
gender = st.sidebar.selectbox("Select your gender:", ["Male", "Female"])
height = st.sidebar.slider("Enter your height (in cm):", 100, 250, 175)
weight = st.sidebar.slider("Enter your weight (in kg):", 40, 200, 70)

# Calculate BMI
bmi = weight / ((height / 100) ** 2)

# Determine BMI Category
if bmi < 18.5:
    category = "Underweight"
    color = "#FFC107"  # Yellow
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
    color = "#28A745"  # Green
elif 25 <= bmi < 29.9:
    category = "Overweight"
    color = "#FD7E14"  # Orange
else:
    category = "Obesity"
    color = "#DC3545"  # Red

# Display BMI Result
st.markdown(
    f"<div class='bmi-result' style='background-color: {color}; color: white;'>"
    f"Your BMI is {bmi:.2f} - {category}"
    f"</div>",
    unsafe_allow_html=True
)

# BMI Categories Info
st.markdown("### BMI Categories")
st.info("- **Underweight**: BMI less than 18.5\n"
        "- **Normal weight**: BMI between 18.5 and 24.9\n"
        "- **Overweight**: BMI between 25 and 29.9\n"
        "- **Obesity**: BMI 30 or greater")




