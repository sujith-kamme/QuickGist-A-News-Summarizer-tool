from src.code.config.config import ConfigurationManager
from src.code.components.data_import_check import DataValidation
from src.code.logging import LogTool

class DataValidationPipeline:
    def __init__(self):
        pass
    def run(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()
        
        