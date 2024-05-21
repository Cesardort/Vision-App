# src/utils.py
import cv2

def load_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"No se pudo encontrar la imagen en la ruta: {image_path}")
    return image
