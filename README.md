# Loan Default Prediction Project

This project is aimed at predicting loan default using machine learning techniques. It includes a pipeline for data ingestion, validation, transformation, model training, and evaluation, along with a user interface (UI) for easy interaction, MLflow for tracking experimentation and Docker.


## Setup Instructions

To use this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/premota/Loan_default.git

2. Navigate into the project directory:
    ```bash
   cd Loan-default-prediction

3. Create a virtual environment with Python 3.9 installed:
    ```bash
    python3.9 -m venv <env_name>
    
    OR:

    conda create -p <env_name> python==3.9 -y

4. Activate the virtual environment:
    ```bash
    .\<env_name>\Scripts\activate
    
    OR
    
    conda activate <env_name>/

5. Install the required packages:
    ```bash
    pip install -r requirements.txt

### Running the Pipeline
Once you have set up the environment, you can run the entire pipeline by executing the following command:

6. Run pipeline:
    ```bash
    python main.py

### Launching the User Interface

7. To launch the UI, use the following command:
    ```bash
    streamlit run app.py

    
