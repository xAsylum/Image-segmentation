from pathlib import Path

import cv2
from cv2.typing import MatLike
import matplotlib.pyplot as plt


class Prediction:
    def __init__(self, sample: MatLike, mask: MatLike|None = None):
        if mask is not None:
            assert(sample.shape == mask.shape)
            self._mask = mask
        self._sample = sample

    def show_with_mask(self):
        if mask is None:
            raise Exception('Set mask first!')
        else:
            plt.imshow(self._sample)
            plt.imshow(self._mask, alpha=0.5)
            plt.show()


PATH = '/Users/jakubwieliczko/agh/python/Image-segmentation/data'
MASK ='dataset-compressed-png/gtFine/train/dusseldorf/dusseldorf_000000_000019_gtFine_color.png'
IMG ='leftImg8bit_trainvaltest-compressed-png/leftImg8bit/train/dusseldorf/dusseldorf_000000_000019_leftImg8bit.png'

imgpath = Path(PATH) / Path(IMG)
maskpath = Path(PATH) / Path(MASK)
img = cv2.imread(str(imgpath))
mask = cv2.imread(str(maskpath))

pred = Prediction(img, mask)
pred.show_with_mask()

    