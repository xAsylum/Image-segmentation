import numpy as np
from PIL import Image
from pathlib import Path
import os

PATH = 'C:/Users/pawwo/Downloads/data'


def find_unique_colors(folder_path):
  colors = set()
  for path in folder_path.glob("*.png"):
    image = Image.open(path).convert("RGB")
    image_array = np.array(image).reshape(-1, 3)
    unique_colors = np.unique(image_array, axis=0)
    colors.update(map(tuple, unique_colors))
  return colors

def create_color_mapping(colors: set):
  color_by_id = {
    255: (0, 0, 0)
  }
  for i, color in enumerate(sorted(colors - {(0, 0, 0)})):
    color_by_id[i] = color

  return color_by_id

def convert_to_single_channel(image_rgb, color_by_id):
  image_rgb = np.array(image_rgb)
  image_single_channel = np.full(image_rgb.shape[:2], 255, dtype=np.uint8)
  for label, color in color_by_id.items():
    pixels = np.all(image_rgb == color, axis=-1)
    image_single_channel[pixels] = label
  return image_single_channel
  
def convert_masks_to_class_ids(source_path: Path, target_path:Path, color_by_id: dict):
  target_path.mkdir(parents=True, exist_ok=True)
  for path in source_path.glob("*.png"):
    image = Image.open(path).convert("RGB")
    mask = convert_to_single_channel(image, color_by_id)
    output_path = target_path / path.name
    Image.fromarray(mask).save(output_path)


if __name__ == '__main__':
  """
    1. Ustaw PATH na folder z danymi.
    2. Kolorowe maski z train/mask i test/mask zostaną przekonwertowane na jednokanałowe maski z identyfikatorami klas.
    Wyniki będą w folderach train/mask_single_channel i test/mask_single_channel.
    Czarny kolor (0, 0, 0) otrzymuje specjalny identyfikator 255.
  """
  source_paths = [
    Path(os.path.join(PATH, 'train/mask')),
    Path(os.path.join(PATH, 'test/mask'))
  ]
  target_paths = [
    Path(os.path.join(PATH, 'train/mask_single_channel')),
    Path(os.path.join(PATH, 'test/mask_single_channel'))
  ]
  colors = find_unique_colors(source_paths[0]) #zakładam, że zbiór treningowy zawiera wszystkie klasy występujące w zbiorze danych
  color_by_id = create_color_mapping(colors)

  for i in range(2):
    convert_masks_to_class_ids(source_paths[i], target_paths[i], color_by_id)


