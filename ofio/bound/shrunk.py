from ...utils.parser import ParserMethods

class Shrunk(ParserMethods):

  def __init__(this):
    this.shrunk: list[tuple[int, int,int]] = []

  def set(this, _key, _value, item):
    a, b, c = item
    this.shrunk.append((
      float(a),
      float(b),
      float(c)
    ))
