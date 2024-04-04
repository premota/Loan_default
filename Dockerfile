# Use Python 3.9 Alpine as the base image (my venv was created with python 3.9)
FROM python:3.9-slim-buster

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Install the Python dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Command to run Streamlit application on port 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501"]