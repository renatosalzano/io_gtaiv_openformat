
from .ofio.oft import Oft
from .ofio.skel.bone import Bone
from .ofio.mesh.mesh import Mesh

from .utils import path, debug, log
from .blender import context
from bpy.types import Object
from . import store, config

oft: Oft = None
lod_mesh: list[Mesh] = []
tmp_object: dict[str, Object] = {}



def import_mesh(bone_name: str, parent_object: Object):

  for Mesh in lod_mesh:
    
    if Mesh.has_object(bone_name):

      mesh_obj = Mesh.get_object(bone_name)
      
      context.set_parent(parent_object, mesh_obj)
      
      hide = False if mesh_obj.name.startswith('L0') else True

      mesh_obj.hide_set(hide)


def import_child(bone_name: str, parent_object: Object):

  child = oft.get_child(bone_name)

  if child:
    is_wheel = bone_name.startswith('wheel')

    if is_wheel:
      index = bone_name.split('_')[1] # wheel_lf
      wheelname = f'wheelmesh_{index}'

    child_lod_mesh = child.build_mesh()

    for child_mesh in child_lod_mesh:

      for mesh_name, mesh_object in child_mesh.objects.items():

        if child_mesh.Lod > 0:
          wheelname = f'{wheelname}_l{child_mesh.Lod}'

        if is_wheel:
          tmp_object[wheelname] = mesh_object


    child_bound = child.build_bound()




def import_model(bone: Bone, parent: Object = None):

  x, y, z = bone.WorldOffset

  origin = (-x, -y, z)

  bone_obj = context.create_empty(bone.name, origin)

  if config.IMPORT_MESH:
    import_mesh(bone.name, bone_obj)

  import_child(bone.name, bone_obj)
  
  if bone.name in tmp_object:

    if bone.name.startswith('wheel'):
      tmp_object[bone.name].location = origin
      # context.shade_smooth(tmp_object[bone.name])


    context.set_parent(bone_obj, tmp_object[bone.name])

  if bone.haschildrens():

    for child_bone in bone.children.values():

      import_model(child_bone, bone_obj)

  if parent:
    context.set_parent(parent, bone_obj)


def build_mesh():

  for mesh in oft.drawable.lodgroup.build_mesh('vehicle'):
    lod_mesh.append(mesh)


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

  global oft
  oft = Oft(filepath)

  stopwatch.time(f'imported data')

  oft.import_materials()
  print(f'materials count: {len(store.materials)}')

  stopwatch.time(f'imported materials')

  if config.IMPORT_MESH:
    build_mesh()
    stopwatch.time(f'build mesh')

  context.select_collection(store.filename)

  for bone in oft.drawable.skel.bone.values():
    import_model(bone)

  stopwatch.stop()

  context.clean_unused()
  pass
