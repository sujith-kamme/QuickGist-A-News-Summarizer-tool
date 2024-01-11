from src.code.logging import LogTool
from src.code.pipeline.stage1_data_ingestion import DataIngestionPipeline


stage_phase="Data Ingestion"

try:
    LogTool.info(f"----------- {stage_phase} phase started -----------")
    data_ingestion=DataIngestionPipeline()
    data_ingestion.run()
    LogTool.info(f"----------- {stage_phase} phase completed -----------")

except Exception as e:
    LogTool.exception(e)
    raise e




