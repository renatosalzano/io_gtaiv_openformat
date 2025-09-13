
from .ofio.oft import Oft
from .ofio.skel.bone import Bone
from .ofio.mesh.mesh import Mesh

from .utils import path, debug, log
from .blender import context
from bpy.types import Object
from . import store

oft: Oft = None
lod_mesh: list[Mesh] = []


def import_model(bone: Bone, parent: Object = None):

  x, y, z = bone.WorldOffset

  origin = (-x, -y, z)

  bone_obj = context.create_empty(bone.name, origin)

  for Mesh in lod_mesh:
    
    if Mesh.has_object(bone.name):

      mesh_obj = Mesh.get_object(bone.name)
      
      context.set_parent(bone_obj, mesh_obj)
      
      mesh_obj.hide_viewport = False if mesh_obj.name.startswith('L0') else True

  if bone.haschildrens():

    for child_bone in bone.children.values():

      import_model(child_bone, bone_obj)

  if parent:
    context.set_parent(parent, bone_obj)




def import_oft(filepath = ""):

  stopwatch = log.StopWatch()

  store.root_dir = path.dirname(filepath)
  store.filename = path.filename(filepath)
  store.is_vehicle = True

  src = f'{store.root_dir}/{store.filename}'

  if path.is_dir(src):
    context.clean_unused()

    # main_collection = context.get_collection(store.filename)

    # if main_collection:
    #   breakpoint()
    #   context.delete_hierarchy()

    store.main_collection = context.new_collection(
      name=store.filename,
      append_to_scene=True
    )

  else:
    raise ImportError(f'missing directory "{store.filename}" in {filepath}')

  debug.log(f'import model at "{filepath}"')

  oft = Oft(filepath)

  stopwatch.time(f'imported data')

  oft.import_materials()

  stopwatch.time(f'imported materials')

  lods = oft.drawable.lodgroup.get_lods()

  for lod, filepaths in lods.items():
    for filepath in filepaths:
      debug.log(f'import {lod}.mesh "{filepath}"')
      lod_mesh.append(Mesh(filepath))

  stopwatch.time(f'created mesh')

  context.select_collection(store.filename)

  for bone in oft.drawable.skel.bone.values():
    import_model(bone)

  stopwatch.stop()

  context.clean_unused()
  pass
