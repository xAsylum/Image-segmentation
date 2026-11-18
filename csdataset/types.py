
from enum import Enum

class EntryType(Enum):
    IMG = '_leftImg8bit'
    MASK = '_gtFine_color'

class DatasetType(Enum):
    TRAIN = 'train'
    VAL = 'val'
    TEST = 'test'

class PreloadSetting(Enum):
    NONE=0
    BATCH=1
    ALL=2

class DatasetSetting:
    def __init__(self, *,
            preloadSetting: PreloadSetting,
            batchSize: int|None = None):
        assert(preloadSetting != PreloadSetting.BATCH or batchSize is not None)
        self.preload = preloadSetting
        self.batchSize = batchSize

class DatasetSettings:
    @staticmethod
    def fullyPreloaded():
        return DatasetSetting(preloadSetting=PreloadSetting.ALL)
    
    @staticmethod
    def lazyLoadingForBatches(batchSize: int) -> DatasetSetting:
        return DatasetSetting(preloadSetting=PreloadSetting.BATCH, batchSize=batchSize)

    @staticmethod
    def lazyLoadingForAll() -> DatasetSetting:
        return DatasetSetting(preloadSetting=PreloadSetting.NONE)