from ...utils.parser import ParserMethods
from ...utils import debug


class CurvedEdges(ParserMethods):

  def __init__(this):
    this._is_array_block = True
    this._set_block = True
    this.edges: list[Edge] = []


  def set_block(this, key, value):
    debug.log(f'[CurvedEdges] {key} {value}')
    this.edges.append(Edge())
    return this.edges[-1]
  

  def get_polygon(this, index: int):
    return this.edges[index]



class Edge(ParserMethods):

  def __init__(this):
    this.unk_V = (0.0, 0.0, 0.0)
    this.unk_V2 = (0.0, 0.0, 0.0)
    this.unk_F = 0.0
    this.Vertices = (0, 0, 0)