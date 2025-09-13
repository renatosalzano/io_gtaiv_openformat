
from ...ofio.types import RGBAf, vec3, vec2
from .ShaderNode import ShaderNode
                    
class ShaderInvert(ShaderNode):

  def __init__(
    this,
    name: str = None,
    Fac: float = None,
    Color: RGBAf = None,

  ):
    super().__init__()
    this.name = name
    this.type = 'ShaderNodeInvert'

    if Fac:
      this.inputs.append(('Fac', Fac))

    if Color:
      this.inputs.append(('Color', Color))


  @property
  def Fac(this):
    return (this.node, 'Fac', 0)


  @property
  def Color(this):
    return (this.node, 'Color', 1)


  def _Color(this, link):
    this.material.link((this.node, 'Color'), link)

