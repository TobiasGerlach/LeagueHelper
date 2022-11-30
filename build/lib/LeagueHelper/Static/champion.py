import abc


class Ability:
    def __init__(self) -> None:

        self._COOLDOWNS = []
        self._MAGIC_DMG = []
        self._PHYSICAL_DMG = []
        self._ABSOLUTE_DMG = []
        self._HEAL = []

        self._cooldown = None
        self._magic_dmg = None
        self._physical_dmg = None
        self._absolute_dmg = None
        self._heal = None
        self._dmg_reduction = 1

    @abc.abstractmethod
    def execute(self):
        pass

    def _calc_physical_dmg(self, dmg, champion):
        if champion.armor > 0:
            return self._dmg_reduction * dmg * (100 / (100 + champion.armor))
        else:
            return self._dmg_reduction * dmg * (2 - (100 / (100 - champion.armor)))

    def _calc_magical_dmg(self, dmg, champion):
        if champion.mr > 0:
            return self._dmg_reduction * dmg * (100 / (100 + champion.mr))
        else:
            return self._dmg_reduction * dmg * (2 - (100 / (100 - champion.mr)))

    def _calc_healing(self, dmg, champion):
        pass


class Champion(metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        self._NAME = []
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

        self._q = Ability()
        self._q = Ability()
        self._q = Ability()

        self._BASE_AS = None
        self._ATTACK_WINDUP = None
        self._AS_RATIO = None
        self._BONUS_AS = None

        self._GAMEPLAY_RADIUS = None
        self._SELECTION_RADIUS = None
        self._PATHING_RADIUS = None
        self._ACQ_RADIUS = None

        self._level = 1
        self._q_lv = 0
        self._w_lv = 0
        self._e_lv = 0
        self._r_lv = 0
        self._name = []
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

    @property
    def armor(self):
        return self._armor


class Ahri(Champion):
    def __init__(self) -> None:
        super().__init__()

    def passive(self):
        self._stacks = 0


if __name__ == "__main__":
    ahri = Ahri()
