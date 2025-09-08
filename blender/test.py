import bpy


def create_material(name, use_nodes = True):
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
  
def get_node(material, node):
  nodes = material.node_tree.nodes
  return nodes.get(node)

def debug_shader():

  # material = create_material('test')
  # node = get_node(material, "Principled BSDF")



  # print(node.inputs[0])

  # node_types = bpy.types.NODE_MT_add_node.items()

  # for identifier, label in node_types:
  #   print(label, identifier)
  pass



def init():
  debug_shader()