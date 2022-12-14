import time
import numpy as np
import cv2
from mss import mss
from PIL import Image
from pathlib import Path
from LeagueHelper.Static.mimimap_analyzer import MinimapAnalyzer


class ScreenCapture:
    def __init__(self) -> None:
        """Bounding boxes carry data that was extracted by using gimp markers. _get_bb_data can determine the cv2 bounding boxes."""
        self._bounding_boxes = {
            "minimap": {"left": 2188, "top": 1067, "width": 403, "height": 389},
            "champion_status": {
                "left": 691,
                "top": 1235,
                "width": 1086,
                "height": 209,
            },
            "champions_summary": {
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
