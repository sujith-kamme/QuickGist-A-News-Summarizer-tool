from src.code.config.config import ConfigurationManager
from src.code.components.data_transformation import DataTransformation
from src.code.logging import LogTool

class DataTransformationPipeline:
    def __init__(self):
        pass
    def run(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.transform()