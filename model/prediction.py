import math
from pathlib import Path

import cv2
from cv2.typing import MatLike
import matplotlib.pyplot as plt
import numpy as np

from feature import Feature, feature_from_color


class Prediction:
    def __init__(self, sample: MatLike, mask: MatLike|None = None):
        if mask is not None:
            assert(sample.shape == mask.shape)
            self._mask = mask
        self._sample = sample

    def show_with_mask(self):
        if self._mask is None:
            raise Exception('Set mask first!')
        else:
            plt.imshow(self._sample)
            plt.imshow(self._mask, alpha=0.5)
            plt.show()

    def extract_feature(self, feature: Feature, fill_color = [0, 0, 0]):
        compared = np.all(self._mask == feature.get_color(), axis=-1, keepdims=True)
        return np.where(compared, self._sample, fill_color)
        
    def detected_classes(self) -> dict[Feature, int]:
        classes = {}
        for x in range(self._mask.shape[0]):
            for y in range(self._mask.shape[1]):
                feature = (feature_from_color(tuple(self._mask[x, y])))
                if feature in classes.keys():
                    classes[feature] += 1
                else:
                    classes[feature] = 1
        return classes

    def plot_detected_classes(self, fill_color=[0, 0, 0]):
        valid_features = [f for f in self.detected_classes().keys() if f is not None]
        n = len(valid_features)

        if n == 0:
            print("No features detected to plot.")
            return

        cols = min(n, 2)
        rows = math.ceil(n / cols)
        _, axes = plt.subplots(rows, cols, figsize=(2 * cols, 2 * rows))
        axes = np.atleast_1d(axes).flatten()
        for idx, feature in enumerate(valid_features):
            img = self.extract_feature(feature, fill_color)
            axes[idx].imshow(img)
            title = getattr(feature, "name", str(feature))
            axes[idx].set_title(title)
            axes[idx].axis("off")

        for idx in range(n, len(axes)):
            axes[idx].axis("off")
        
        plt.tight_layout()
        plt.show()

    def plot_detected_classes_together(self):
        valid_features = [f for f in self.detected_classes().keys() if f is not None]
        return np.maximum.reduce([self.extract_feature(feature) for feature in valid_features])


# PATH = '/Users/jakubwieliczko/agh/python/Image-segmentation/data'
# MASK ='dataset-compressed-png/gtFine/train/dusseldorf/dusseldorf_000000_000019_gtFine_color.png'
# IMG ='leftImg8bit_trainvaltest-compressed-png/leftImg8bit/train/dusseldorf/dusseldorf_000000_000019_leftImg8bit.png'
# 
# imgpath = Path(PATH) / Path(IMG)
# maskpath = Path(PATH) / Path(MASK)
# img = cv2.imread(str(imgpath))
# mask = cv2.imread(str(maskpath))
# 
# pred = Prediction(img, mask)
# pred.plot_detected_classes([125, 125, 125])


    