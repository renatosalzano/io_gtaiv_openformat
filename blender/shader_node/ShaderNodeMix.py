from ...ofio.types import RGBAf, vec3, vec2
from .ShaderNode import ShaderNode
from mathutils import Euler
from typing import Literal

BlendType = Literal[
  'MIX', 'SCREEN', 'DARKEN', 'MULTIPLY', 'LIGHTEN', 'DODGE', 'ADD', 'OVERLAY',
  'SOFT_LIGHT', 'LINEAR_LIGHT',
  'SATURATION', 'DIFFERENCE', 'EXCLUSION', 'DIVIDE',
  'COLOR', 'VALUE', 'HUE', 'SATURATION'
]

FactorType = Literal[
   'UNIFORM',
   'NON_UNIFORM'
]

class ShaderNodeMix(ShaderNode):
  def __init__(
    this,
    name: str = None,
    data_type: Literal['FLOAT', 'RGBA', 'VECTOR'] = None,
    blend_type: BlendType = "MIX",
    factor_type: FactorType = "UNIFORM",
    Factor: float | vec3 = None,
    A: float | vec3 | RGBAf | Euler = None,
    B: float | vec3 | RGBAf | Euler = None,
  ):
    super().__init__()
    this.name = name
    this.type = "ShaderNodeMix"

    this.settings = {}
    if Factor:
      this.inputs.append(('Factor', Factor))
    if A:
      this.inputs.append(('A', A))
    if B:
      this.inputs.append(('B', B))

    if data_type:
        this.settings['data_type'] = data_type

        match data_type:
          case 'RGBA':
            this.settings['blend_type'] = blend_type
          case 'VECTOR':
            this.settings['factor_type'] = factor_type

  @property
  def Factor(this):
    return (this.node, 'Factor', 0)

  @property
  def A(this):
    return (this.node, 'A', 1)
  
  @property
  def B(this):
    return (this.node, 'B', 2)

  def _Result(this, link):
    this.material.link((this.node, 'Result'), link)