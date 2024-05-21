# tests/test_processing.py
import cv2
import unittest
from src.processing import process_image

class TestProcessing(unittest.TestCase):
    
    def test_process_image(self):
        image = cv2.imread('data/input_image.jpg')
        if image is None:
            self.fail("No se pudo cargar la imagen de prueba.")
        
        processed_image = process_image(image)
        self.assertIsNotNone(processed_image)
        self.assertEqual(processed_image.shape, image.shape[:2])

if __name__ == '__main__':
    unittest.main()
