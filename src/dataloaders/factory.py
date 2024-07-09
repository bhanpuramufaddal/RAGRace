from enum import Enum
from src.dataloaders import pubmed

# Create an Enum
class SupportedDatasets(Enum):
  PUBMED = 'pubmed'

def dataloader_factory(dataset, **kwargs):
  if dataset == SupportedDatasets.PUBMED:
    return pubmed.PubMedDataLoader(**kwargs)
  else:
    raise NotImplementedError(dataset + ' is not supported')