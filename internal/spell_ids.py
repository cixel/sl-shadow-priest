racials = {
    "Human": 20598,
    "Blood_Elf": 28730,
    "Vulpera": 312411,
    "Maghar_Orc": 274738,
    "Undead": 5227,
    "Void_Elf": 255669,
    "Dark_Iron_Dwarf": 265221,
    "Troll": 26297,
    "Lightforged_Draenei": 255647,
    "Orc": 33697,
    "Kul_Tiran": 291628,
    "Goblin": 69042,
    "Draenei": 6562,
    "Panda": 107072,
    "Mechagnome": 312923,
    "Nightborne": 255665,
    "Night_Elf_Crit": 154748,
    "Night_Elf_Haste": 154748,
    "Dwarf": 59224,
    "Tauren": 154743,
    "Gnome": 92680,
    "Worgen": 68975,
    "Zandalari_Troll_Kimbul": 292363,
    "Zandalari_Troll_Paku": 292361,
    "Zandalari_Troll_Bwonsamdi": 292360
}

enchants = {
    "Weapon_Lightless_Force": 309620,
    "Weapon_Sinful_Revelation": 309623,
    "Weapon_Celestial_Guidance": 309627,
    "Wrists_Illuminated_Soul": 309608,
    "Wrists_Eternal_Intellect": 309609,
    "Chest_Eternal_Bounds": 323761,
    "Chest_Eternal_Stats": 324773,
    "Chest_Eternal_Insight": 342316,
    "Chest_Sacred_Stats": 323762,
    "Ring_Tenet_of_Critical_Strike": 309616,
    "Ring_Tenet_of_Versatility": 309619,
    "Ring_Tenet_of_Haste": 309617,
    "Ring_Tenet_of_Mastery": 309618,
    "Ring_Bargain_of_Critical_Strike": 309612,
    "Ring_Bargain_of_Versatility": 309615,
    "Ring_Bargain_of_Haste": 309613,
    "Ring_Bargain_of_Mastery": 309614
}

legendaries = {
    "Shadowflame_Prism": 336143,
    "Shadowflame_Prism_Conduit_15": 336143,
    "Twins_of_the_Sun_Priestess_Conduit_15": 336897,
    "Eternal_Call_to_the_Void": 336214,
    "Talbadars_Stratagem": 342415,
    "Judgment_of_the_Arbiter": 339344,
    "Sephuzs_Proclamation": 339348,
    "Painbreaker_Psalm": 336165
}

covenants = {
    "Necrolord": 324724,
    "Venthyr": 323673,
    "Night_Fae": 327661,
    "Kyrian": 325013
}

conduits = {
    "Haunting_Apparitions": 338319,
    "Dissonant_Echoes": 338342,
    "Mind_Devourer": 338332,
    "Rabid_Shadows": 338338,
    "Courageous_Ascension": 337966,
    "Fae_Fermata": 338305,
    "Festering_Transfusion": 337979,
    "Shattered_Perceptions": 338315
}


def find_ids(key):
    if key == 'racials':
        return racials
    elif key == 'enchants':
        return enchants
    elif key == 'covenants':
        return covenants
    elif key == 'legendaries':
        return legendaries
    elif key == 'conduits':
        return conduits
