import bpy
import bmesh
from .converter import vector_to_string

def new_collection(name, parent = None):
  # New Collection
  coll = bpy.data.collections.new(name)

  if parent:
    parent.children.link(coll)
  else:
    # Add collection to scene collection
    bpy.context.scene.collection.children.link(coll)

  return coll


def create_mesh(name, verts, idx):
  mesh_data = bpy.data.meshes.new(name)
  mesh_data.from_pydata(verts, [], idx)
  return mesh_data


def create_mesh_obj(name, mesh = None, collection = None):
  mesh = mesh if bool(mesh) else create_mesh(name, [], [])

  obj = bpy.data.objects.new(name, mesh)

  if collection:
    collection.objects.link(obj)
  else:
    bpy.context.collection.objects.link(obj)

  return obj


def create_empty(name, location, collection):
  # select main collection
  bpy.ops.object.select_all(action='DESELECT')
  bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children[collection.name]
  bpy.ops.object.empty_add(type='SINGLE_ARROW', location=location)
  empty = bpy.context.object
  empty.name = name
  empty.empty_display_size = 0.1

  return empty


def set_parent(parent, child):
  
  if not bool(child):
    return
  
  # deselect all
  bpy.ops.object.select_all(action='DESELECT')
  # set parent to active
  bpy.context.view_layer.objects.active = parent
  child.select_set(state=True)
  bpy.ops.object.parent_set(type='OBJECT')


def bmesh_from_mesh(mesh):
  bm = bmesh.new()
  bm.from_mesh(mesh)
  bm.faces.ensure_lookup_table()
  bm.verts.ensure_lookup_table()
  return bm


def bmesh_from_edit_mesh(mesh):
  bm = bmesh.from_edit_mesh(mesh)
  bm.faces.ensure_lookup_table()
  bm.verts.ensure_lookup_table()
  return bm


def bmesh_to_mesh(bm, mesh):
  bm.to_mesh(mesh)
  mesh.update()
  bm.free()
  return mesh


def bmesh_delete_selected_verts(bm):
  selected = [v for v in bm.verts if v.select]

  bmesh.ops.delete(bm, geom=selected)


def join_meshes(name, mesh_to_join):
  # deselect all
  bpy.ops.object.select_all(action='DESELECT')
  
  if len(mesh_to_join) < 2:
    return mesh_to_join[0]

  active_mesh = mesh_to_join[0]
  active_mesh.name = name
  # set the first to active
  bpy.context.view_layer.objects.active = active_mesh
  # select meshes
  for obj in mesh_to_join:
    obj.select_set(state=True)

  bpy.ops.object.join()

  bpy.ops.object.select_all(action='DESELECT')

  return active_mesh


def mode_set(mode: str):
  bpy.ops.object.mode_set(mode = mode.upper())


def shade_smooth():
  bpy.ops.object.select_all(action='SELECT')
  bpy.ops.object.shade_smooth()
  bpy.ops.object.select_all(action='DESELECT')


def clean_unused():
  bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=False)
  # for material in bpy.data.materials:
  #   if not material.users:
  #       bpy.data.materials.remove(material)
  # for mesh in bpy.data.meshes:
  #   if not mesh.users:
  #       bpy.data.meshes.remove(mesh)


def create_capsule(z: int):
  bm = bmesh.new()
  bmesh.ops.create_uvsphere(bm, u_segments=8, v_segments=9, diameter=2)
  delta_Z = z
  bm.verts.ensure_lookup_table()
  for vert in bm.verts:
    if vert.co[2] < 0:
      vert.co[2] -= delta_Z
    elif vert.co[2] > 0:
      vert.co[2] += delta_Z

  name = 'Capsule'
  mesh = bpy.data.meshes.new(name)
  bm.to_mesh(mesh)
  mesh.update()
  bm.free()

  object = bpy.data.objects.new(name, mesh)
  bpy.context.scene.collection.objects.link(object)
  bpy.context.scene

  scene: Scene = bpy.context.scene


def merge_by_distance(mesh_obj):

  bpy.context.view_layer.objects.active = mesh_obj
  
  merge_threshold = 0.001

  # Get into edit mode (vertices can only be accessed in edit mode)
  bpy.ops.object.mode_set(mode='EDIT')

  # Select all vertices
  bpy.ops.mesh.select_all(action='SELECT')

  # Merge vertices by distance
  bpy.ops.mesh.remove_doubles(threshold=merge_threshold)

  # Get back into object mode
  bpy.ops.object.mode_set(mode='OBJECT')


def split_by_uv_island(mesh_obj, not_split):
  
  if not_split:
    return [mesh_obj], {}

  bpy.context.view_layer.objects.active = mesh_obj

  mode_set('edit')

  me = mesh_obj.data
  bm = bmesh_from_edit_mesh(me)

  # # old seams
  # old_seams = [e for e in bm.edges if e.seam]

  # # unmark old seams
  # for e in old_seams:
  #     e.seam = False

  # mark seams from uv islands
  bpy.ops.mesh.select_all(action='SELECT')  # select all mesh elements
  bpy.ops.uv.select_all(action='SELECT')  # select all UVs
  bpy.ops.uv.seams_from_islands()  # mark seams from UV islands

  seams = []
  seam_verts = set()

  for edge in bm.edges:
    if edge.seam:
      seams.append(edge)
      seam_verts.update(edge.verts)

  seam_verts = list(seam_verts)

  verts_data = {}

  for vert in seam_verts:
    key = vector_to_string(vert.co)
    verts_data[key] = vector_to_string(vert.normal)

  # split on seams
  bmesh.ops.split_edges(bm, edges=seams)

  # re-instate old seams
  # for e in old_seams:
  #     e.seam = True

  bmesh.update_edit_mesh(me)

  bm.free()

  # separate mesh objects for each newly split section
  bpy.ops.mesh.separate(type='LOOSE')

  mode_set('object')

  ret = [mesh_obj]

  for obj in bpy.context.selected_objects:
    ret.append(obj)

  
  return (ret, verts_data)


def split_by_material(mesh_obj):
  
  bpy.ops.object.select_all(action='DESELECT')

  # set to active
  bpy.context.view_layer.objects.active = mesh_obj

  delete_loose(mesh_obj)

  bpy.ops.object.mode_set(mode='EDIT')
  # Seperate by material
  bpy.ops.mesh.separate(type='MATERIAL')
  # Object Mode
  bpy.ops.object.mode_set(mode='OBJECT')

  first_material = mesh_obj.data.materials[0]
  splitted_obj = [(first_material, mesh_obj)]

  for obj in bpy.context.selected_objects:

    material_name = obj.data.materials[0]
    splitted_obj.append((material_name, obj))
    pass

  # bpy.ops.object.select_all(action='DESELECT')

  return splitted_obj


def copy_mesh_obj(mesh_obj):
  # set to active
  bpy.context.view_layer.objects.active = mesh_obj

  copy = bpy.context.active_object.copy()
  # append to scene
  copy.data = copy.data.copy()
  bpy.context.collection.objects.link(copy)

  bpy.context.view_layer.objects.active = copy
  return copy

  
def delete_loose(mesh_obj):
  # set to active
  bpy.context.view_layer.objects.active = mesh_obj

  bpy.ops.object.mode_set(mode='EDIT')            
  bpy.ops.mesh.select_all(action='SELECT')
  bpy.ops.mesh.delete_loose(use_verts=True, use_edges=True, use_faces=False)
  bpy.ops.object.mode_set(mode = 'OBJECT')