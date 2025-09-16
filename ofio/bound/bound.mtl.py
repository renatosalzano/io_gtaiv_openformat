from ..types import vec3int

class BoundMtl:
  
  def __init__(
    this,
    bound_name: str,       
    bound_color: tuple[int, int, int],
    ):
    this.bound_name = bound_name
    this.bound_color = bound_color
                    
colors = (
	vec3int(125, 125, 125), # 0
	vec3int(255, 0, 0), # 1
	vec3int(110, 110, 110), # 2
	vec3int(150, 150, 150), # 3
	vec3int(150, 150, 150), # 4
	vec3int(150, 150, 150), # 5
	vec3int(230, 230, 230), # 6
	vec3int(230, 230, 230), # 7
	vec3int(175, 125, 50), # 8
	vec3int(170, 130, 0), # 9
	vec3int(160, 150, 120), # 10
	vec3int(255, 220, 170), # 11
	vec3int(160, 100, 0), # 12
	vec3int(0, 130, 0), # 13
	vec3int(150, 110, 80), # 14
	vec3int(0, 180, 0), # 15
	vec3int(255, 255, 0), # 16
	vec3int(200, 230, 0), # 17
	vec3int(130, 90, 0), # 18
	vec3int(200, 160, 80), # 19
	vec3int(160, 130, 50), # 20
	vec3int(200, 200, 200), # 21
	vec3int(190, 250, 250), # 22
	vec3int(200, 200, 200), # 23
	vec3int(100, 100, 100), # 24
	vec3int(190, 250, 250), # 25
	vec3int(100, 100, 100), # 26
	vec3int(170, 130, 0), # 27
	vec3int(170, 130, 0), # 28
	vec3int(90, 70, 30), # 29
	vec3int(255, 255, 255), # 30
	vec3int(130, 80, 0), # 31
	vec3int(170, 130, 0), # 32
	vec3int(255, 255, 255), # 33
	vec3int(0, 190, 255), # 34
	vec3int(255, 220, 190), # 35
	vec3int(255, 220, 190), # 36
	vec3int(255, 220, 190), # 37
	vec3int(255, 220, 190), # 38
	vec3int(90, 90, 90), # 39
	vec3int(90, 90, 90), # 40
)

