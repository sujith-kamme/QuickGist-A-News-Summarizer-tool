from src.code.entity import DataIngestionConfig
from src.code.constants import *
from src.code.utils.common import read_yaml, create_directories

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        keys_filepath = KEYS_FILE_PATH
        ):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.keys = read_yaml(keys_filepath)

        create_directories([self.config.artifacts_root])

    

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.dataset

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir ,
            s3_bucket=config.s3_bucket,
            s3_dataset=config.s3_dataset
        )
        return data_ingestion_config
    
    def get_keys(self):
        keys=self.keys
        return keys