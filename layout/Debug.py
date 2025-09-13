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
  
  
    
  



class DATA_OT_debug_material(bpy.types.Operator):

  bl_idname = "debug.material"
  bl_label = "Debug Mat"
  bl_description = "debug material"

  def execute(this, context):

    # write_shader_class("PrincipledBSDF", "Principled", "ShaderNodeBsdfPrincipled")
    # write_shader_class("MaterialOutput", "MaterialOutput", "ShaderNodeOutputMaterial")
    # write_shader_class("ImageTexture", "ImageTexture", "ShaderNodeTexImage")
    write_shader_class("ShaderInvert", "ShaderInvert", "ShaderNodeInvert")

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