# 0
default = BoundMtl("default", colors[0])
# 1
nofriction = BoundMtl("nofriction", colors[1])
# 2
car_void = BoundMtl("car_void", colors[1])
# 3
concrete = BoundMtl("concrete", colors[2])
# 4
concrete_freeway = BoundMtl("concrete_freeway", colors[2])
# 5
painted_road = BoundMtl("painted_road", colors[2])
# 6
plaster_board = BoundMtl("plaster_board", colors[2])
# 7
rumble_strip = BoundMtl("rumble_strip", colors[2])
# 8
tarmac = BoundMtl("tarmac", colors[2])
# 9
breeze_block = BoundMtl("breeze_block", colors[3])
# 10
mossy_rock = BoundMtl("mossy_rock", colors[3])
# 11
rock = BoundMtl("rock", colors[3])
# 12
stone = BoundMtl("stone", colors[3])
# 13
brick_cobble = BoundMtl("brick_cobble", colors[4])
# 14
brick_wall = BoundMtl("brick_wall", colors[4])
# 15
marble = BoundMtl("marble", colors[5])
# 16
paving_slabs = BoundMtl("paving_slabs", colors[6])
# 17
ceramics = BoundMtl("ceramics", colors[7])
# 18
rooftile = BoundMtl("rooftile", colors[7])
# 19
rail_sleeper = BoundMtl("rail_sleeper", colors[8])
# 20
wood_board = BoundMtl("wood_board", colors[8])
# 21
wood_counter = BoundMtl("wood_counter", colors[8])
# 22
wood_fence = BoundMtl("wood_fence", colors[8])
# 23
wood_handrail = BoundMtl("wood_handrail", colors[8])
# 24
wood_section = BoundMtl("wood_section", colors[8])
# 25
wood_wall_old = BoundMtl("wood_wall_old", colors[8])
# 26
wooden_garage_door = BoundMtl("wooden_garage_door", colors[8])
# 27
laminate = BoundMtl("laminate", colors[9])
# 28
polished_court = BoundMtl("polished_court", colors[9])
# 29
gravel = BoundMtl("gravel", colors[10])
# 30
pothole = BoundMtl("pothole", colors[2])
# 31
railway_gravel = BoundMtl("railway_gravel", colors[10])
# 32
sand = BoundMtl("sand", colors[11])
# 33
clay_court = BoundMtl("clay_court", colors[2])
# 34
dirt_dry = BoundMtl("dirt_dry", colors[12])
# 35
twigs = BoundMtl("twigs", colors[13])
# 36
mud_soft = BoundMtl("mud_soft", colors[14])
# 37
grass = BoundMtl("grass", colors[15])
# 38
short_grass = BoundMtl("short_grass", colors[15])
# 39
bushes = BoundMtl("bushes", colors[13])
# 40
flowers = BoundMtl("flowers", colors[16])
# 41
leaves_pile = BoundMtl("leaves_pile", colors[17])
# 42
bark_chipping = BoundMtl("bark_chipping", colors[18])
# 43
tree_bark_dark = BoundMtl("tree_bark_dark", colors[18])
# 44
tree_bark_light = BoundMtl("tree_bark_light", colors[19])
# 45
tree_bark_med = BoundMtl("tree_bark_med", colors[20])
# 46
aircon_duct = BoundMtl("aircon_duct", colors[21])
# 47
aircon_vent = BoundMtl("aircon_vent", colors[21])
# 48
billboard_frame = BoundMtl("billboard_frame", colors[21])
# 49
corrugated_iron = BoundMtl("corrugated_iron", colors[21])
# 50
electricity_box = BoundMtl("electricity_box", colors[21])
# 51
hollow_metal_panel = BoundMtl("hollow_metal_panel", colors[21])
# 52
hollow_metal_rail = BoundMtl("hollow_metal_rail", colors[21])
# 53
hollow_rust_metal = BoundMtl("hollow_rust_metal", colors[21])
# 54
lead_roofing = BoundMtl("lead_roofing", colors[21])
# 55
metal_awning = BoundMtl("metal_awning", colors[21])
# 56
metal_cellar = BoundMtl("metal_cellar", colors[21])
# 57
metal_drainage = BoundMtl("metal_drainage", colors[21])
# 58
metal_garage_door = BoundMtl("metal_garage_door", colors[21])
# 59
metal_grill = BoundMtl("metal_grill", colors[21])
# 60
metal_helipad = BoundMtl("metal_helipad", colors[21])
# 61
metal_lattice = BoundMtl("metal_lattice", colors[21])
# 62
metal_manhole = BoundMtl("metal_manhole", colors[21])
# 63
metal_railing = BoundMtl("metal_railing", colors[21])
# 64
metal_roller_door = BoundMtl("metal_roller_door", colors[21])
# 65
metal_tread_plate = BoundMtl("metal_tread_plate", colors[21])
# 66
metal_vent_subway = BoundMtl("metal_vent_subway", colors[21])
# 67
rail_crossing = BoundMtl("rail_crossing", colors[21])
# 68
rail_track = BoundMtl("rail_track", colors[21])
# 69
roller_door = BoundMtl("roller_door", colors[21])
# 70
solid_metal_panel = BoundMtl("solid_metal_panel", colors[21])
# 71
solid_rust_metal = BoundMtl("solid_rust_metal", colors[21])
# 72
treadplate_on_wood = BoundMtl("treadplate_on_wood", colors[21])
# 73
glass_brick = BoundMtl("glass_brick", colors[22])
# 74
glass_medium = BoundMtl("glass_medium", colors[22])
# 75
glass_strong = BoundMtl("glass_strong", colors[22])
# 76
glass_weak = BoundMtl("glass_weak", colors[22])
# 77
perspex = BoundMtl("perspex", colors[22])
# 78
skylights = BoundMtl("skylights", colors[22])
# 79
car_metal = BoundMtl("car_metal", colors[23])
# 80
car_plastic = BoundMtl("car_plastic", colors[24])
# 81
windscreen = BoundMtl("windscreen", colors[25])
# 82
corrugated_plastic = BoundMtl("corrugated_plastic", colors[26])
# 83
fibreglass = BoundMtl("fibreglass", colors[26])
# 84
plastic = BoundMtl("plastic", colors[26])
# 85
tarpaulin = BoundMtl("tarpaulin", colors[26])
# 86
linoleum = BoundMtl("linoleum", colors[27])
# 87
carpet = BoundMtl("carpet", colors[28])
# 88
fabric_cloth = BoundMtl("fabric_cloth", colors[28])
# 89
roofing_felt = BoundMtl("roofing_felt", colors[28])
# 90
rug = BoundMtl("rug", colors[28])
# 91
rubber = BoundMtl("rubber", colors[29])
# 92
paper = BoundMtl("paper", colors[30])
# 93
cardboard = BoundMtl("cardboard", colors[31])
# 94
mattress_foam = BoundMtl("mattress_foam", colors[32])
# 95
pillow_feathers = BoundMtl("pillow_feathers", colors[33])
# 96
pothole_puddle = BoundMtl("pothole_puddle", colors[34])
# 97
puddles = BoundMtl("puddles", colors[34])
# 98
water = BoundMtl("water", colors[34])
# 99
ped = BoundMtl("ped", colors[35])
# 100
buttocks = BoundMtl("buttocks", colors[35])
# 101
thigh_left = BoundMtl("thigh_left", colors[36])
# 102
shin_left = BoundMtl("shin_left", colors[36])
# 103
foot_left = BoundMtl("foot_left", colors[37])
# 104
thigh_right = BoundMtl("thigh_right", colors[36])
# 105
shin_right = BoundMtl("shin_right", colors[36])
# 106
foot_right = BoundMtl("foot_right", colors[37])
# 107
spine0 = BoundMtl("spine0", colors[35])
# 108
spine1 = BoundMtl("spine1", colors[35])
# 109
spine2 = BoundMtl("spine2", colors[35])
# 110
spine3 = BoundMtl("spine3", colors[35])
# 111
neck = BoundMtl("neck", colors[38])
# 112
head = BoundMtl("head", colors[38])
# 113
clavicle_left = BoundMtl("clavicle_left", colors[35])
# 114
upper_arm_left = BoundMtl("upper_arm_left", colors[36])
# 115
lower_arm_left = BoundMtl("lower_arm_left", colors[36])
# 116
hand_left = BoundMtl("hand_left", colors[36])
# 117
clavicle_right = BoundMtl("clavicle_right", colors[35])
# 118
upper_arm_right = BoundMtl("upper_arm_right", colors[36])
# 119
lower_arm_right = BoundMtl("lower_arm_right", colors[36])
# 120
hand_right = BoundMtl("hand_right", colors[36])
# 121
lowfriction_wheel = BoundMtl("lowfriction_wheel", colors[1])
# 122
hollow_wood = BoundMtl("hollow_wood", colors[8])
# 123
hollow_plastic = BoundMtl("hollow_plastic", colors[26])
# 124
hollow_cardboard = BoundMtl("hollow_cardboard", colors[31])
# 125
hollow_fibreglass = BoundMtl("hollow_fibreglass", colors[26])
# 126
windscreen_weak = BoundMtl("windscreen_weak", colors[25])
# 127
windscreen_med_weak = BoundMtl("windscreen_med_weak", colors[25])
# 128
windscreen_med_strong = BoundMtl("windscreen_med_strong", colors[25])
# 129
windscreen_strong = BoundMtl("windscreen_strong", colors[25])
# 130
tvscreen = BoundMtl("tvscreen", colors[39])
# 131
videowall = BoundMtl("videowall", colors[40])
# 132
pooltable_surface = BoundMtl("pooltable_surface", colors[28])
# 133
pooltable_cushion = BoundMtl("pooltable_cushion", colors[8])
# 134
pooltable_ball = BoundMtl("pooltable_ball", colors[7])
# 135
windscreen_side_weak = BoundMtl("windscreen_side_weak", colors[25])
# 136
windscreen_side_med = BoundMtl("windscreen_side_med", colors[25])
# 137
windscreen_rear = BoundMtl("windscreen_rear", colors[25])
# 138
windscreen_front = BoundMtl("windscreen_front", colors[25])
# 139
fx_metal_gas_pipe_flame = BoundMtl("fx_metal_gas_pipe_flame", colors[21])
# 140
fx_metal_water_pipe = BoundMtl("fx_metal_water_pipe", colors[21])
# 141
fx_metal_steam_pipe = BoundMtl("fx_metal_steam_pipe", colors[21])
# 142
fx_metal_oil_glug = BoundMtl("fx_metal_oil_glug", colors[21])
# 143
fx_wood_water_glug = BoundMtl("fx_wood_water_glug", colors[8])
# 144
fx_ceramic_water_hi_pressure = BoundMtl("fx_ceramic_water_hi_pressure", colors[7])
# 145
fx_metal_electric_sparks = BoundMtl("fx_metal_electric_sparks", colors[21])
# 146
fx_spare_1 = BoundMtl("fx_spare_1", colors[21])
# 147
fx_spare_2 = BoundMtl("fx_spare_2", colors[21])
# 148
fx_spare_3 = BoundMtl("fx_spare_3", colors[21])
# 149
emissive_glass = BoundMtl("emissive_glass", colors[22])
# 150
emissive_plastic = BoundMtl("emissive_plastic", colors[26])
# 151
glass_strong_shoot_thru = BoundMtl("glass_strong_shoot_thru", colors[22])
# 152
grass_patchy = BoundMtl("grass_patchy", colors[15])
# 153
grass_long = BoundMtl("grass_long", colors[15])
# 154
carpet_fabric = BoundMtl("carpet_fabric", colors[28])
# 155
pooltable_pocket = BoundMtl("pooltable_pocket", colors[8])


