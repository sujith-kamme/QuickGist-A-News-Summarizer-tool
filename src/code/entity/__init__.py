from dataclasses import dataclass #used for creating entities
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    s3_bucket: str
    s3_dataset: str