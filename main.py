from src.code.logging import LogTool
from src.code.pipeline.stage1_data_ingestion import DataIngestionPipeline
from src.code.pipeline.stage2_data_import_check import DataValidationPipeline


stage_1="Data Ingestion"

try:
    LogTool.info(f"----------- {stage_1} phase started -----------")
    data_ingestion=DataIngestionPipeline()
    data_ingestion.run()
    LogTool.info(f"----------- {stage_1} phase completed -----------")

except Exception as e:
    LogTool.exception(e)
    raise e


stage_2="Data Validation"

try:
    LogTool.info(f"----------- {stage_2} phase started -----------")
    data_validation=DataValidationPipeline()
    data_validation.run()
    LogTool.info(f"----------- {stage_2} phase completed -----------")

except Exception as e:
    LogTool.exception(e)
    raise e



