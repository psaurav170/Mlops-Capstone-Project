from mlflow.tracking import MlflowClient

client = MlflowClient()
print([a.path for a in client.list_artifacts("95b1d0859d36464bb32a7dd3719b2425")])
