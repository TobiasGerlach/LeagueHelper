import pytest
import cv2
import sys
from LeagueHelper.Static import MinimapAnalyzer



class TestMinimapAnalyzer:
    def test_get_champions(self):
        print(sys.path)
        assert False

    def test_find_circles(self):
        minimap = cv2.imread(
            "C:\\Users\\tobia\\Documents\\Code\\LeagueHelper\\tests\\media\\minimap.png"
        )
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
