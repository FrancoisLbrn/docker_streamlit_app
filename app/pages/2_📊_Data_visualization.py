import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


st.set_page_config(page_title="Data Visualization", page_icon="📊")

@st.cache_data
def load_data():
    df = sns.load_dataset('titanic')
    return df

selected_option = st.radio("Display", ["Correlation Heatmap", "Class Distribution", "Age Distribution"], horizontal=True)

df = load_data()

if selected_option == "Correlation Heatmap":
    df_encoded = pd.get_dummies(df, drop_first=True)
    st.subheader("Correlation Heatmap")
    corr = df_encoded.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=False, cmap='coolwarm', ax=ax)
    st.pyplot(fig)
    
elif selected_option == "Class Distribution":
    st.subheader("Ticket Class Count")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='pclass', ax=ax)
    st.pyplot(fig)
    
elif selected_option == "Age Distribution":
    st.subheader("Age Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df['age'], kde=True, ax=ax)
    st.pyplot(fig)