
from ...ofio.types import RGBAf, vec3, vec2
from .ShaderNode import ShaderNode
                    
class ShaderUVMap(ShaderNode):

  def __init__(
    this,
    name: str = None,
    uv_map: str = None
  ):
    super().__init__()
    this.name = name
    this.type = 'ShaderNodeUVMap'

    if uv_map:
      this.settings['uv_map'] = uv_map


  def _UV(this, link):
    this.material.link((this.node, 'UV'), link)

