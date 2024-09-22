# Python image
FROM python:3.9-slim

COPY pyproject.toml poetry.lock .

# Install poetry using pipx
RUN pip install pipx 
RUN pipx install poetry 

# Add pipx location to the path
ENV PATH="/root/.local/bin:$PATH"

# Install the dependencies
RUN poetry install

COPY . .

# Expose ports for uvicorn and streamlit
EXPOSE 8000 
EXPOSE 8501