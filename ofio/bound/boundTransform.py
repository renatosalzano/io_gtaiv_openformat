from ...utils.parser import ParserMethods
from ..matrix import Matrix

class BoundTransform(ParserMethods):

  def __init__(this):
    this.matrix = []

  def set(this, k, v, item):
    x, y, z = item

    this.matrix.append((
      float(x),
      float(y),
      float(z)
    ))
  