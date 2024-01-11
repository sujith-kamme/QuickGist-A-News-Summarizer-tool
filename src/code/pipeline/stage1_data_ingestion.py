from src.code.config.config import ConfigurationManager
from src.code.components.data_ingestion import DataIngestion
from src.code.logging import LogTool

class DataIngestionPipeline:
    def __init__(self):
        pass
    def run(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        aws_keys=config.get_keys()
        data_ingestion = DataIngestion(config=data_ingestion_config,keys=aws_keys)
        data_ingestion.download_file_from_s3()
        data_ingestion.extract_zip_file()