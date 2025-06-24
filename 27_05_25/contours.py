import cv2
import numpy as np                  
from typing import List
from dataclasses import dataclass

@dataclass
class ContourFinder:
    """
    A class to find contours in an image.
    """

    def __init__(self):
        pass

    def find_contours(self, image: np.ndarray) -> List[np.ndarray]:
        """
        Find contours in the given image.

        Args:
            image (np.ndarray): The input image.

        Returns:
            List[np.ndarray]: A list of contours found in the image.
        """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(blurred, 50, 150)
        contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return contours
from typing import List
import cv2          
