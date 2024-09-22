from fastapi import FastAPI
import pickle
from pydantic import BaseModel
from typing import List
from pathlib import Path

MODEL_PATH = "../models/model_titanic.pkl"

def load_model(model_path: str) -> object:
    """
    Function to load the model and return it as object
    :param model_path: str
    :return: model: object
    """
    model_path = Path.cwd() / model_path

    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    return model

class ItemList(BaseModel):
    """
    Class to define the structure of the input data
    """
    instances: List[List[float]]

app = FastAPI()
model = load_model(MODEL_PATH)

@app.get("/")
async def root() -> dict:
    """
    Hello world function to test the api
    """
    return {"message": "Hello World"}

@app.post('/v1/models/my_model:predict')
def predict(input_data: ItemList) -> dict:
    """
    Function to predict the sex of Titanic passengers
    :param input_data: ItemList
    :return: prediction: int
    """

    extracted_list = input_data.instances
    res = model.predict(extracted_list)[0]
    a = 'survived' if res == 'male' else 'not survived'
    return {"prediction": a}
