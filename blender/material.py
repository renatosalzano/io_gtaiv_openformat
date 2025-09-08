import bpy
from bpy.types import Material as material, Node as node
from bpy import types

types.ShaderNodeBsdfPrincipled



class Material:

  def __init__(this, name: str):

    materials = bpy.data.materials

    if name in materials:
      this._material = materials[name]
    else:
      this._material = materials.new(name)

    this.principled: node = None


  def use_nodes(this):
    this._material.use_nodes = True
    this.principled = this.get_node("Principled BSDF")
    this.principled.inputs['']


  def get_nodes(this):
    return this._material.node_tree.nodes
  

  def get_node(this, name):
    nodes = this.get_nodes()
    return nodes.get(name)
  


