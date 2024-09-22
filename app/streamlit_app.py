import streamlit as st
import requests
import pandas as pd
from typing import List
import pandera as pa

API_URL = "http://uvicorn:8000/v1/models/my_model:predict"

SCHEMA = pa.DataFrameSchema({
    "Sex": pa.Column(int, checks=pa.Check.isin([0,1])),
    "Pclass": pa.Column(int, checks=pa.Check.isin([1,2,3]), nullable=False),
    "Age": pa.Column(float, checks=pa.Check.le(100), nullable=True),
    "Parch": pa.Column(int, checks=[pa.Check.ge(0),pa.Check.le(10)]),
},
strict=True,)


def model_prediction(data: List[List[float]]) -> str:
    """
    Function to send data to the API and get the prediction of the model
    :param data:
    :return: str
    """

    response = requests.post(API_URL, json={"instances": data})
    if response.status_code == 200:
        prediction = response.json().get("prediction", "No prediction found")
        return prediction
    else:
        return "Error"


def model_predictions(data: pd.DataFrame) -> pd.DataFrame:
    """
    Function to get multiple predictions if multiples rows are in the data
    :param data: pd.DataFrame
    :return: pd.DataFrame
    """

    list_predict = []
    for i in range(data.shape[0]):
        prediction = model_prediction(data.iloc[[i]].values.tolist())
        list_predict.append(prediction)

    data['prediction'] = list_predict

    return data


def load_data(uploaded_file: str) -> pd.DataFrame or None:
    """
    Load the data from the uploaded file and return it
    :param uploaded_file:
    :return: data: pd.DataFrame or None
    """

    try:
        return pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Error loading the file : {e}")
        return None


def check_format(schema: pa.DataFrameSchema, df: pd.DataFrame) -> bool:
    """
    Pandera to check the dropped data format and return bool
    :param df: pd.DataFrame
    :param schema: pa.DataFrameSchema
    :return: bool
    """

    try:
        schema.validate(df)
        return True
    except pa.errors.SchemaError as exc:
        st.error(exc)


def main():
    """
    Main function to display the Streamlit app

    This function sets up the Streamlit interface for uploading a CSV file,
    editing the data, and making predictions using a pre-trained model.
    It includes:
    - Title and header setup.
    - File uploader for CSV files.
    - Data validation and format checking.
    - Data editor for user interaction.
    - Prediction button to generate model predictions.
    """

    st.title("Titanic Survival Prediction")
    st.header("Upload and Edit Your Data")

    st.title("Upload file")
    uploaded_file = st.file_uploader("Drop file here")

    if uploaded_file is not None:
        df = load_data(uploaded_file)
        if df is not None:
            if check_format(SCHEMA, df):
                edited_df = st.data_editor(df, num_rows="dynamic")
                if not check_format(SCHEMA, edited_df ):
                    st.write("Wrong input format.")
                else :
                    if st.button("Predict"):
                        edited_df = model_predictions(edited_df)
                        st.write(edited_df)
            else:
                st.write("Please upload a CSV file with the correct format.")
    else:
        st.write("Please upload a CSV file to start.")

if __name__ == "__main__":
    main()
