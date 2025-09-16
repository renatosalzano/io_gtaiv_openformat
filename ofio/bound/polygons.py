from ...utils.parser import ParserMethods
from ...utils import debug

class Polygons(ParserMethods):

  def __init__(this):
    this._is_array_block = True
    this._set_block = True
    this.polygons: list[Polygon] = []


  def set_block(this, key, value):
    debug.log(f'[Polygons] {key} {value}')
    this.polygons.append(Polygon())
    return this.polygons[-1]
  

  def get_polygon(this, index: int):
    return this.polygons[index]




class Polygon(ParserMethods):

  def __init__(this):
    this.Material =  0
    this.Vertices =  (0,0,0,0)
    this.Siblings =  (0,0,0,0)
