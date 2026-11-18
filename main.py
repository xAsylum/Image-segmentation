import sys
import csdataset
import matplotlib.pyplot as plt
from cv2.typing import MatLike

dataset = csdataset.create_dataset(
    path='/Users/jakubwieliczko/agh/python/Image-segmentation/data/test',
    datasetType=csdataset.DatasetType.TRAIN,
    datasetSetting=csdataset.DatasetSettings.fullyPreloaded()
)

print(f"Dataset entries: {len(dataset)}")

total_ram_bytes = sum(
    img.nbytes 
    for img in dataset.imgs 
) + sum(
    img.nbytes 
    for img in dataset.masks
)

print(f"Size in RAM: {total_ram_bytes / (1024**2):.2f} MB ({total_ram_bytes} bytes)")

result = dataset[0]
assert(type(result) == tuple)
img, mask = result
plt.imshow(img)
plt.show()