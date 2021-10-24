from zdspy.randomizer.common import BMG_Location, Location, ZMB_MPOB_Location

def location(loc: str):
    return f'data/{loc}'


# TODO: don't use raw strings here
locations: dict[str, Location] = {
    'first_ocean_temple_chest': ZMB_MPOB_Location(34, location('Map/dngn_main/map00.bin/zmb/dngn_main_00.zmb')),
    'first_mercay_npc': BMG_Location(135, location('English/Message/main_isl.bmg'))
}


def set_location(location: str, value: int):
    locations[location].set_location(value)
