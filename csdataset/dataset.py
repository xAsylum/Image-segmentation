import cv2
from cv2.typing import MatLike
from csdataset.types import DatasetSetting, EntryType, PreloadSetting

class CityScapesDataset:
    def __init__(self,
            datasetSetting: DatasetSetting,
            datasetWithPaths: dict[str, dict[EntryType, str]]):
        self.setting = datasetSetting
        self.paths = []
        self.imgs = []
        self.masks = []
        for key in datasetWithPaths:
            paths = datasetWithPaths.get(key)
            if not paths:
                continue
            img = paths.get(EntryType.IMG)
            mask = paths.get(EntryType.MASK)

            if not img or not mask:
                continue

            self.paths.append((img, mask))
            if self.setting.preload == PreloadSetting.ALL:
                self.imgs.append(
                    cv2.imread(img)
                )
                self.masks.append(
                    cv2.imread(mask)
                )

        assert(len(self.imgs) == len(self.masks))

    def __get__(self, idx:int) -> tuple[MatLike, MatLike] | None:
        if idx >= len(self):
            return None
        match self.setting.preload:
            case PreloadSetting.ALL:
                return self.imgs[idx], self.masks[idx]
            case PreloadSetting.NONE:
                img_path, mask_path = self.paths[idx]
                return cv2.imread(img_path), cv2.imread(mask_path)
            case PreloadSetting.BATCH:
                return self.get_from_batch_preload(idx)
    def __len__(self):
        return len(self.paths)

    def get_from_batch_preload(self, idx):
        pass