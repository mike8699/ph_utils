from zdspy.randomizer.common import BMG_Location, Location, ZMB_MPOB_Location

def location(loc: str):
    return f'data/{loc}'


# TODO: don't use raw strings here
locations: dict[str, Location] = {
    'ocean_temple_first_chest': ZMB_MPOB_Location(34, location('Map/dngn_main/map00.bin/zmb/dngn_main_00.zmb')),
    'mercay_island_first_npc': BMG_Location(135, location('English/Message/main_isl.bmg')),
    'mercay_island_chest_on_small_island': ZMB_MPOB_Location(54, location('Map/isle_main/map02.bin/zmb/isle_main_02.zmb')),
    'mercay_island_rollable_tree': ZMB_MPOB_Location(25, location('Map/isle_main/map02.bin/zmb/isle_main_02.zmb')),
    'mercay_island_SE_cliff_chest_left': ZMB_MPOB_Location(97, location('Map/isle_main/map03.bin/zmb/isle_main_03.zmb')),
    'mercay_island_SE_cliff_chest_right': ZMB_MPOB_Location(98, location('Map/isle_main/map03.bin/zmb/isle_main_03.zmb')),
    'mercay_island_SE_cucco_chest': ZMB_MPOB_Location(113, location('Map/isle_main/map03.bin/zmb/isle_main_03.zmb')),
    'mercay_island_shipyard_chest': ZMB_MPOB_Location(2, location('Map/isle_main/map16.bin/zmb/isle_main_16.zmb')),
    'mercay_island_oshus_sword_chest': ZMB_MPOB_Location(1, location('Map/isle_main/map19.bin/zmb/isle_main_19.zmb')),

    'isle_ember_chest_near_flame_temple': ZMB_MPOB_Location(74, location('Map/isle_flame/map00.bin/zmb/isle_main_00.zmb')),
    'isle_ember_chest_on_northern_small_island': ZMB_MPOB_Location(75, location('Map/isle_flame/map00.bin/zmb/isle_main_00.zmb')),
    'flame_temple_first_floor_key_chest': ZMB_MPOB_Location(26, location('Map/dngn_flame/map00.bin/zmb/dngn_flame.zmb')),
    'flame_temple_first_floor_red_rupee_chest': ZMB_MPOB_Location(68, location('Map/dngn_flame/map00.bin/zmb/dngn_flame_00.zmb')),
    'flame_temple_first_floor_red_rupee_chest': ZMB_MPOB_Location(68, location('Map/dngn_flame/map00.bin/zmb/dngn_flame_00.zmb')),
    'flame_temple_second_floor_boomerang_chest': ZMB_MPOB_Location(7, location('Map/dngn_flame/map01.bin/zmb/dngn_flame_01.zmb')),
    'flame_temple_third_floor_big_key_chest': ZMB_MPOB_Location(15, location('Map/dngn_flame/map02.bin/zmb/dngn_flame_02.zmb')),
    'flame_temple_boss_chest': ZMB_MPOB_Location(2, location('Map/boss_flame/map00.bin/zmb/boss_flame_00.zmb')),
}


def set_location(location: str, value: int):
    locations[location].set_location(value)
