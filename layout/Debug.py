import bpy
from ..blender.material import Material
from ..utils.debug import create_file
from ..blender.shader_node.shaders import PrincipledBSDF, ShaderNodeMix, ImageTexture

# array: type(bpy.types.NodeSocketColor.default_value)


def write_shader_class(FILENAME: str, NODE_NAME:str, NODE_TYPE: str):

  output_file = create_file(FILENAME + '.py')

  mat = bpy.data.materials
  material = None

  if 'test' in mat:
    material = mat['test']
  else:
    material = mat.new(name='test')
    material.use_nodes = True

  nodes = material.node_tree.nodes
  node = nodes.get(NODE_NAME)

  if node == None:
    node = nodes.new(type=NODE_TYPE)

  output_file.write(f'''
from ...ofio.types import RGBAf, vec3, vec2
from .ShaderNode import ShaderNode
                    
class {FILENAME}(ShaderNode):

  def __init__(
    this,
    name: str = None,
''')


  for key, value in node.inputs.items():
    # key = key.lower()
    
    # node_name = key.replace(' ', '')

    # breakpoint()

    # if value.type == 'SHADER':
    #   key = key.replace(' ', '')
    #   output_file.write(f'    {key}: {node_value_type} = None,\n')

    # nodes_file.write(f'class {node_name}:\n\tdef __init__(\n\t\tthis,\n')
    if value.hide_value:
      continue

    print(key)

    if hasattr(value, 'default_value'):
      default_value = getattr(value, 'default_value')
      
      node_value_type = str(default_value)

      if node_value_type.startswith('<bpy_float'):
        vector_len = node_value_type[11]
        if vector_len == '4':
          node_value_type = 'RGBAf'
        else:
          node_value_type = 'vec3'
      else:
        node_value_type = type(default_value).__name__

      key = key.replace(' ', '')
      output_file.write(f'    {key}: {node_value_type} = None,\n')


  output_file.write(f'''
  ):
    this.name = name
    this.type = '{NODE_TYPE}'
''')

  for key, value in node.inputs.items():

    if value.hide_value or value.type == 'SHADER':
      continue

    _key = key.replace(' ', '')

    output_file.write(f'''
    if {_key}:
      this.inputs.append(('{key}', {_key}))
''')
    
  output_file.write('\n')

  for index, key in enumerate(node.inputs.keys()):
    _key = key.replace(' ', '')
    output_file.write(f'''
  @property
  def {_key}(this):
    return (this.node, '{key}', {index})

''')

  for index, key in enumerate(node.outputs.keys()):
    _key = key.replace(' ', '')

    output_file.write(f'''
  def {_key}(this, link):
    this.material.link((this.node, '{key}'), link)

''')
  



  
def write_bound_mtl():

  iv_col_material_mtlgrp = [
  
  [
		"generic", "void", "concrete", "stone", "brick_cobble", "marble", "paving_slabs", "ceramics", "wood", "laminate", "gravel", "sand", "dirt_dry", "bushes", "mud_soft", "grass", "flowers", "leaves_pile", "tree_bark_dark",
		"tree_bark_light", "tree_bark_medium", "metal", "glass", "car_metal", "car_plastic", "windscreen", "plastic", "linoleum", "carpet_fabric", "rubber", "paper", "cardboard", "mattress_foam", "pillow_feathers", "water", 
		"ped_torso", "ped_limb", "ped_foot", "ped_head", "tvscreen", "videowall"

  ],

  [
    (125, 125, 125),
		(255, 0, 0),
		(110, 110, 110),
		(150, 150, 150),
		(150, 150, 150),
		
		(150, 150, 150),
		(230, 230, 230),
		(230, 230, 230),
		(175, 125, 50),
		(170, 130, 0),
		# 10
		(160, 150, 120),
		(255, 220, 170),
		(160, 100, 0),
		(0, 130, 0),
		(150, 110, 80), 
		
		(0, 180, 0),
		(255, 255, 0),
		(200, 230, 0),
		(130, 90, 0),
		(200, 160, 80),
		# 20
		(160, 130, 50),
		(200, 200, 200),
		(190, 250, 250),
		(200, 200, 200),
		(100, 100, 100), 
		
		(190, 250, 250),
		(100, 100, 100),
		(170, 130, 0),
		(170, 130, 0),
		(90, 70, 30),
		# 30
		(255, 255, 255),
		(130, 80, 0),
		(170, 130, 0),
		(255, 255, 255),
		(0, 190, 255), 
		
		(255, 220, 190),
		(255, 220, 190),
		(255, 220, 190),
		(255, 220, 190),
		(90, 90, 90),
    # 40
		(90, 90, 90)
  ],
	[
		["default"], 
		["nofriction", "car_void", "lowfriction_wheel"], 
		["concrete", "concrete_freeway", "painted_road", "plaster_board", "rumble_strip", "tarmac", "pothole", "clay_court"], 
		["breeze_block", "mossy_rock", "rock", "stone"], 
		["brick_cobble", "brick_wall"], 
    
		["marble"], 
		["paving_slabs"], 
		["ceramics", "rooftile", "pooltable_ball", "fx_ceramic_water_hi_pressure"], 
		["rail_sleeper", "wood_board", "wood_counter", "wood_fence", "wood_handrail", "wood_section", "wood_wall_old", "wooden_garage_door", "hollow_wood", "pooltable_cushion", "fx_wood_water_glug", "pooltable_pocket"], 
		["laminate", "polished_court"], 
		# 10
		["gravel", "railway_gravel"], 
		["sand"], 
		["dirt_dry"], 
		["twigs", "bushes"], 
		["mud_soft"], 
		# 15
		["grass", "short_grass", "grass_patchy", "grass_long"], 
		["flowers"], 
		["leaves_pile"], 
		["bark_chipping", "tree_bark_dark"], 
		["tree_bark_light"], 
		["tree_bark_med"], 
		["aircon_duct", "aircon_vent", "billboard_frame", "corrugated_iron", "electricity_box", "hollow_metal_panel", "hollow_metal_rail", "hollow_rust_metal", "lead_roofing", "metal_awning", "metal_cellar", "metal_drainage", 
		"metal_garage_door", "metal_grill", "metal_helipad", "metal_lattice", "metal_manhole", "metal_railing", "metal_roller_door", "metal_tread_plate", "metal_vent_subway", "rail_crossing", "rail_track", "roller_door", 
		"solid_metal_panel", "solid_rust_metal", "treadplate_on_wood", "fx_metal_gas_pipe_flame", "fx_metal_water_pipe", "fx_metal_steam_pipe", "fx_metal_oil_glug", "fx_metal_electric_sparks", "fx_spare_1", "fx_spare_2", "fx_spare_3"], 
		["glass_brick", "glass_medium", "glass_strong", "glass_weak", "perspex", "skylights", "emissive_glass", "glass_strong_shoot_thru"], 
		["car_metal"], 
		["car_plastic"], 
		["windscreen", "windscreen_weak", "windscreen_med_weak", "windscreen_med_strong", "windscreen_strong", "windscreen_side_weak", "windscreen_side_med", "windscreen_rear", "windscreen_front"], 
		["corrugated_plastic", "fibreglass", "plastic", "tarpaulin", "hollow_plastic", "hollow_fibreglass", "emissive_plastic"], 
		["linoleum"], 
		["carpet", "fabric_cloth", "roofing_felt", "rug", "pooltable_surface", "carpet_fabric"], 
		["rubber"], 
		["paper"], 
		["cardboard", "hollow_cardboard"], 
		["mattress_foam"], 
		["pillow_feathers"], 
		["pothole_puddle", "puddles", "water"], 
		["ped", "buttocks", "spine0", "spine1", "spine2", "spine3", "clavicle_left", "clavicle_right"], 
		["thigh_left", "shin_left", "thigh_right", "shin_right", "upper_arm_left", "lower_arm_left", "hand_left", "upper_arm_right", "lower_arm_right", "hand_right"], 
		["foot_left", "foot_right"], 
		["neck", "head"], 
		["tvscreen"],
		["videowall"]
  ],
	
	[
		"none","ext_pavement_litter","ext_weeds_rocks","ext_wasteground_debris","ext_woodland_plants","ext_rubble_bricks_weeds", "ext_alleyway_litter","ext_junkyard_rubbish","ext_bushes_lush","ext_bushes_dry","ext_flowerbed_plants","ext_bushes_mixed",
		"ext_grass_dryplants_stones","ext_grass_dryplants_med","ext_grass_lushplants_short","ext_pavingslabs_debris", "ext_fastfood_litter","ext_litter_paper_leaf","ext_dirt_rubble_weeds","ext_woodplanks_breezeblocks","int_fastfood_litter",
		"ext_docks_rubble_wood_rope","ext_industrial_debris","ext_roadside_litter","ext_grass_dryplants_short","ext_meadow_plants", "ext_flowers_plants_sparse","ext_grass_dryplants_long","ext_grass_lushplants_long","int_skanky_litter","int_laundry_clothing",
		"int_laundry_socks","int_711_litter","ext_wasteground_weeds","ext_wasteground_bushy","ext_bushy_low","ext_bushy_med", "ext_weeds_tall","ext_weeds_dense","ext_weeds_tall_dense","proc_wtr_floating_scum","proc_urb_floating","proc_indus_floating",
  ],
  
	[
		[0],
		[1, 2, 121],
		[3, 4, 5, 6, 7, 8, 30, 33],
		[9, 10, 11, 12],
		[13, 14],
		[15],
		[16],
		[17, 18, 134, 144],
		[19, 20, 21, 22, 23, 24, 25, 26, 122, 133, 143, 155],
		[27, 28],
		[29, 31],
		[32],
		[34],
		[35, 39],
		[36],
		[37, 38, 152, 153],
		[40],
		[41],
		[42, 43],
		[44],
		[45],
		[46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 139, 140, 141, 142, 145, 146, 147, 148],
		[73, 74, 75, 76, 77, 78, 149, 151],
		[79],
		[80],
		[81, 126, 127, 128, 129, 135, 136, 137, 138],
		[82, 83, 84, 85, 123, 125, 150],
		[86],
		[87, 88, 89, 90, 132, 154],
		[91],
		[92],
		[93, 124],
		[94],
		[95],
		[96, 97, 98],
		[99, 100, 107, 108, 109, 110, 113, 117],
		[101, 102, 104, 105, 114, 115, 116, 118, 119, 120],
		[103, 106],
		[111, 112],
		[130], 
		[131]
  ]
  ]

  output_file = create_file('bound.mtl.py')

  output_file.write('''
class BoundMtl:
  
  def __init__(
    this,
    bound_name: str,       
    bound_color: tuple[int, int, int],
    ):
    this.bound_name = bound_name
    this.bound_color = bound_color
                    
''')
  

  categories, colors, names, flags, structure = iv_col_material_mtlgrp

  output_file.write('colors = (\n')

  i = 0
  for color in colors:
    output_file.write(f'\tvec3int{color}, # {i}\n')
    i += 1

  output_file.write(')\n\n')

  list_indexes: dict[str, int] = {}
  last_index = 0
  list_values: dict = {}

  for row_index, row in enumerate(structure):

    color = colors[row_index]
    category = categories[row_index]
    flag = flags[row_index]
    vars = names[row_index]

    if isinstance(row, int):
      row = [row]

    for i, index in enumerate(row):

      list_indexes[f'{index}'] = index
      list_values[f'{index}'] = {
        'color': color,
        'category': category,
        'flag': flag,
        'name': vars[i],
        'index': row_index
      }

      # for name in names[i]:
