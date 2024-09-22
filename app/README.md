# Launch API and Streamlit app

Activate the poetry env of the project :

```bash 
poetry install
poetry shell
```

Then go to the App folder :

```bash
cd app
uvicorn api:app
```

To access the api, go to the url of the swagger :

```bash
http://127.0.0.1:8000/docs
```

In the swagger to predict, go to :

```text
http://127.0.0.1:8000/docs#/default/predict_v1_models_my_model_predict_post
```

In the `request body`, past the following :

```text
{
  "instances": [
    [
      1,1,1,1
    ]
  ]
}
```

and click on `execute`.

We should have this result :

```text
{
  "prediction": "survived"
}
```

Launch dash (in the app folder):

```bash
streamlit run streamlit_app.py
```