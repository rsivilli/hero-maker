from numpy import Inf
from dataclasses import dataclass

@dataclass
class stat_description(object):
    desc:str 
    max_value:int = Inf
    min_value:int = -Inf
    




stat_config = {
    "strength":[
    stat_description(
        max_value = 1,
        desc="Morbidly weak, has significant trouble lifting own limbs"
    ),
    stat_description(
        min_value= 2,
        max_value = 3,
        desc="Needs help to stand, can be knocked over by strong breezes"
    )
    ,
    stat_description(
        min_value= 4,
        max_value = 5,
        desc="Knocked off balance by swinging something dense"
    )
    ,
    stat_description(
        min_value= 6,
        max_value = 7,
        desc="Difficulty pushing an object of their weight"
    ),
    stat_description(
        min_value= 8,
        max_value = 9,
        desc="Has trouble even lifting heavy objects"
    ),
    stat_description(
        min_value= 10,
        max_value = 11,
        desc="Can literally pull their own weight"
    ),
    stat_description(
        min_value= 12,
        max_value = 13,
        desc="Needs help to stand, can be knocked over by strong breezes"
    ),
    stat_description(
        min_value= 14,
        max_value = 15,
        desc="Needs help to stand, can be knocked over by strong breezes"
    ),
    stat_description(
        min_value= 16,
        max_value = 17,
        desc="Needs help to stand, can be knocked over by strong breezes"
    ),
    stat_description(
        min_value= 18,
        max_value = 19,
        desc="Needs help to stand, can be knocked over by strong breezes"
    )
    

]
}