import math
from dataclasses import dataclass
import random

# colors in german
_BLUE = "blue"
_WHITE = "white"
_YELLOW = "yellow"
_ORANGE = "orange"
_RED = "red"

_SUPERGIANT = "super giant"
_GIANT = "gient"
_DWARF = "dwarf"

sun_temp = 5778
sun_mag = 4.83


def _accusative_of(color: str) -> str:
    return color
    # In german we get use:
    # return color + "r" if color.endswith("e") else color + "er"


@dataclass
class Star:
    name: str
    temp: float
    mag: float

    @property
    def description(self):
        """
        Classify a star by its temperature (K) and absolute magnitude (Mv).
        Returns a string like "{_RED} supergiant", "{_YELLOW} dwarf", etc.
        """
        if self.temp >= 30000:
            color = f"{_BLUE}"
        # elif self.temp >= 10000:
        #     color = f"{_BLUE}-{_WHITE}"
        elif self.temp >= 7500:
            color = f"{_WHITE}"
        # elif self.temp >= 6000:
        #     color = f"{_YELLOW}-{_WHITE}"
        elif self.temp >= 5200:
            color = f"{_YELLOW}"
        elif self.temp >= 3700:
            color = f"{_ORANGE}"
        else:
            color = f"{_RED}"

        color = _accusative_of(color)

        # 2. Determine luminosity class
        if self.mag < -5:
            lum_class = _SUPERGIANT
        elif self.mag <= 1:
            lum_class = _GIANT
        else:
            lum_class = _DWARF

        return f"{color} {lum_class}"

    @property
    def diameter(self):
        """ Star diameter relative to the sun. """
        # Step 1: Luminosity ratio
        lum_ratio = 10 ** (0.4 * (sun_mag - self.mag))
        # Step 2: Temperature ratio
        temp_ratio = self.temp / sun_temp
        # Step 3: Radius ratio
        radius_ratio = math.sqrt(lum_ratio / (temp_ratio ** 4))
        return radius_ratio

    @property
    def color(self) -> tuple[float, float, float]:
        """
        Returns a color representation of the star based on its temperature.
        This is a simple approximation and can be used for visualization.
        """
        t = self.temp / 100.0
        # Red
        if t <= 66:
            r = 1.0
        else:
            r = t - 60
            r = 329.698727446 * (r ** -0.1332047592)
            r = max(0, min(r / 255, 1))
        # Green
        if t <= 66:
            g = 99.4708025861 * math.log(t) - 161.1195681661
            g = max(0, min(g / 255, 1))
        else:
            g = t - 60
            g = 288.1221695283 * (g ** -0.0755148492)
            g = max(0, min(g / 255, 1))
        # Blue
        if t >= 66:
            b = 1.0
        elif t <= 19:
            b = 0.0
        else:
            b = t - 10
            b = 138.5177312231 * math.log(b) - 305.0447927307
            b = max(0, min(b / 255, 1))
        return r, g, b


_STAR_LIST = [
    Star('Deneb', 8525, -8.38),
    Star('Rigel', 12100, -6.69),
    Star('Betelgeuse', 3500, -5.85),
    Star('Canopus', 7350, -5.71),
    Star('Antares', 3400, -5.28),
    Star('Beta Centauri', 25400, -4.53),
    Star('Polaris', 6015, -3.64),
    Star('Spica', 25400, -3.55),
    Star('Bellatrix', 22000, -2.78),
    Star('Achernar', 15000, -1.46),
    Star('Arcturus', 4286, -0.30),
    Star('Aldebaran', 3910, -0.63),
    Star('Wega', 9602, 0.58),
    Star('Pollux', 4865, 1.09),
    Star('Sirius', 9940, 1.42),
    Star('Atair', 7550, 2.21),
    Star('Procyon', 6530, 2.66),
    Star('Sonne', sun_temp, sun_mag),
    Star('Alpha Centauri A', 5790, 4.38),
    Star('Alpha Centauri B', 5260, 5.71),
    Star('Epsilon Eridani', 5084, 6.18),
    Star('61 Cygni A', 4450, 7.49),
    Star('61 Cygni B', 4040, 8.31),
    Star('Lacaille 9352', 3460, 10.68),
    Star('Gliese 725 A', 3400, 10.0),
    Star('Gliese 725 B', 3100, 11.0),
    Star('Sirius B', 25200, 11.18),
    Star('Bernard\'s Star', 3134, 13.21),
    Star('Procyon B', 7740, 13.0),
    Star('Proxima Centauri', 3042, 15.53),
]


def get_star_list():
    """
    Returns a list of Star objects in random order.
    This should ensure that slow students not finishing the list will still have a chance to a see a typical HRD.
    White Dwarfs are included in to the top 10 items.
    """
    stars_copy = _STAR_LIST.copy()
    random.shuffle(stars_copy)
    sirius_b = next(star for star in stars_copy if star.name == 'Sirius B')
    procyon_b = next(star for star in stars_copy if star.name == 'Procyon B')
    stars_copy.remove(sirius_b)
    stars_copy.remove(procyon_b)
    stars_copy.insert(random.randint(0, 9), sirius_b)
    stars_copy.insert(random.randint(0, 9), procyon_b)

    return stars_copy
