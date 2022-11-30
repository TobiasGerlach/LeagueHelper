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
        print(minimap)
        assert False

    def test_determine_champions(self):
        minimap = cv2.imread(
            "C:\\Users\\tobia\\Documents\\Code\\LeagueHelper\\tests\\media\\minimap.png"
        )
        assert False

    def test_tempalte_matching(self):
        ma = MinimapAnalyzer()

        minimap = cv2.imread(
            "C:\\Users\\tobia\\Documents\\Code\\LeagueHelper\\tests\\media\\minimap.png"
        )
        template = cv2.imread(
            "C:\\Users\\tobia\\Documents\\Code\\LeagueHelper\\media\\blue_circle.png"
        )
        ma._tempalte_matching(minimap, template)

        assert False