bound_mtl = (
## 0 --- 9 ##
	default, # 0
	nofriction, # 1
	car_void, # 2
	concrete, # 3
	concrete_freeway, # 4
	painted_road, # 5
	plaster_board, # 6
	rumble_strip, # 7
	tarmac, # 8
	breeze_block, # 9
## 10 --- 19 ##
	mossy_rock, # 10
	rock, # 11
	stone, # 12
	brick_cobble, # 13
	brick_wall, # 14
	marble, # 15
	paving_slabs, # 16
	ceramics, # 17
	rooftile, # 18
	rail_sleeper, # 19
## 20 --- 29 ##
	wood_board, # 20
	wood_counter, # 21
	wood_fence, # 22
	wood_handrail, # 23
	wood_section, # 24
	wood_wall_old, # 25
	wooden_garage_door, # 26
	laminate, # 27
	polished_court, # 28
	gravel, # 29
## 30 --- 39 ##
	pothole, # 30
	railway_gravel, # 31
	sand, # 32
	clay_court, # 33
	dirt_dry, # 34
	twigs, # 35
	mud_soft, # 36
	grass, # 37
	short_grass, # 38
	bushes, # 39
## 40 --- 49 ##
	flowers, # 40
	leaves_pile, # 41
	bark_chipping, # 42
	tree_bark_dark, # 43
	tree_bark_light, # 44
	tree_bark_med, # 45
	aircon_duct, # 46
	aircon_vent, # 47
	billboard_frame, # 48
	corrugated_iron, # 49
## 50 --- 59 ##
	electricity_box, # 50
	hollow_metal_panel, # 51
	hollow_metal_rail, # 52
	hollow_rust_metal, # 53
	lead_roofing, # 54
	metal_awning, # 55
	metal_cellar, # 56
	metal_drainage, # 57
	metal_garage_door, # 58
	metal_grill, # 59
## 60 --- 69 ##
	metal_helipad, # 60
	metal_lattice, # 61
	metal_manhole, # 62
	metal_railing, # 63
	metal_roller_door, # 64
	metal_tread_plate, # 65
	metal_vent_subway, # 66
	rail_crossing, # 67
	rail_track, # 68
	roller_door, # 69
## 70 --- 79 ##
	solid_metal_panel, # 70
	solid_rust_metal, # 71
	treadplate_on_wood, # 72
	glass_brick, # 73
	glass_medium, # 74
	glass_strong, # 75
	glass_weak, # 76
	perspex, # 77
	skylights, # 78
	car_metal, # 79
## 80 --- 89 ##
	car_plastic, # 80
	windscreen, # 81
	corrugated_plastic, # 82
	fibreglass, # 83
	plastic, # 84
	tarpaulin, # 85
	linoleum, # 86
	carpet, # 87
	fabric_cloth, # 88
	roofing_felt, # 89
## 90 --- 99 ##
	rug, # 90
	rubber, # 91
	paper, # 92
	cardboard, # 93
	mattress_foam, # 94
	pillow_feathers, # 95
	pothole_puddle, # 96
	puddles, # 97
	water, # 98
	ped, # 99
## 100 --- 109 ##
	buttocks, # 100
	thigh_left, # 101
	shin_left, # 102
	foot_left, # 103
	thigh_right, # 104
	shin_right, # 105
	foot_right, # 106
	spine0, # 107
	spine1, # 108
	spine2, # 109
## 110 --- 119 ##
	spine3, # 110
	neck, # 111
	head, # 112
	clavicle_left, # 113
	upper_arm_left, # 114
	lower_arm_left, # 115
	hand_left, # 116
	clavicle_right, # 117
	upper_arm_right, # 118
	lower_arm_right, # 119
## 120 --- 129 ##
	hand_right, # 120
	lowfriction_wheel, # 121
	hollow_wood, # 122
	hollow_plastic, # 123
	hollow_cardboard, # 124
	hollow_fibreglass, # 125
	windscreen_weak, # 126
	windscreen_med_weak, # 127
	windscreen_med_strong, # 128
	windscreen_strong, # 129
## 130 --- 139 ##
	tvscreen, # 130
	videowall, # 131
	pooltable_surface, # 132
	pooltable_cushion, # 133
	pooltable_ball, # 134
	windscreen_side_weak, # 135
	windscreen_side_med, # 136
	windscreen_rear, # 137
	windscreen_front, # 138
	fx_metal_gas_pipe_flame, # 139
## 140 --- 149 ##
	fx_metal_water_pipe, # 140
	fx_metal_steam_pipe, # 141
	fx_metal_oil_glug, # 142
	fx_wood_water_glug, # 143
	fx_ceramic_water_hi_pressure, # 144
	fx_metal_electric_sparks, # 145
	fx_spare_1, # 146
	fx_spare_2, # 147
	fx_spare_3, # 148
	emissive_glass, # 149
## 150 --- 155 ##
	emissive_plastic, # 150
	glass_strong_shoot_thru, # 151
	grass_patchy, # 152
	grass_long, # 153
	carpet_fabric, # 154
	pooltable_pocket, # 155
)
