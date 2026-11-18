from csdataset.importer import DatasetImport
from csdataset.types import DatasetType, DatasetSettings, DatasetSetting
from csdataset.dataset import CityScapesDataset

def create_dataset(
        path: str,
        datasetType: DatasetType,
        datasetSetting: DatasetSetting) -> CityScapesDataset:
    importer = DatasetImport()

    datasetPaths = importer.construct_dataset(
        path,
        datasetType
    )

    dataset = CityScapesDataset(
        datasetSetting,
        datasetPaths
    )
    return dataset