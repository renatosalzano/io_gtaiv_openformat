
from .ofio.oft import Oft
from .ofio.skel.bone import Bone
from .ofio.mesh.mesh import Mesh

from .utils import path, debug, log
from .blender import context
from bpy.types import Object
from . import store, config

from mathutils import Matrix
# oft: Oft = None
# lod_mesh: list[Mesh] = []
# tmp_object: dict[str, Object] = {}
# tmp_col_object: dict[str, Object] = {}


class import_oft:

  def __init__(this, filepath):

    stopwatch = log.StopWatch()

    store.root_dir = path.dirname(filepath)
    store.filename = path.filename(filepath)
    store.is_vehicle = True

    src = f'{store.root_dir}/{store.filename}'

    if path.is_dir(src):
      context.clean_unused()

      store.main_collection = context.new_collection(
        name=store.filename,
        append_to_scene=True
      )

    else:
      raise ImportError(f'missing directory "{store.filename}" in {filepath}')

    debug.log(f'import model at "{filepath}"')

    this.oft = Oft(filepath)
    this.lod_mesh: list[Mesh] = []
    this.tmp_object: dict[str, Object] = {}
    # breakpoint()

    stopwatch.time(f'imported data')

    if config.IMPORT_MATERIALS:

      this.oft.import_materials()
      stopwatch.time(f'imported materials')

    if config.IMPORT_MESH:
      
      this.build_mesh()
      stopwatch.time(f'build mesh')

    
    context.select_collection(store.main_collection.name)

    for bone in this.oft.drawable.skel.bone.values():
      this.import_model(bone)

    # this.test()

    stopwatch.stop()

    context.clean_unused()
    # finish

  def test(this):

    for child in this.oft.fragments._child.values():

      bone = this.oft.get_bone_by_name(child._name)

      x, y, z = bone.WorldOffset

      location = (-x, -y, z)

      bone_transform = Matrix().Translation(location)

      # testing
      f8 = this.oft.get_f8(child.group_index).get_matrix()

      # boundTransform * inverse(f50) * _bound.parent.transform
      f50 = child.f50.get_matrix()
      boundTransform = child.boundTransform

      parent_transform = Matrix()

      debug.log(f'[TEST F8] {child._name}')

      if child._parent:
        parent_bone = this.oft.get_bone_by_name(child._parent._name)
        x, y, z = parent_bone.WorldOffset
        # debug.log(f'parent world offset: {parent_bone.WorldOffset}')
        parent_transform.Translation((-x, -y, z))
     
      calc_f8 = parent_transform
      debug.log(f'F8 {f8}')
      # debug.log(f'F50 {f50}')
      # debug.log(f'boundTransform {boundTransform}')
      # debug.log(f'parentTransform {parent_transform}')
      debug.log(f'CALC F8 {bone_transform}')
      # print('\n--- f8 ---\n', f8, '\n--- calc f8 ---\n', calc_f8)


  def import_model(this, bone: Bone, parent: Object = None):

    debug.log(f'[import_oft] "{bone.name}"')

    x, y, z = bone.WorldOffset

    location = (-x, -y, z)

    bone_obj = context.create_empty(bone.name, location)
    this.set_properties(bone_obj, bone)

    if config.IMPORT_MESH:
      this.import_mesh(bone.name, bone_obj)

    this.import_child(bone.name, bone_obj, parent)


    if bone.has_childrens():

      for child_bone in bone.children.values():

        this.import_model(child_bone, bone_obj)

    if parent:
      context.set_parent(parent, bone_obj)


  def import_mesh(this, bone_name: str, parent_object: Object):

    for Mesh in this.lod_mesh:
      
      if Mesh.has_object(bone_name):

        mesh_obj = Mesh.get_object(bone_name)
        
        context.set_parent(parent_object, mesh_obj)
        
        hide = False if mesh_obj.name.startswith('L0') else True

        mesh_obj.hide_set(hide)


  def import_child(this, bone_name: str, bone_object: Object, parent_object: Object):

    child = this.oft.get_child(bone_name)

    if child:

      is_wheel = bone_name.startswith('wheel')

      if config.IMPORT_MESH:

        child_lod_mesh = child.build_mesh()

        if is_wheel:
          index = bone_name.split('_')[1] # wheel_lf
          wheelname = f'wheelmesh_{index}'

        for child_mesh in child_lod_mesh:

          for mesh_name, mesh_object in child_mesh.objects.items():

            if child_mesh.Lod > 0:
              wheelname = f'{wheelname}_l{child_mesh.Lod}'

            if is_wheel:
              this.tmp_object[wheelname] = mesh_object

      if config.IMPORT_COLLISION:

        child_bound = child.build_bound()

        if child_bound:

          context.set_parent(bone_object, child_bound, True)

          child_bound.hide_set(config.HIDE_COLLISION)

      
      # f50.invert()
      
      # breakpoint()



    if bone_name in this.tmp_object:

      if bone_name.startswith('wheel'):
        this.tmp_object[bone_name].location = parent_object.location
      
      context.set_parent(parent_object, this.tmp_object[bone_name])

  


  def build_mesh(this):

    mesh_list = this.oft.drawable.lodgroup.build_mesh('vehicle')

    for mesh in mesh_list:
      this.lod_mesh.append(mesh)


  def set_properties(this, object: Object, bone: Bone):

    object['Flags'] = " ".join(bone.Flags)
    object['Index'] = bone.Index
    object['Id'] = bone.Id
    object['Mirror'] = bone.Mirror
    object['LocalOffset'] = bone.LocalOffset
    object['RotationEuler'] = bone.RotationEuler
    object['RotationQuaternion'] = bone.RotationQuaternion
    object['Scale'] = bone.Scale
    object['WorldOffset'] = bone.WorldOffset
    object['Orient'] = bone.Orient
    object['Sorient'] = bone.Sorient
    object['TransMin'] = bone.TransMin
    object['TransMax'] = bone.TransMax
    object['RotMin'] = bone.RotMin
    object['RotMax'] = bone.RotMax


def InvertedMatrix(location: tuple[float]):
  x, y, z = location

  return Matrix().Translation((-x, -y, z))