
from .ShaderNode import ShaderNode

class MaterialOutput(ShaderNode):

  def __init__(
    this,
    name: str = None

  ):
    this.name = name
    this.type = 'ShaderNodeOutputMaterial'


  @property
  def Surface(this):
    return (this.node, 'Surface', 0)


  @property
  def Volume(this):
    return (this.node, 'Volume', 1)


  @property
  def Displacement(this):
    return (this.node, 'Displacement', 2)


  @property
  def Thickness(this):
    return (this.node, 'Thickness', 3)