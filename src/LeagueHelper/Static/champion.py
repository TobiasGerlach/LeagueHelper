import abc

import cv2
import numpy as np
from LeagueHelper.Static import Ability
from pathlib import Path
import logging


class Champion(metaclass=abc.ABCMeta):
    def __init__(self, name) -> None:
        self._NAME = name
        self.champ_icon = None
        # self._q = Ability()
        # self._w = Ability()
        # self._e = Ability()

        self._level = 1
        self._q_lv = 0
        self._w_lv = 0
        self._e_lv = 0
        self._r_lv = 0
        self._max_health = []
        self._health_regen = []
        self._max_resource = []
        self._resource_regen = []
        self._armor = []
        self._attack_damage = []
        self._magic_resist = []
        self._crit_dmg = []
        self._move_speed = []
        self._attack_range = []

        self._summoner_spells = []
        self._summoner_spells_cooldowns = []
        self._items = []
        self._items_cooldowns = []
        self._get_champ_data()

    @property
    def armor(self):
        return self._armor

    def _get_champ_data(self):
        data_path = Path(__file__).parents[3] / ("data/champions/" + self._NAME)
        if not data_path.is_dir():
            logging.warning("Champion unknown")
            return
        image_path = str(data_path / (self._NAME + "_circle.png"))
        # print(image_path)
        self.champ_icon = cv2.imread(image_path)
        if self.champ_icon is None:
            print(self.champ_icon)
            logging.warning(
                "Could not load image " + str(data_path / (self._NAME + "_circle.png"))
            )
            return
        self._MAX_HEALTH = []
        self._HEALTH_REGEN = []
        self._MAX_RESOURCE = []
        self._RESOURCE_REGEN = []
        self._ARMOR = []
        self._ATTACK_DAMAGE = []
        self._MAGIC_RESIST = []
        self._CRIT_DMG = []
        self._MOVE_SPEED = []
        self._ATTACK_RANGE = []
        self._BASE_AS = None
        self._ATTACK_WINDUP = None
        self._AS_RATIO = None
        self._BONUS_AS = None

        self._GAMEPLAY_RADIUS = None
        self._SELECTION_RADIUS = None
        self._PATHING_RADIUS = None
        self._ACQ_RADIUS = None

    def _calc_physical_dmg(self, dmg, dmg_reduction):
        if self._armor > 0:
            return dmg_reduction * dmg * (100 / (100 + self._armor))
        else:
            return dmg_reduction * dmg * (2 - (100 / (100 - self._armor)))

    def _calc_magical_dmg(self, dmg, dmg_reduction):
        if self._mr > 0:
            return dmg_reduction * dmg * (100 / (100 + self._mr))
        else:
            return dmg_reduction * dmg * (2 - (100 / (100 - self._mr)))

    def _calc_healing(self, dmg):
        pass
