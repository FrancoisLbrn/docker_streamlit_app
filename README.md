# Docker & Streamlit

# Description
This project showcases the integration of Streamlit and Docker to create a scalable and interactive web application for data science and machine learning purposes.

Streamlit is a powerful open-source framework designed for building and deploying data-driven applications.

In this project, we used Streamlit to create an intuitive interface where users can interact with our machine learning model, upload data, and visualize predictions seamlessly.

On the other hand, Docker allows us to containerize our application, ensuring that it runs consistently across different environments. By using Docker in this project, we ensure that the Streamlit application, along with its dependencies, can be easily run on any platform, enabling smooth collaboration and deployment.

The application will query the API to predict results based on a model that I had previously trained.
The Streamlit APP is composed of 4 pages :
- Main page : where you can load test data `data/test.csv` you can edit and change the data before prediction.
- Explore Data : to have a quick view on the titanic dataset
- Data vizualization : To have some vizualisation.
- Predict Survival : Interactly check if a passenger survived based on the info you provide. 


# Setup

1.  **Clone the Repository:**
    
    ```bash
    git clone https://github.com/FrancoisLbrn/docker_streamlit_app.git
    ```
    or in SSH
    ```bash
    git clone git@github.com:FrancoisLbrn/docker_streamlit_app.git
    ```

# Usage

## Running project with Docker 
In a terminal, execute the following command
1. Create a compose file

        nano docker-compose.yml

2. Copy the following lines of code into the file and save it

        services:
            uvicorn:
                image: francoislbrn/docker_streamlit:uvicorn
                working_dir: /app
                command: poetry run uvicorn api:app --host 0.0.0.0 --port 8000
                ports:
                    - "8000:8000"

            streamlit:
                image: francoislbrn/docker_streamlit:streamlit
                working_dir: /app
                command: poetry run streamlit run streamlit_app.py
                ports:
                    - "8501:8501"


3. Launch the services running this command

        docker compose up

4. Now you can acces the app at clicking on the local_URL which display in the terminal (`http://localhost:8501`)

## Running project Locally
1.  **Install Dependencies:** 

    Make sure you have Poetry installed. Then, navigate to the project directory 

        cd
        

    and run:

        poetry install


2. **Open the dedicated shell**
    
    In the terminal run :

        poetry shell
    
    You must see the virtual environment activated (at the begin of the line)

3. **Launch the API**

    Go to the App folder :

        cd app

    and run the following command to start the API:

        uvicorn api:app

    PS: Need to change in `app/streamlit_app.py` the API URL to begin with `http://localhost:8000`

4. **Check API is running**

    To access the api, go to the url of the swagger :
    ```text 
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

    You should have this result :

    ```text
    {
    "prediction": "survived"
    }
    ```

5. **Launch streamlit app**

    Go back to the terminal in the poetry shell and run 

        streamlit run streamlit_app.py