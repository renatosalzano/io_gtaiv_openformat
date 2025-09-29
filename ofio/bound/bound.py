

from ...utils.parser import ParserMethods
from .polygons import Polygons, Polygon
from .curved_edges import CurvedEdges
from ...blender import mesh, material
from ...blender.shader_node.shaders import ShaderDiffuseBSDF
from ..types import vec4, vec3, vec3int
from .bound_mtl import bound_mtl
from mathutils import Matrix
from ...utils import debug

from ..child_struct import ChildStruct

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
    this._bound_chunks: dict[str, BoundChunk] = {}
    this._idx = []
    this._vertices = []
    this._materials: list[material.Material] = []
    this._material_index = []
    this._polygon_parsed = [0]


  
  def build(this, child: ChildStruct):

    debug.log(f'[buond] build {this._name} - {this.Type}')

    match this.Type:

      case "BoundGeometry":
        this.parse_polygons(this.Polygons.get_polygon(0))
        this.parse_vertices()

        mesh_to_join: list[mesh.Mesh] = []

        for chunk in this._bound_chunks.values():

          tmp_mesh = mesh.Mesh(
            name=f'TMP_COL_{this._name}_MAT_{chunk.material_index}', 
            faces=chunk.idx,
            vertices=this._vertices
          )

          bound_material = chunk.build_material(this.Materials)

          tmp_mesh.append_material(bound_material)
          tmp_object = tmp_mesh.to_object()

          mesh_to_join.append(tmp_object)

        bound_object = mesh.join(mesh_to_join, f'_COL_{this._name}')

        x, y, z = this.VertexOffset.xyz

        bound_object.location = (x, y, z)

        debug.log(f'[bound] child_transform = {child._transform}')

        bound_object.location = child._transform @ bound_object.location

        # parent_matrix = Matrix()

        # if child._parent:
        #   parent_matrix = child._parent.f50.get_matrix().inverted()

        # transform_matrix = child.f50.get_matrix().inverted() * parent_matrix

        # print(this._name, child._transform)

        # world_offset = bound_object.matrix_world * child._transform

        # bound_object.location = world_offset @ bound_object.location

        this.set_properties(bound_object)

        return bound_object
      
      case "BoundCurvedGeometry":
        vert = this.Vertices.get_vert(1)

        rad = float(vert.z * this.VertexScale.z)

        if rad < 0:
          rad *= -1

        sphere_mesh = mesh.Mesh(f'_COL_{this._name}')
        sphere_mesh.to_sphere(radius=rad)

        bound_object = sphere_mesh.to_object()

        this.set_properties(bound_object)

        return bound_object
      case _:
        return None

  
  def parse_polygons(this, polygon: Polygon):

    vertices = list(polygon.Vertices)

    # Polygon.Siblings = (3, 0, 2, -1) -> (3, 0, 2)
    if -1 in polygon.Siblings and vertices[-1] == 0:
      # faces have 3 vertices connected
      vertices.pop()

    key = f'{polygon.Material}'

    if not key in this._bound_chunks:
      this._bound_chunks[key] = BoundChunk(polygon.Material)

    this._bound_chunks[key].idx.append(tuple(vertices))

    # this._idx.append(tuple(vertices))
    # this._material_index.append(polygon.Material)

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
        # vert[i] += offset[i]

      vert.x *= -1
      vert.y *= -1
    
      this._vertices.append(vert)


  def set_properties(this, object: mesh.Object):
    
    object['Type'] = this.Type
    object['CentroidPresent'] = this.CentroidPresent
    object['CGPresent'] = this.CGPresent
    object['Radius'] = this.Radius
    object['WorldRadius'] = this.WorldRadius
    object['AABBMax'] = this.AABBMax
    object['AABBMin'] = this.AABBMin
    object['Centroid'] = this.Centroid
    object['CenterOfMass'] = this.CenterOfMass
    object['Margin'] = this.Margin
    # object['VertexScale'] = this.VertexScale
    # object['VertexOffset'] = this.VertexOffset


class BoundChunk:

  def __init__(this, material_index: int):
    this.idx: list[int] = []
    this.material_index: int = material_index
    pass


  def build_material(this, bound_materials: ListVec3Int):

    bound_material_index = bound_materials.get()[this.material_index][0]

    mtl = bound_mtl[bound_material_index]
    r, g, b = mtl.bound_color

    mat = material.Material(mtl.bound_name)
    mat_output = mat.get_output()

    diffuse_color = mat.add_node(
      ShaderDiffuseBSDF(
        Color=(r, g, b, 1.0),
        Roughness=1.0
      )
    )

    diffuse_color._BSDF(mat_output.Surface)

    return mat