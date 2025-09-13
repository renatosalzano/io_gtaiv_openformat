
from .. import store
import bpy
from mathutils import Vector
from ..utils import file_exist

def material_exist(name):
  materials = bpy.data.materials
  if name in materials:
    return True
  return False


def create_material(name, use_nodes = False):
  materials = bpy.data.materials

  if name in materials:
    # material = materials[name]
    # material = remove_nodes(material)
    return materials[name]
  else:
    # create new material
    material = materials.new(name)
    material.use_nodes = use_nodes
    return material


def remove_nodes(material):
  nodes = material.node_tree.nodes
  for node in nodes:
    nodes.remove(node)
  return material


def debug_material(material):
  nodes = material.node_tree.nodes
  links = material.node_tree.links
  breakpoint()
  pass


def get_node(material, node):
  nodes = material.node_tree.nodes
  return nodes.get(node)


def get_input(node, input):
  i = node.inputs.get(input)
  return i


def add_node(material, node_type, settings = None):

  nodes = material.node_tree.nodes
  # links = material.node_tree.links

  node = nodes.new(type=node_type)

  if settings is not None:
    for key, value in settings.items():
      setattr(node, key, value)

  return node


def link_node(material, output, input, row = 0):
  # breakpoint()
  links = material.node_tree.links

  output_node, output_name = output
  input_node, input_name = input
  output = output_node.outputs.get(output_name)
  input = input_node.inputs.get(input_name)

  # breakpoint()

  offset_x = output_node.width / 2 + input_node.width / 2 + 200.0

  output_node.location = input_node.location - Vector((offset_x, row * 300.0))

  links.new(output, input)


def texture_path(basename):
  dir_paths = [
    f'{store.root_dir}/{store.basename}',
    f'{store.root_dir}/vehshare',
    f'{store.root_dir}/texture'
  ]
  
  extensions = ['.dds', '.png']
  path = ''
  filename = ''
  image_found = False
  for dir in dir_paths:

    if image_found:
      break

    for ext in extensions:
      test_path = f'{dir}/{basename}{ext}'
      if file_exist(test_path):
        path = test_path
        filename = f'{basename}{ext}'
        break

  return (path, filename)


def add_texture_node(material, basename, name):

  path, filename = texture_path(basename)

  nodes = material.node_tree.nodes
  links = material.node_tree.links

  texture_node = nodes.new(type="ShaderNodeTexImage")
  setattr(texture_node, 'name', name)

  if path == "":
    return texture_node

  if not filename in bpy.data.images:
    texture_node.image = bpy.data.images.load(path)
  else:
    texture_node.image = bpy.data.images.get(filename)
  
  return texture_node
  # links.new(image_texture_node.outputs[0], material_output_node.inputs[0])


def get_materials(materials_data):
  ret = []
  for material in bpy.data.materials:
    try:
      material_name = material.name.replace('[', '').replace(']','')
      if material_name in materials_data:
        ret.append(material.name)
      
    except:
      print(f'unknow shader {material.name}')
      pass
  
  return ret