#       output_file.write(f'''
# # {index}
# {vars[i]} = "{vars[i]}"
# ''')



  indexes = list(list_indexes.values())
  indexes.sort()


  

  i = 0
  for key in indexes:

    key = f'{key}'
    value = list_values[key]
    name = value['name']
    color = value['color']
    category = value['category']
    flag = value['flag']
    index = value['index']
    output_file.write(f'# {key}\n')
    output_file.write(f'{name} = BoundMtl("{name}", colors[{index}])\n')

    # output_file.write(f'\tBoundMtl("{name}", colors[{index}]),\n')

    i += 1

  output_file.write('\n\nbound_mtl = (\n')

  i = 0

  for key in indexes:

    if i > 1:
      if (indexes[i - 1] +1) != key:
        print('error')

    Idx = i
    if Idx % 10 == 0:
      output_file.write(f'## {Idx} --- {Idx + 9} ##\n')

    key = f'{key}'
    value = list_values[key]
    # output_file.write(f'\t\n')
    name = value['name']
    color = value['color']
    category = value['category']
    flag = value['flag']
    index = value['index']

     

    output_file.write(f'\t{name}, # {key}\n')

    # output_file.write(f'\tBoundMtl("{name}", colors[{index}]),\n')

    i += 1

  output_file.write(')\n')



  # print(indexes)

  # print(list(list_indexes.values()).sort())

  
      # output_file.write(f'# {index}: {i}\n')



