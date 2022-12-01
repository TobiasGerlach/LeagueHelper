import pytest
import cv2
import sys
from LeagueHelper.Static import MinimapAnalyzer
from pathlib import Path


class TestMinimapAnalyzer:
    def test_get_champions(self):
        assert False

    def test_find_circles(self):
        media_path = Path(__file__).parent.parent / "media"
        minimap = cv2.imread(str(media_path / "minimap.png"))
        # inRange(image, cv::Scalar(0, 125, 0), cv::Scalar(255, 200, 255), output) 90,20,20 30,60,90
        print(minimap)
        assert False

    def test_determine_champions(self):
        media_path = Path(__file__).parent.parent / "media"
        minimap = cv2.imread(str(media_path / "minimap.png"))
        assert False

    def test_tempalte_matching(self):
        ma = MinimapAnalyzer()
        media_path = Path(__file__).parent.parent / "media"
        minimap = cv2.imread(str(media_path / "minimap.png"))
        template = cv2.imread(str(media_path / "blue_circle.png"))
        ma._tempalte_matching(minimap, template)

        assert False
