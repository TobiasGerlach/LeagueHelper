import copy
from typing import List
from pathlib import Path
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

    def _get_circles(self, minimap: np.array, color: str):
        if color == "red":
            LOWER_BOUNDS = (35, 45, 210)
            UPPER_BOUNDS = (80, 70, 255)
        elif color == "blue":
            LOWER_BOUNDS = (160, 155, 55)
            UPPER_BOUNDS = (235, 165, 125)
        else:
            raise Exception("Invalid Color")
        im = copy.copy(minimap)
        im = cv2.inRange(im, LOWER_BOUNDS, UPPER_BOUNDS)
        # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        cv2.imshow("ss", im)
        minDist = 7
        param1 = 500
        param2 = 5  # smaller value-> more false circles
        minRadius = 14
        maxRadius = 14
        circles = cv2.HoughCircles(
            im,
            cv2.HOUGH_GRADIENT,
            1,
            minDist,
            param1=param1,
            param2=param2,
            minRadius=minRadius,
            maxRadius=maxRadius,
        )
        return circles

    def _find_circles(self, minimap):

        circles_red = self._get_circles(minimap, "red")
        circles_blue = self._get_circles(minimap, "blue")

        return circles_red, circles_blue

    def _determine_champions(self):
        pass

    def _tempalte_matching(self, minimap: np.array, template: np.array):
        img_gray = cv2.cvtColor(minimap, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

        # Specify a threshold
        threshold = 0.8

        # Store the coordinates of matched area in a numpy array
        loc = np.where(res >= threshold)


if __name__ == "__main__":
    ma = MinimapAnalyzer(champions=0)
    minimap = cv2.imread(
        "C:\\Users\\tobia\\Documents\\Code\\LeagueHelper\\tests\\media\\minimap.png"
    )

    im = ma._find_circles(minimap)
