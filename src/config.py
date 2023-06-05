 
import os
import pathlib
import joblib

current_dir = pathlib.Path(__file__).parent.resolve()
dirname = os.path.join(current_dir, 'saved_model')
model = joblib.load(os.path.join(dirname, "pipeline_churn_random_forest.pkl") ) 


