import bpy
import bmesh

from bmesh.types import BMesh
from bpy.types import Mesh as mesh, Object
from ..blender.material import Material

from . import context
from .. import store


class Mesh:

  _mesh: mesh
  _bmesh: BMesh

  def __init__(this, name: str, vertices = None, faces = None):

    this._name = name
    this._mesh: mesh = bpy.data.meshes.new(name)
    this._bmesh: Bmesh = None
    this._object: Object = None

    if vertices and faces:
      this.mesh_from_pydata(vertices, faces)
  

  def mesh_from_pydata(this, vertices = [], faces = []):
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
  

  def copy(this):

    mesh = Mesh(this._name)
    mesh._mesh = this._mesh.copy()

    return mesh
  
  
  def to_object(this):

    if this._object:
      return this._object
    
    object = bpy.data.objects.new(this._name, this._mesh)

    if store.main_collection:
      store.main_collection.objects.link(object)
    else:
      bpy.context.collection.objects.link(object)

    this._object = object

    return this._object
  

  def append_material(this, material: Material):

    if not this._object:
      this.to_object()

    if isinstance(material, Material):
      this._object.data.materials.append(material.get_material())
    else:
      raise ValueError(f'[blender.mesh] must be Material')


  def remove(this):

    if store.main_collection:
      store.main_collection.objects.unlink(this._object)
    else:
      bpy.context.collection.objects.unlink(this._object)


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

def join(meshes: list[Object], rename: str = None) -> Object:

  context.deselect_all()

  if len(meshes) == 1:
    return meshes[0]
  

  result = meshes[0]

  if rename:
    result.name = rename
  
  context.set_active(result)

  for object in meshes:
    object.select_set(state=True)

  context.join()
  
  bpy.ops.object.shade_smooth()

  context.deselect_all()

  return result

