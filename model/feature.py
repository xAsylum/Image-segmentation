from enum import Enum
from typing import Tuple

class Feature(Enum): #    Id          [ R,   G    B ]
    ROAD =                 0,         (128,  64, 128)
    SIDEWALK =             1,         (244,  35, 232)
    BUILDING =             2,         ( 70,  70,  70)
    WALL =                 3,         (102, 102, 156)
    FENCE =                4,         (190, 153, 153)
    POLE =                 5,         (153, 153, 153)
    TRAFFIC_LIGHT =        6,         (250, 170,  30)
    TRAFFIC_SIGN =         7,         (220, 220,   0)
    VEGETATION =           8,         (107, 142,  35)
    TERRAIN =              9,         (152, 251, 152)
    SKY =                 10,         ( 70, 130, 180)
    PERSON =              11,         (220,  20,  60)
    RIDER =               12,         (255,   0,   0)
    CAR =                 13,         (  0,   0, 142)
    TRUCK =               14,         (  0,   0,  70)
    BUS =                 15,         (  0,  60, 100)
    TRAIN =               16,         (  0,  80, 100)
    MOROTCYCLE =          17,         (  0,   0, 230)
    BICYCLE =             18,         (119,  11,  32)

    def get_id(self):
        return self.value[0]

    def get_color(self):
        return self.value[1]

class FeatureCategory(Enum):
    FLAT =              ( 0,  1)
    CONSTRUCTION =      ( 2,  4)
    OBJECT =            ( 5,  7)
    NATURE =            ( 8,  9)
    SKY =               (10, 10)
    HUMAN =             (11, 12)
    VEHICLE =           (13, 18)

    def included(self, id: int):
        return self.value[0] <= id and id <= self.value[1]

_FEATURE_FROM_COLOR = {
    x.get_color(): x for _, x in Feature.__members__.items()
}

def feature_from_color(color: Tuple[int, int, int]) -> Feature | None:
    if color in _FEATURE_FROM_COLOR.keys():
        return _FEATURE_FROM_COLOR[color]
    return None