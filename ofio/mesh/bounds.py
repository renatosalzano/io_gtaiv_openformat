from ...utils.parser import ParserMethods
from ..types import vec4

class Bounds(ParserMethods):

  def __init__(this):
    this.bounds: list[vec4] = []

  
  def set(this, _k, _v, item):

    x, y, z, w = item

    this.bounds.append(
      vec4(
        float(x),
        float(y),
        float(z),
        float(w),
      )
    )
