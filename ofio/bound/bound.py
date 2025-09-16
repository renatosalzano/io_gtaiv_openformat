

from ...utils.parser import ParserMethods
from .polygons import Polygons, Polygon
from .curved_edges import CurvedEdges
from ...blender import mesh
from ..types import vec3, vec3int

class ListVec3Int(ParserMethods):

  def __init__(this, name: str):
    this.name = name
    this.list: list[tuple[int, int, int]] = []

  def set(this, _key, _value, item):
    x, y, z = item
    this.list.append((
      int(x),
      int(y),
      int(z)
    ))


  def get_vert(this, index: int):
    x, y, z = this.list[index]
    return vec3int(x, y, z)

  
  def get(this):
    return this.list


class Bound(ParserMethods):

  def __init__(this, bound_name: str):
    this.Type = ""
    this.CentroidPresent = 0
    this.CGPresent = 0

    this.Radius = 0.0
    this.WorldRadius = 0.0
    this.AABBMax: vec3 = (0.0, 0.0, 0.0)
    this.AABBMin: vec3 = (0.0, 0.0, 0.0)
    this.Centroid: vec3 = (0.0, 0.0, 0.0)
    this.CenterOfMass: vec3 = (0.0, 0.0, 0.0)
    this.Margin: vec3 = (0.0, 0.0, 0.0)
    this.VertexScale: vec3 = (0.0, 0.0, 0.0)
    this.VertexOffset: vec3 = (0.0, 0.0, 0.0)

    this.Shrunk = ListVec3Int('Shrunk')
    this.Vertices = ListVec3Int('Vertices')
    this.Materials = ListVec3Int('Materials')

    this.Polygons = Polygons()
    this.CurvedEdges = CurvedEdges()
    this.CapsuleRadius = 0.0
    this.CapsuleHeight = 0.0

    this._name = bound_name
    this._idx = []
    this._vertices = []
    this._material_index = []
    this._polygon_parsed = [0]


  
  def build(this):
    match this.Type:

      case "BoundGeometry":
        this.parse_polygons(this.Polygons.get_polygon(0))
        this.parse_vertices()

        return mesh.Mesh(
          name=f'COL_{this._name}', 
          faces=this._idx, 
          vertices=this._vertices
        )
      
      case "BoundCurvedGeometry":
        vert = this.Vertices.get_vert(1)

        rad = float(vert.z * this.VertexScale.z)

        if rad < 0:
          rad *= -1

        sphere_mesh = mesh.Mesh(this._name)
        sphere_mesh.to_sphere(radius=rad)
        return sphere_mesh
      case _:
        return None

  
  def parse_polygons(this, polygon: Polygon):

    vertices = list(polygon.Vertices)

    # Polygon.Siblings = (3, 0, 2, -1) -> (3, 0, 2)
    if -1 in polygon.Siblings and vertices[-1] == 0:
      # faces have 3 vertices connected
      vertices.pop()

    this._idx.append(tuple(vertices))
    this._material_index.append(polygon.Material)

    for sibling_polygon in polygon.Siblings:

      if sibling_polygon == -1:
        continue

      if sibling_polygon not in this._polygon_parsed:

        this._polygon_parsed.append(sibling_polygon)
        this.parse_polygons(this.Polygons.get_polygon(sibling_polygon))

  
  def parse_vertices(this):

    scale = this.VertexScale
    offset = this.VertexOffset

    for index in range(len(this.Vertices.get())):

      vert = this.Vertices.get_vert(index)

      for i in range(3):
        vert[i] *= scale[i]
        vert[i] += offset[i]

      vert.x *= -1
      vert.y *= -1
    
      this._vertices.append(vert)


