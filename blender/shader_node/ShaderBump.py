
from ...ofio.types import RGBAf, vec3, vec2
from .ShaderNode import ShaderNode
                    
class ShaderBump(ShaderNode):

  def __init__(
    this,
    name: str = None,
    Strength: float = None,
    Distance: float = None,
    FilterWidth: float = None,

  ):
    this.name = name
    this.type = 'ShaderNodeBump'

    if Strength:
      this.inputs.append('Strength', Strength)

    if Distance:
      this.inputs.append('Distance', Distance)

    if FilterWidth:
      this.inputs.append('Filter Width', FilterWidth)


  @property
  def Strength(this):
    return (this.node, 'Strength', 0)


  @property
  def Distance(this):
    return (this.node, 'Distance', 1)


  @property
  def FilterWidth(this):
    return (this.node, 'Filter Width', 2)


  @property
  def Height(this):
    return (this.node, 'Height', 3)


  @property
  def InNormal(this):
    return (this.node, 'Normal', 4)


  def OutNormal(this, link):
    this.material.link((this.node, 'Normal'), link)

