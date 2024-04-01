Loan Default with MLflow and DVC

workflow:
- Update config.yaml
- Update secrets.yaml [Optional]
- Update params.yaml
- Update the entity
- Update the configuration manager in src config
- Update the components
- Update the pipeline
- Update the main.py
- Update the dvc.yaml
- MLflow

mlflow.set_tracking_uri()
mlflow.get_tracking_uri()
mlflow.create_experiment()
mlflow.set_experiment()
mlflow.start_run()
mlflow.log_param()
mlflow.log_params()
mlflow.log_metrics()
mlflow.log_artifact()
mlflow.log_artifacts()
mlflow.set_tag()

