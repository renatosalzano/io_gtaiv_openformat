from ..utils.parser import ParserMethods

class Lodgroup(ParserMethods):

  def __init__(this):
    this.high = ""
    this.med = ""
    this.low = ""
    this.vlow = ""
    this.center = (0.0, 0.0, 0.0)
    this.AABBMin = (0.0, 0.0, 0.0)
    this.AABBMax = (0.0, 0.0, 0.0)
    this.radius = 0.0


  # def set(this, key, value, item):

  #   match key:
  #     case 'high' | 'med' | 'low' | 'vlow':
  #       setattr(this, key, value)
  #     case _:
  #       super().set(key, value, item)