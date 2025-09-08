import bpy
import bmesh

from bmesh.types import BMesh
from bpy.types import Mesh as mesh, Object

from . import context


class Mesh:

  _mesh: mesh
  _bmesh: BMesh

  def __init__(this, name: str, vertices, faces):

    this._mesh: mesh = bpy.data.meshes.new(name)
    this._bmesh: Bmesh = None

    if vertices and faces:
      this.mesh_from_pydata(vertices, faces)
  

  def mesh_from_pydata(this, vertices, faces):
    this._mesh.from_pydata(vertices, [], faces)
    return this._mesh


  def to_bmesh(this):
    this._bmesh = Bmesh()
    return this._bmesh.from_mesh(this._mesh)
  

  def commit_bmesh(this):

    this._bmesh.bmesh.to_mesh(this._mesh)

    this._mesh.update()

    this._bmesh.bmesh.free()

    return this._mesh


class Bmesh:

  def __init__(this):
    this.bmesh: BMesh = bmesh.new()
    pass

  
  def from_mesh(this, mesh: mesh):
    this.bmesh.from_mesh(mesh)
    this.bmesh.faces.ensure_lookup_table()
    this.bmesh.verts.ensure_lookup_table()
    return this.bmesh
  

  def commit(this):
    this.bmesh.to_mesh()


  def delete_selected_vertices(this):

    selected = [v for v in this.bmesh.verts if v.select]
    bmesh.ops.delete(this.bmesh, geom=selected)


  
#region METHODS

def join(meshes: list[Mesh], rename: str) -> mesh:

  context.deselect_all()

  if len(meshes) == 1:
    return meshes[0]
  

  result = meshes[0]._mesh

  if rename:
    result.name = rename
  
  context.set_active(result)

  for mesh in meshes:
    object: Object = mesh._mesh
    object.select_set(state=True)

  context.join()
  context.deselect_all()

  return result

