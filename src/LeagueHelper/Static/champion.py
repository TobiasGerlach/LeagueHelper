class Champion:
    def __init__(self) -> None:
        self._NAME = []
        self._HEALTH = []
        self._HEALTH_REGEN = []
        self._RESOURCE = []
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

        self._summoner_spells = []
        self._summoner_spells_cooldowns = []
        self._ability_cooldowns = []
        self._items = []
        self._items_cooldowns = []

    def hit_q_ability(self, Champion):
        pass

    def hit_w_ability(self, Champion):
        pass

    def hit_e_ability(self, Champion):
        pass
