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
    def __init__(self, name) -> None:
        self._NAME = name

        self._q = Ability()
        self._q = Ability()
        self._q = Ability()

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

    def get_champ_data(self):
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


class Aatrox(Champion):
    def __init__(self) -> None:
        super().__init__("Aatrox")


class Ahri(Champion):
    def __init__(self) -> None:
        super().__init__("Ahri")


class Ahri(Champion):
    def __init__(self) -> None:
        super().__init__("Akali")

    def passive(self):
        self._stacks = 0


class Aatrox(Champion):
    def __init__(self) -> None:
        super().__init__("Akshan")


class Akali(Champion):
    def __init__(self) -> None:
        super().__init__("Alistar")


class Akshan(Champion):
    def __init__(self) -> None:
        super().__init__()


class Alistar(Champion):
    def __init__(self) -> None:
        super().__init__()


class Amumu(Champion):
    def __init__(self) -> None:
        super().__init__()


class Anivia(Champion):
    def __init__(self) -> None:
        super().__init__()


class Annie(Champion):
    def __init__(self) -> None:
        super().__init__()


class Aphelios(Champion):
    def __init__(self) -> None:
        super().__init__()


class Ashe(Champion):
    def __init__(self) -> None:
        super().__init__()


class Aurelion(Champion):
    def __init__(self) -> None:
        super().__init__()


class Azir(Champion):
    def __init__(self) -> None:
        super().__init__()


class Bard(Champion):
    def __init__(self) -> None:
        super().__init__()


class BelVeth(Champion):
    def __init__(self) -> None:
        super().__init__()


class Blitzcrank(Champion):
    def __init__(self) -> None:
        super().__init__()


class Brand(Champion):
    def __init__(self) -> None:
        super().__init__()


class Braum(Champion):
    def __init__(self) -> None:
        super().__init__()


class Caitlyn(Champion):
    def __init__(self) -> None:
        super().__init__()


class Camille(Champion):
    def __init__(self) -> None:
        super().__init__()


class Cassiopeia(Champion):
    def __init__(self) -> None:
        super().__init__()


class ChoGath(Champion):
    def __init__(self) -> None:
        super().__init__()


class Corki(Champion):
    def __init__(self) -> None:
        super().__init__()


class Darius(Champion):
    def __init__(self) -> None:
        super().__init__()


class Diana(Champion):
    def __init__(self) -> None:
        super().__init__()


class DrMundo(Champion):
    def __init__(self) -> None:
        super().__init__()


class Draven(Champion):
    def __init__(self) -> None:
        super().__init__()


class Ekko(Champion):
    def __init__(self) -> None:
        super().__init__()


class Elise(Champion):
    def __init__(self) -> None:
        super().__init__()


class Evelynn(Champion):
    def __init__(self) -> None:
        super().__init__()


class Ezrael(Champion):
    def __init__(self) -> None:
        super().__init__()


class Fiddlesticks(Champion):
    def __init__(self) -> None:
        super().__init__()


class Fiora(Champion):
    def __init__(self) -> None:
        super().__init__()


class Fizz(Champion):
    def __init__(self) -> None:
        super().__init__()


class Galio(Champion):
    def __init__(self) -> None:
        super().__init__()


class Gangplank(Champion):
    def __init__(self) -> None:
        super().__init__()


class Garen(Champion):
    def __init__(self) -> None:
        super().__init__()


class Gnar(Champion):
    def __init__(self) -> None:
        super().__init__()


class Gragas(Champion):
    def __init__(self) -> None:
        super().__init__()


class Graves(Champion):
    def __init__(self) -> None:
        super().__init__()


class Gwen(Champion):
    def __init__(self) -> None:
        super().__init__()


class Hecarim(Champion):
    def __init__(self) -> None:
        super().__init__()


class Heimerdinger(Champion):
    def __init__(self) -> None:
        super().__init__()


class Illaoi(Champion):
    def __init__(self) -> None:
        super().__init__()


class Irelia(Champion):
    def __init__(self) -> None:
        super().__init__()


class Ivern(Champion):
    def __init__(self) -> None:
        super().__init__()


class Janna(Champion):
    def __init__(self) -> None:
        super().__init__()


class Jarvan(Champion):
    def __init__(self) -> None:
        super().__init__()


class Jax(Champion):
    def __init__(self) -> None:
        super().__init__()


class Jayce(Champion):
    def __init__(self) -> None:
        super().__init__()


class Jhin(Champion):
    def __init__(self) -> None:
        super().__init__()


