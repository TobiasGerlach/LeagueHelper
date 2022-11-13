import time
import numpy as np
import cv2
from mss import mss
from PIL import Image
from pathlib import Path


class ScreenCapture:
    def __init__(self) -> None:
        self._bounding_boxes = {
            "screen": {"top": 0, "left": 0, "width": 2560, "height": 1440},
            "minimap": {"top": 1067, "left": 2188, "width": 372, "height": 373},
            "champions_summary": {
                "top": 0,
                "left": 0,
                "width": 2560,
                "height": 1440,
            },  # 2129 873 431 189
            "champion_status": {
                "top": 0,
                "left": 0,
                "width": 2560,
                "height": 1440,
            },  # 684 1178 1095 291
        }
        self._sct = mss()
        self._frame_screen = None
        self._frame_minimap = None
        self._frame_champions_summary = None
        self._frame_champion_status = None

    def _get_bb_data(self, type: str):
        x_from = self._bounding_boxes[type]["left"]
        x_to = self._bounding_boxes[type]["left"] + self._bounding_boxes[type]["width"]
        y_from = self._bounding_boxes[type]["top"]
        y_to = self._bounding_boxes[type]["height"] + self._bounding_boxes[type]["top"]
        return x_from, x_to, y_from, y_to

    def update(self):
        self._frame_screen = self._sct.grab(self._bounding_boxes["screen"])
        x_from, x_to, y_from, y_to = self._get_bb_data("minimap")
        self._frame_minimap = self._frame_screen[x_from:x_to, y_from:y_to]
        x_from, x_to, y_from, y_to = self._get_bb_data("champions_summary")
        self._frame_champions_summary = self._frame_screen[x_from:x_to, y_from:y_to]
        x_from, x_to, y_from, y_to = self._get_bb_data("champion_status")
        self._frame_champion_status = self._frame_screen[x_from:x_to, y_from:y_to]

    @property
    def frame_screen(self):
        return self._frame_screen

    @property
    def frame_minimap(self):
        return self._frame_minimap

    @property
    def frame_champions_summary(self):
        return self._frame_champions_summary

    @property
    def frame_champion_status(self):
        return self._frame_champion_status


if __name__ == "__main__":
    path_to_dataset = Path("E:\Bilder\Trainingsdaten_lol")
    SC = ScreenCapture()
    SC.update()
    cv2.imshow("test", SC.frame_screen)
