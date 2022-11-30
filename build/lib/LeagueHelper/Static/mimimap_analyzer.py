from typing import List
import cv2
import numpy as np
from LeagueHelper.Static import Champion


class MinimapAnalyzer:
    def __init__(self, champions: List[Champion]):
        self._champions = champions

    def get_champions(self, minimap: np.array):
        champ_koords = self._find_circles(minimap)
        for champ in self._champions:
            self._determine_champions()

    def _find_circles(self):
        pass

    def _determine_champions(self):
        pass

    def _tempalte_matching(self, minimap: np.array, template: np.array):
        img_gray = cv2.cvtColor(minimap, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

        # Specify a threshold
        threshold = 0.8

        # Store the coordinates of matched area in a numpy array
        loc = np.where(res >= threshold)