class Jinx(Champion):
    def __init__(self) -> None:
        super().__init__()


class KSante(Champion):
    def __init__(self) -> None:
        super().__init__()


class Kaisa(Champion):
    def __init__(self) -> None:
        super().__init__()


class Kalista(Champion):
    def __init__(self) -> None:
        super().__init__()


class Karma(Champion):
    def __init__(self) -> None:
        super().__init__()


class Karthus(Champion):
    def __init__(self) -> None:
        super().__init__()


class Kassadin(Champion):
    def __init__(self) -> None:
        super().__init__()


class Katarina(Champion):
    def __init__(self) -> None:
        super().__init__()


class Kayle(Champion):
    def __init__(self) -> None:
        super().__init__()


class Kayn(Champion):
    def __init__(self) -> None:
        super().__init__()


class Kennen(Champion):
    def __init__(self) -> None:
        super().__init__()


class KhaZix(Champion):
    def __init__(self) -> None:
        super().__init__()


class Kindred(Champion):
    def __init__(self) -> None:
        super().__init__()


class Kled(Champion):
    def __init__(self) -> None:
        super().__init__()


class KogMaw(Champion):
    def __init__(self) -> None:
        super().__init__()


class LeBlanc(Champion):
    def __init__(self) -> None:
        super().__init__()


class LeeSin(Champion):
    def __init__(self) -> None:
        super().__init__()


class Leona(Champion):
    def __init__(self) -> None:
        super().__init__()


class Lillia(Champion):
    def __init__(self) -> None:
        super().__init__()


class Lissandra(Champion):
    def __init__(self) -> None:
        super().__init__()


class Lucian(Champion):
    def __init__(self) -> None:
        super().__init__()


class Lulu(Champion):
    def __init__(self) -> None:
        super().__init__()


class Lux(Champion):
    def __init__(self) -> None:
        super().__init__()


class Malphite(Champion):
    def __init__(self) -> None:
        super().__init__()


class Malzahar(Champion):
    def __init__(self) -> None:
        super().__init__()


class Maokai(Champion):
    def __init__(self) -> None:
        super().__init__()


class MasterYi(Champion):
    def __init__(self) -> None:
        super().__init__()


class MissFortune(Champion):
    def __init__(self) -> None:
        super().__init__()


class Mordekaiser(Champion):
    def __init__(self) -> None:
        super().__init__()


class Morgana(Champion):
    def __init__(self) -> None:
        super().__init__()


class Nami(Champion):
    def __init__(self) -> None:
        super().__init__()


class Nasus(Champion):
    def __init__(self) -> None:
        super().__init__()


class Nautilus(Champion):
    def __init__(self) -> None:
        super().__init__()


class Neeko(Champion):
    def __init__(self) -> None:
        super().__init__()


class Nidalee(Champion):
    def __init__(self) -> None:
        super().__init__()


class Nilah(Champion):
    def __init__(self) -> None:
        super().__init__()


class Nocturne(Champion):
    def __init__(self) -> None:
        super().__init__()


class Nunu(Champion):
    def __init__(self) -> None:
        super().__init__()


class Olaf(Champion):
    def __init__(self) -> None:
        super().__init__()


class Orianna(Champion):
    def __init__(self) -> None:
        super().__init__()


class Ornn(Champion):
    def __init__(self) -> None:
        super().__init__()


class Pantheon(Champion):
    def __init__(self) -> None:
        super().__init__()


class Poppy(Champion):
    def __init__(self) -> None:
        super().__init__()


class Pyke(Champion):
    def __init__(self) -> None:
        super().__init__()


class Qiyana(Champion):
    def __init__(self) -> None:
        super().__init__()


class Quinn(Champion):
    def __init__(self) -> None:
        super().__init__()


class Rakan(Champion):
    def __init__(self) -> None:
        super().__init__()


class Rammus(Champion):
    def __init__(self) -> None:
        super().__init__()


class RekSai(Champion):
    def __init__(self) -> None:
        super().__init__()


class Rell(Champion):
    def __init__(self) -> None:
        super().__init__()


class Renata(Champion):
    def __init__(self) -> None:
        super().__init__()


class Renekton(Champion):
    def __init__(self) -> None:
        super().__init__()


class Rengar(Champion):
    def __init__(self) -> None:
        super().__init__()


class Riven(Champion):
    def __init__(self) -> None:
        super().__init__()


class Rumble(Champion):
    def __init__(self) -> None:
        super().__init__()


class Ryze(Champion):
    def __init__(self) -> None:
        super().__init__()


