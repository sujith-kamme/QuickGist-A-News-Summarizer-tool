import os
from src.code.logging import LogTool
from src.code.entity import DataTransformationConfig
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
        
    
    def convert_examples_to_features(self,example_batch):
        input_encodings = self.tokenizer(example_batch['article'] , max_length = 1024, truncation = True)
        
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['highlights'], max_length = 128, truncation = True)
            
        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    
    def transform(self):
        try:
            dataset = load_dataset("csv", data_files={'train': f"{self.config.data_path}/train.csv",
                                                        'test': f"{self.config.data_path}/test.csv",
                                                        'validation': f"{self.config.data_path}/validation.csv"})
            
            if len(dataset['train']) == 0:
                raise ValueError("Empty dataset.")
            
            dataset_pt = dataset.map(self.convert_examples_to_features, batched=True)
            dataset_pt.save_to_disk(os.path.join(self.config.root_dir, "dataset"))
        except Exception as e:
            raise ValueError(f"Error during transformation: {e}")