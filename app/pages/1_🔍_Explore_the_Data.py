import streamlit as st
import seaborn as sns

st.set_page_config(page_title="Explore the Data", page_icon="🔍")


@st.cache_data
def load_data():
    df = sns.load_dataset('titanic')
    return df

selected_option = st.radio("Display", ["Raw Data", "Statistics", "Missing value"], horizontal=True)

df = load_data()

if selected_option == "Raw Data":
    st.subheader("Raw Titanic Data")
    st.write(df.head())
    
elif selected_option == "Statistics":
    st.subheader("Dataset Summary Statistics")
    st.write(df.describe())
    
elif selected_option == "Missing value":
    st.subheader("Missing Values in the Dataset")
    st.write(df.isnull().sum())