class Samira(Champion):
    def __init__(self) -> None:
        super().__init__()


class Sejuani(Champion):
    def __init__(self) -> None:
        super().__init__()


class Senna(Champion):
    def __init__(self) -> None:
        super().__init__()


class Seraphine(Champion):
    def __init__(self) -> None:
        super().__init__()


class Sett(Champion):
    def __init__(self) -> None:
        super().__init__()


class Shaco(Champion):
    def __init__(self) -> None:
        super().__init__()


class Shen(Champion):
    def __init__(self) -> None:
        super().__init__()


class Shyvana(Champion):
    def __init__(self) -> None:
        super().__init__()


class Singed(Champion):
    def __init__(self) -> None:
        super().__init__()


class Sion(Champion):
    def __init__(self) -> None:
        super().__init__()


class Sivir(Champion):
    def __init__(self) -> None:
        super().__init__()


class Skarner(Champion):
    def __init__(self) -> None:
        super().__init__()


class Sona(Champion):
    def __init__(self) -> None:
        super().__init__()


class Soraka(Champion):
    def __init__(self) -> None:
        super().__init__()


class Swain(Champion):
    def __init__(self) -> None:
        super().__init__()


class Sylas(Champion):
    def __init__(self) -> None:
        super().__init__()


class Syndra(Champion):
    def __init__(self) -> None:
        super().__init__()


class Tahm(Champion):
    def __init__(self) -> None:
        super().__init__()


class Taliyah(Champion):
    def __init__(self) -> None:
        super().__init__()


class Talon(Champion):
    def __init__(self) -> None:
        super().__init__()


class Taric(Champion):
    def __init__(self) -> None:
        super().__init__()


class Teemo(Champion):
    def __init__(self) -> None:
        super().__init__()


class Thresh(Champion):
    def __init__(self) -> None:
        super().__init__()


class Tristana(Champion):
    def __init__(self) -> None:
        super().__init__()


class Trundle(Champion):
    def __init__(self) -> None:
        super().__init__()


class Tryndamere(Champion):
    def __init__(self) -> None:
        super().__init__()


class Twisted(Champion):
    def __init__(self) -> None:
        super().__init__()


class Twitch(Champion):
    def __init__(self) -> None:
        super().__init__()


class Udyr(Champion):
    def __init__(self) -> None:
        super().__init__()


class Urgot(Champion):
    def __init__(self) -> None:
        super().__init__()


class Varus(Champion):
    def __init__(self) -> None:
        super().__init__()


class Vayne(Champion):
    def __init__(self) -> None:
        super().__init__()


class Veigar(Champion):
    def __init__(self) -> None:
        super().__init__()


class Velkoz(Champion):
    def __init__(self) -> None:
        super().__init__()


class Vex(Champion):
    def __init__(self) -> None:
        super().__init__()


class Vi(Champion):
    def __init__(self) -> None:
        super().__init__()


class Viego(Champion):
    def __init__(self) -> None:
        super().__init__()


class Viktor(Champion):
    def __init__(self) -> None:
        super().__init__()


class Vladimir(Champion):
    def __init__(self) -> None:
        super().__init__()


class Volibear(Champion):
    def __init__(self) -> None:
        super().__init__()


class Warwick(Champion):
    def __init__(self) -> None:
        super().__init__()


class Wukong(Champion):
    def __init__(self) -> None:
        super().__init__()


class Xayah(Champion):
    def __init__(self) -> None:
        super().__init__()


class Xerath(Champion):
    def __init__(self) -> None:
        super().__init__()


class XinZhao(Champion):
    def __init__(self) -> None:
        super().__init__()


class Hurensohn(Champion):
    def __init__(self) -> None:
        super().__init__()


class Yone(Champion):
    def __init__(self) -> None:
        super().__init__()


class Yorick(Champion):
    def __init__(self) -> None:
        super().__init__()


class Yuumi(Champion):
    def __init__(self) -> None:
        super().__init__()


class Zac(Champion):
    def __init__(self) -> None:
        super().__init__()


class Zed(Champion):
    def __init__(self) -> None:
        super().__init__()


class Zeri(Champion):
    def __init__(self) -> None:
        super().__init__()


class Ziggs(Champion):
    def __init__(self) -> None:
        super().__init__()


class Zilean(Champion):
    def __init__(self) -> None:
        super().__init__()


class Zoe(Champion):
    def __init__(self) -> None:
        super().__init__()


class Zyra(Champion):
    def __init__(self) -> None:
        super().__init__()


if __name__ == "__main__":
    ahri = Ahri()
