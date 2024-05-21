# src/main.py
import cv2
from processing import process_image

def main():
    image_path = 'data/input_image.jpg'  # Image data 
    image = cv2.imread(image_path)
    
    if image is None:
        print("Error: No se pudo cargar la imagen.")
        return
    
    processed_image = process_image(image)
    cv2.imshow('Processed Image', processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
