import os
from pathlib import Path
import sys
from csdataset.types import EntryType, DatasetType

class DatasetImport:
    
    def __init__(self):
        pass

    def construct_dataset(
            self, 
            masterPath: str,
            datasetType: DatasetType) -> dict[str, dict[EntryType, str]]:
        dataset : dict[str, dict[EntryType, str]] = {}
        for path, _, files in os.walk(masterPath):
            if path.find('/' + datasetType.value +'/') == -1:
                continue
            for file in files:
                if file.endswith('.png'):
                    trimmedName = file.removesuffix('.png')
                    id: str|None = None
                    dataType: EntryType|None = None
                    for type in EntryType:
                        if trimmedName.endswith(str(type.value)):
                            id = trimmedName.removesuffix(str(type.value))
                            dataType = type

                    if id is not None and dataType is not None:
                        if id not in dataset.keys():
                            dataset[id] = {}
                        dataset[id][dataType] = str(Path(masterPath) / Path(path) / Path(file))
        return dataset
