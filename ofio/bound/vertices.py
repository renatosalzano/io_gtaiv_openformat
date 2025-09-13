from ...utils.parser import ParserMethods

class Vertices(ParserMethods):

  def __init__(this):
    this.vertices: list[tuple[int, int,int]] = []

  def set(this, _key, _value, item):
    x, y, z = item
    this.vertices.append((
      float(x),
      float(y),
      float(z)
    ))