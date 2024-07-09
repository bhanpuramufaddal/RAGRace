import os
import numpy as np
import random
import json
from src.dataloaders.base import IDataLoader

class PubMedDataLoader(IDataLoader):
  def __init__(self,
    data_dir,
    tokenizer,
    batch_size = 32,
    max_tokens=2000,
  ):

    self.data_dir = data_dir
    self.batch_size = batch_size
    self.tokenizer = tokenizer
    self.max_tokens = max_tokens

  # Define a generator function to read the data
  def data_generator(self):
    data_dir = self.data_dir
    files = os.listdir(data_dir)
    count = 0
    
    for filename in files:

      if not filename.endswith('.jsonl'):
        continue

      filepath = os.path.join(self.data_dir, filename)
      with open(filepath, 'r') as file:
        data_list = file.readlines()

      for data in data_list:
        data = json.loads(data)

        chunks = self.tokenizer.split_text(data['contents'], self.max_tokens)

        metadata = {
          'PMID': data['PMID'],
          'title': data['title'],
        }

        for chunk in chunks:
          data_dict = {
            'id': count,
            'text': chunk,
            'metadata': metadata,
          }
          count += 1
          yield data_dict
    
  def __len__(self):
    return len(list(self.data_generator()))
  
  def __iter__(self):
    # return by batch
    batch = []
    num_batches = 0
    while True:
      for data in self.data_generator():
        batch.append(data)
        if len(batch) >= self.batch_size:
          yield batch
          num_batches += 1
          batch = []

      if batch:
        yield batch
        num_batches += 1
      
