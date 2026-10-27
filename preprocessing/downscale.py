from pathlib import Path
import shutil
import cv2
from cv2.typing import MatLike

PATH = '/Users/jakubwieliczko/agh/python/Image-segmentation/preprocessing'

def downscale_path(read_path: str, write_path: str):
    SCALE = 0.25
    img = cv2.imread(read_path)
    def downscale_image(image: MatLike) -> MatLike:
        height, width = image.shape[:2]
        new_img = cv2.resize(src = image,
                            dsize=(int(SCALE * width), int(SCALE * height)),
                            interpolation=cv2.INTER_NEAREST)
        return new_img

    cv2.imwrite(write_path, downscale_image(img))



import os

sourcePath = Path(os.path.join(PATH, 'dataset'))
targetPath = Path(os.path.join(PATH, 'dataset-compressed-png'))

for path, _, files in os.walk(sourcePath):
    relativeSubpath = Path(path).relative_to(sourcePath)
    targetSubpath = targetPath / relativeSubpath
    for file in files:
        if file.endswith('.png'):
            file = Path(file)
            dst = (targetSubpath / file)
            dst.parent.mkdir(parents=True, exist_ok=True)
            downscale_path(str(path / file), str(targetSubpath / file))
       