from dotenv import load_dotenv
import os
from mlflow.sklearn import load_model
from database import engine, get_db, create_db_and_tables
from models import Churn, CreateUpdateChurn 

from sqlalchemy.orm import Session

load_dotenv()

create_db_and_tables()

mlflow_tracking_uri = os.getenv("MLFLOW_TRACKING_URI")
mlflow_s3_endpoint_url = os.getenv("MLFLOW_S3_ENDPOINT_URL")
model_name = os.getenv("MODEL_NAME")
model_version = os.getenv("MODEL_VERSION")
model_uri = os.getenv("MODEL_URI")  
#model = load_model(model_uri)  
model = load_model("saved_model/pipeline_churn_random_forest.pkl")  


