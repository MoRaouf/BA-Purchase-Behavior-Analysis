"""
A prediction pipeline for the web application.
"""

import os
import sys
import pandas as pd
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
from src.utils import load_pickle_object

from sklearn.preprocessing import OrdinalEncoder




@dataclass
class PredictPipelineConfig:
    preprocessor_path = os.path.join("artifacts","preprocessor.pkl")
    model_path = os.path.join("models","model.pkl")

class PredictPipeline:
    
    def __init__(self):
        self.predict_pipeline_config = PredictPipelineConfig()
    
    def predict(self, predict_data):
        """Get the predictions of the passed data"""

        logging.info("Initiated prediction pipeline")
        try:
            #separate target column
            X= predict_data.copy()

            #preprocess flight_day column
            mapping = {
                        "Monday": 1,
                        "Tuesday": 2,
                        "Wednesday": 3,
                        "Thursday": 4,
                        "Friday": 5,
                        "Saturday": 6,
                        "Sunday": 7,
                    }

            X["flight_day"] = X["flight_day"].map(mapping)

            #load preprocessor
            #load the model
            preprocessor = load_pickle_object(self.predict_pipeline_config.preprocessor_path)

            #preprocess object columns
            obj_cols = ['sales_channel', 'trip_type', 'flight_day', 'route', 'booking_origin']
            X[obj_cols] = preprocessor.fit_transform(X[obj_cols])




            # #preprocess object columns
            # obj_cols = ['sales_channel', 'trip_type', 'flight_day', 'route', 'booking_origin']
            # for colname in obj_cols:
            #     X[colname], _ = X[colname].factorize()

            
            #load the model
            model_pkl = load_pickle_object(self.predict_pipeline_config.model_path)
            model = model_pkl["model_object"]

            #get predictions
            preds = model.predict(X)

            logging.info("Finished prediction pipeline")

            return preds


        except Exception as e:
            raise CustomException(e, sys)