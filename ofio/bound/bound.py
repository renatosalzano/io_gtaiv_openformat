

from ...utils.parser import ParserMethods
from .shrunk import Shrunk
from .polygons import Polygons
from .curved_edges import CurvedEdges
from .vertices import Vertices

class ListVec3Int(ParserMethods):

  def __init__(this, name: str):
    this.name = name
    this.list: list[tuple[int, int, int]] = []

  def set(this, _key, _value, item):
    x, y, z = item
    this.list.append((
      float(x),
      float(y),
      float(z)
    ))

class Bound(ParserMethods):

  def __init__(this):
    this.Type = ""
    this.CentroidPresent = 0
    this.CGPresent = 0
    this.Radius = 0.0
    this.WorldRadius = 0.0
    this.AABBMax = (0.0, 0.0, 0.0)
    this.AABBMin = (0.0, 0.0, 0.0)
    this.Centroid = (0.0, 0.0, 0.0)
    this.CenterOfMass = (0.0, 0.0, 0.0)
    this.Margin = (0.0, 0.0, 0.0)
    this.VertexScale = (0.0, 0.0, 0.0)
    this.VertexOffset = (0.0, 0.0, 0.0)

    this.Shrunk = ListVec3Int('Shrunk')
    this.Vertices = ListVec3Int('Vertices')
    this.Materials = ListVec3Int('Materials')

    this.Polygons = Polygons()
    this.CurvedEdges = CurvedEdges()
    this.CapsuleRadius = 0.0
    this.CapsuleHeight = 0.0

