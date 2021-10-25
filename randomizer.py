from zdspy.randomizer.common import BMG_Location, Location, ZMB_MPOB_Location

def location(loc: str):
    return f'data/{loc}'


# TODO: don't use raw strings here
locations: dict[str, Location] = {
    'first_ocean_temple_chest': ZMB_MPOB_Location(34, location('Map/dngn_main/map00.bin/zmb/dngn_main_00.zmb')),
    'first_mercay_npc': BMG_Location(135, location('English/Message/main_isl.bmg')),
    'chest_on_small_island': ZMB_MPOB_Location(54, location('Map/isle_main/map02.bin/zmb/isle_main_02.zmb')),
    'mercay_island_rollable_tree': ZMB_MPOB_Location(25, location('Map/isle_main/map02.bin/zmb/isle_main_02.zmb')),
    'mercay_island_SE_cliff_chest_left': ZMB_MPOB_Location(97, location('Map/isle_main/map03.bin/zmb/isle_main_03.zmb')),
    'mercay_island_SE_cliff_chest_right': ZMB_MPOB_Location(98, location('Map/isle_main/map03.bin/zmb/isle_main_03.zmb')),
    'mercay_island_SE_cucco_chest': ZMB_MPOB_Location(113, location('Map/isle_main/map03.bin/zmb/isle_main_03.zmb')),
}


def set_location(location: str, value: int):
    locations[location].set_location(value)
