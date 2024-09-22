import streamlit as st
import pandas as pd
from  streamlit_app import model_prediction

st.set_page_config(page_title="Predict Survival", page_icon="🔮")

def get_user_input() -> pd.DataFrame:
    sex = st.selectbox("Sex", [0, 1], format_func=lambda x: 'Male' if x == 1 else 'Female')
    age = st.slider("Age", 0, 99, 25)
    pclass = st.radio("Passenger Class", [1, 2, 3], horizontal=True)
    parch = st.slider("Parents/Children Aboard", 0, 6, 0)

    return [sex, pclass, age, parch]

# Get user input
user_input = get_user_input()

# Make prediction
if st.button("Predict Survival"):
    pred = model_prediction([user_input])
    st.subheader(f"Prediction: {pred}")