#   for row_index, row in enumerate(structure):
#     color = colors[row_index]
#     category = categories[row_index]
#     flag = flags[row_index]

#     print(row)

#     if isinstance(row, int):
#       row = [row]

#     for i, list_index in enumerate(row):
#       name_list = names[i]

#       array_index = 0

#       if isinstance(list_index, int):
#         array_index = list_index
#       else:
#         array_index = list_index[i]

#       print(array_index)

#       for name_index, name in enumerate(name_list):

#         output_file.write(f'''
# # {array_index}
# {name} = ("{name}", {color}, "{category}", "{flag}")
# ''')


  



class DATA_OT_debug_material(bpy.types.Operator):

  bl_idname = "debug.material"
  bl_label = "Debug Mat"
  bl_description = "debug material"

  def execute(this, context):

    # write_shader_class["PrincipledBSDF", "Principled", "ShaderNodeBsdfPrincipled")
    # write_shader_class["MaterialOutput", "MaterialOutput", "ShaderNodeOutputMaterial")
    # write_shader_class["ImageTexture", "ImageTexture", "ShaderNodeTexImage")
    # write_shader_class["ShaderInvert", "ShaderInvert", "ShaderNodeInvert")

    write_bound_mtl()

    # material = Material('dev')

    # Output = material.get_output()

    # Principled = material.add_node(PrincipledBSDF(
    #   label='Principled'
    # ))

    # MixNode = material.add_node(ShaderNodeMix(
    #   data_type='RGBA',
    #   blend_type='ADD'
    # ))

    # Texture1 = material.add_node(ImageTexture(
    #   name='Texture_1',
    #   label='Texture 1'
    # ))

    # Principled.BSDF(Output.Surface)

    # MixNode.Result(Principled.BaseColor)

    # Texture1.Color(MixNode.A)
    # Texture1.Alpha(MixNode.Factor)

    # breakpoint()
    


    return { 'FINISHED' }


class DATA_OT_fast_import(bpy.types.Operator):

  bl_idname = "debug.fastimport"
  bl_label = "Import Blista"
  bl_description = "import blista"

  def execute(this, context):
    from ..import_oft import import_oft
    from ..utils import path
    from .. import store

    filepath = 'D:/Modding/IV/io_gtaiv_openformats/example/blista.oft'

    store.filename = path.filename(filepath)
    store.root_dir = path.dirname(filepath)

    import_oft(filepath=filepath)

    return {'FINISHED'}


class VIEW3D_PT_debug_panel(bpy.types.Panel):

  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"

  bl_category = "Debug" #sidebar label
  bl_label = "Debug Panel" #head label

  def draw(this, ctx):

    row = this.layout.row()
    row.operator("debug.material", text="debug material")
    row.operator("debug.fastimport", text="import blista")
    

  
# material = Material.new('paint1')

# material.node(
#   PrincipledBSDF(
#     Base_Color=TextureNode(

#     ),
#     Roughness
#   )
# )