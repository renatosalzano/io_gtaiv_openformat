
from ...ofio.types import RGBAf, vec3, vec2
from .ShaderNode import ShaderNode
                    
class ShaderUVMap(ShaderNode):

  def __init__(
    this,
    name: str = None,
    UV: str = None
  ):
    this.name = name
    this.type = 'ShaderNodeUVMap'

    if UV:
      this.settings['uv_map'] = UV


  def UV(this, link):
    this.material.link((this.node, 'UV'), link)

