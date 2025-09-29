
from ...ofio.types import vec4, vec3, vec2
from .ShaderNode import ShaderNode


class ShaderDiffuseBSDF(ShaderNode):

  def __init__(
    this,
    name: str = None,
    Color: vec4 = None,
    Roughness: float = None,

  ):
    super().__init__()
    this.name = name
    this.type = 'ShaderNodeBsdfDiffuse'

    if Color:
      this.inputs.append(('Color', Color))

    if Roughness:
      this.inputs.append(('Roughness', Roughness))



  @property
  def Color(this):
    return (this.node, 'Color', 0)


  @property
  def Roughness(this):
    return (this.node, 'Roughness', 1)


  @property
  def Normal(this):
    return (this.node, 'Normal', 2)


  def _BSDF(this, link):
    this.material.link((this.node, 'BSDF'), link)

