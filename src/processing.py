# src/processing.py
import cv2
import numpy as np

def process_image(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # gray scale
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)  # Gauss blurr
    edges = cv2.Canny(blurred_image, 50, 150)  # edges with Canny
    return edges
