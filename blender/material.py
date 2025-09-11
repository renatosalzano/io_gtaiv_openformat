import bpy
from bpy import types
from bpy.types import Material as material, Node as node, ShaderNode as shadernode
from mathutils import Vector

from .shader_node.shaders import ShaderNode, MaterialOutput
from typing import TypeVar

T = TypeVar('T', bound=ShaderNode)

class Material:

  def __init__(this, name: str):

    materials = bpy.data.materials

    if name in materials:
      this._material = materials[name]
    else:
      this._material = materials.new(name)
      this._material.use_nodes = True
      this.remove_node('Principled BSDF')

    this._output: MaterialOutput = None


  def get_nodes(this):
    return this._material.node_tree.nodes
  

  def get_node(this, name):
    nodes = this.get_nodes()
    return nodes.get(name)
  

  def get_links(this):
    return this._material.node_tree.links
  

  def add_node(this, node: T) -> T:
    _nodes = this.get_nodes()
    _node: shadernode = _nodes.new(node.type)

    node.material = this
    node.node = _node

    return node
  

  def remove_node(this, node_name: str):
    nodes = this.get_nodes()
    node_to_remove = this.get_node(node_name)

    if node_to_remove:
      nodes.remove(node_to_remove)


  def get_output(this) -> MaterialOutput:
    if not this._output:
      this._output = MaterialOutput()
      this._output.node = this.get_node('Material Output')

    return this._output
  

  def link(this, from_node: tuple[shadernode, str], to: tuple[shadernode, str, int]):

    output_node, output_key = from_node
    input_node, input_key, offset_index = to

    links = this.get_links()
    
    output = output_node.outputs.get(output_key)
    input = input_node.inputs.get(input_key)

    # breakpoint()

    offset_x = output_node.width / 2 + input_node.width / 2 + 200.0

    output_node.location = input_node.location - Vector((offset_x, offset_index * 300.0))

    links.new(output, input)




