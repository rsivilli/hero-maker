import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

# import modules.scripts as scripts
from scripts.hm_lib.logger import logger


@dataclass
class CharacterAttributes:
    label: str
    choices: Union[list[str], dict[str, str]]
    info: Union[str, None] = None
    interactive: bool = True
    multiselect: bool = False
    allow_custom_value: bool = False
    value: Optional[str] = None
    format_string: str = "({}:{})"

    def dict(self, skip_keys: Optional[set[str]] = None) -> Dict[str, Any]:
        out: Dict[str, Any] = {}
        if skip_keys is None:
            return asdict(self)
        for key, val in asdict(self).items():
            if key not in skip_keys:
                out[key] = val
        return out


attribute_list = []
attribute_lookup = {}


def load_character_attributes(search_dir: Path) -> list[CharacterAttributes]:
    logger.info(f"Loading files from {search_dir.absolute()}")
    out: List[CharacterAttributes] = []
    attribute_json_files = search_dir.glob("*.json")

    global attribute_lookup
    global attribute_list
    attribute_list = []
    attribute_lookup: dict[str, CharacterAttributes] = {}
    for attribute_json_file in attribute_json_files:
        with open(attribute_json_file, "r") as f:
            tmp = CharacterAttributes(**json.load(f))
            out.append(tmp)
            attribute_lookup[tmp.label] = tmp

    attribute_list: list[CharacterAttributes] = out
    logger.info(f"Loaded {len(attribute_list)} attribute files")
    return out


stat_config: List[Dict[str, str]] = [
    dict(
        info="Is your character mighty as an ox, or do they struggle to carry their shopping back from the magic item store? The Strength stat determines how strong your character is (you probably didn’t need a high Intelligence to know that). It also determines how much you can carry. You’ll use it for breaking down doors or moving heavy obstacles.",
        label="Strength",
    ),
    dict(
        info="Can your character matrix roll out of the path of a crossbow bolt, or do they trip over their own feet? Dexterity determines how agile your character is and how good their reflexes are. You’ll use it for sidestepping traps and hiding from foes.",
        label="Dexterity",
    ),
    dict(
        info="Can your character shrug off an axe blow, or are they blown over by a light gust of wind? Constitution is a measure of your character’s endurance, their ability to take a hit and keep on pushing. You’ll use it for resisting the effects of a poison (or alcohol) or for trudging through a snowstorm.",
        label="Constitution",
    ),
    dict(
        info="Can your character speak seven different languages, or were they snoring at the back during school? The Intelligence stat determines how clever your character is, how much they know, and their ability to use logic and reasoning. You’ll use it for knowledge checks, recalling details about history or the natural world.",
        label="Intelligence",
    ),
    dict(
        info="Can your character perform Holmes-like analysis of a crime scene or social situation, or are they lost in their own little world? Wisdom is one of the trickier stats to grok in D&D. It’s not obvious from the name what this ability score represents. Basically, Wisdom is your character’s awareness and intuition, of other people and of the environment. You’ll use it for Perception and Insight checks, to spot traps or hidden foes and work out an NPC’s intentions.",
        label="Wisdom",
    ),
    dict(
        info="Is your character the belle of the ball, or are they unlikely to get an invite? Charisma determines how your character fares in a social situation, and how likely it is a random stranger will like them. You’ll use it for lying to, cajoling, intimidating, or persuading other people. This stat doesn’t come up much in combat for most classes, but in social situations when roleplay is taking place, Charisma comes to the fore.",
        label="Charisma",
    ),
]
