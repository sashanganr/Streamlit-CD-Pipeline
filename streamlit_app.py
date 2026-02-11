import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# Page Configuration
st.set_page_config(page_title="Temperature Predictor", layout="centered")

st.title("🌡️ Temperature Prediction App")
st.write("Enter input values to predict the temperature.")

# Sample Training Data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([30, 32, 34, 36, 38])

# Train Model
model = LinearRegression()
model.fit(X, y)

# User Input
user_input = st.number_input("Enter Day Number:", min_value=1, max_value=10, step=1)

if st.button("Predict"):
    prediction = model.predict([[user_input]])
    st.success(f"The Predicted Temperature is: {prediction[0]:.2f} °C")
