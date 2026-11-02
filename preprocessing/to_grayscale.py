import cv2
from pathlib import Path

PATH = Path('D:/segmentation_data/compressed_dataset/leftImg8bit-compressed-png')

def convert_image_to_grayscale(image_path: Path, output_path: Path):
  image = cv2.imread(str(image_path))
  new_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  cv2.imwrite(str(output_path), new_img)


def convert_rgb_images_to_grayscale(source_dir: Path, target_dir:Path):
  target_dir.mkdir(parents=True, exist_ok=True)
  for path in source_dir.rglob("*.png"): #przeszukuje takze podfoldery
    relative_path = path.relative_to(source_dir)
    output_path = target_dir / relative_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    convert_image_to_grayscale(path, output_path)


if __name__ == '__main__':
  """
    1. Ustaw PATH na folder z danymi.
    2. Ustaw source_target_dirs  (ponizszy słownik), tak aby:
    - klucze określały katalog źródłowy z obrazami RGB,
    - wartości określały katalog docelowy dla obrazów grayscale.

    Wszystkie obrazy PNG z wybranych katalogów i ich podfolderów
    zostaną przekonwertowane na skalę szarości.
  """

  source_target_dirs = {
    PATH / 'train/image' : PATH / 'train/grayscale_image',
    PATH / 'val/image' : PATH / 'val/grayscale_image',
    PATH / 'test/image' : PATH / 'test/grayscale_image'
  }

  for source_dir, target_dir in source_target_dirs.items():
    convert_rgb_images_to_grayscale(source_dir, target_dir)
