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
        icons = self._get_icon_list_from_circles(champ_koords, minimap)
        champions = [
            self._determine_champion(champ, icons) for champ in self._champions
        ]

    def _get_icon_list_from_circles(self, champ_koords, minimap):
        red = [
            minimap[
                int(koords[1]) - 15 : int(koords[1]) + 15,
                int(koords[0]) - 15 : int(koords[0]) + 15,
            ]
            for koords in champ_koords[0][0]
        ]
        blue = [
            minimap[
                int(koords[1]) - 14 : int(koords[1]) + 17,
                int(koords[0]) - 15 : int(koords[0]) + 16,
            ]
            for koords in champ_koords[1][0]
        ]

        return red, blue

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
        minDist = 7
        param1 = 500
        param2 = 5
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

    def _determine_champion(self, champ, icons):
        red_icons = icons[0]
        blue_icons = icons[1]
        tempalte = cv2.resize(champ.champ_icon, (30, 30))
        min_diff = 1000000000
        for count, ic in enumerate(red_icons):
            ic = cv2.resize(ic, (30, 30))
            diff = cv2.subtract(ic, tempalte).sum()
            if diff < min_diff:
                min_diff = diff
                color_idx, champion_idx = (0, count)
        for count, ic in enumerate(blue_icons):
            ic = cv2.resize(ic, (30, 30))

            diff = cv2.subtract(ic, tempalte).sum()
            if diff < min_diff:
                min_diff = diff
                color_idx, champion_idx = (1, count)
            cv2.imshow("asd", ic)
            cv2.imshow("ggg", tempalte)
            print(diff)
            cv2.waitKey(0)

        print(champ._NAME)
        print(color_idx, "   ", champion_idx)

        color_idx = 0
        champion_idx = 0
        return (color_idx, champion_idx)

    def _tempalte_matching(self, minimap: np.array, template: np.array):
        img_gray = cv2.cvtColor(minimap, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

        # Specify a threshold
        threshold = 0.8

        # Store the coordinates of matched area in a numpy array
        loc = np.where(res >= threshold)


if __name__ == "__main__":
    champions = [
        Champion("KSante"),
        Champion("Azir"),
        Champion("Ahri"),
        Champion("Amumu"),
        Champion("Shyvana"),
        Champion("Jhin"),
        Champion("KaiSa"),
    ]
    ma = MinimapAnalyzer(champions=champions)

    minimap = cv2.imread(
        "C:\\Users\\tobia\\Documents\\Code\\LeagueHelper\\tests\\media\\minimap.png"
    )
    ma.get_champions(minimap)

if __name__ == "__mai0n__":
    NAME = "Ahri"
    data_path = Path(__file__).parents[3] / ("data/champions/" + NAME)
    image_path = str(data_path / (NAME + "_circle.png"))
    # print(image_path)
    champ_icon = cv2.imread(image_path)
    print(champ_icon)
