from src.ml_project.config.configuration import ConfigurationManager
from src.ml_project.components.model_evaluation import ModelEvaluation
from src.ml_project import logger

STAGE_NAME = "Model Evaluation"

class ModelEvaluationTrainingPipeline:
    def __init___(self):
        pass

    def main(self):

        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.log_into_mlflow()
        except Exception as e:
            raise e
        
 
