
from ...utils.parser import Parser, ParserMethods
from ...utils import path, debug
from ... import store
from .mtl import Mtl
from .bounds import Bounds
from .veh_chunks import VehChunks
from ...blender import mesh, context

from bpy.types import Object
from .types import MeshType



class Mesh(ParserMethods):

  def __init__(this, filepath: str, type: MeshType):

    this._is_array_block = True
    this.type: MeshType = type

    this.Version = '11 13'
    this.Skinned = 0
    this.Bounds: Bounds = None
    this.mtl: list[Mtl] = []

    this.lod_prefix: str = ''
    this.Lod: int = 0
    this.set_lod(filepath)

    this.type = type
    this.chunks = VehChunks()
    this.objects: dict[str, Object] = {}

    this.filename = path.filename(filepath)
    this.mesh_name = ''

    if this.filename.startswith('wheel'):
      this.type = 'wheel'
      this.mesh_name = f'{this.lod_prefix}_wheelmesh'

    this.parse(path.join(store.root_dir, path.normalize(filepath)))

    this.build()


  def set_Bounds(this, length):
    this.Bounds = Bounds()
    return this.Bounds


  def set_Mtl(this, index: str):
    
    # index = int(index)

    curr_mtl = this.mtl[-1] if this.mtl else None

    if curr_mtl is not None and curr_mtl.index == index:
      debug.log(f'[mesh] merge Mtl {index}')
      curr_mtl.merge()
      return curr_mtl
    else:
      debug.log(f'[mesh] add Mtl {index}')
      this.mtl.append(Mtl(index, this.Skinned, this.chunks, this.type))

    return this.mtl[-1]
  

  def set_lod(this, filepath: str):

    if 'high' in filepath:
      this.Lod = 0
    if 'med' in filepath:
      this.Lod = 1
    if 'low' in filepath:
      this.Lod = 2
    if 'vlow' in filepath:
      this.lod = 3

    this.lod_prefix = f'L{this.Lod}'
  
  def build(this):

    debug.log(f'[mesh] build filename="{this.filename}" type={this.type}')

    match this.type:
      case 'vehicle':
        this.build_chunked()
      case 'wheel':
        this.build_mesh()
      case _:
        debug.log(f'[mesh] build error: unknown type')
        raise ImportError('BUILD ERROR - unknown mesh type')
      

  def build_chunked(this):

    mtl_mesh: dict[str, mesh.Mesh] = {}

    for mtl in this.mtl:
      mtl_mesh[mtl.index] = mtl.to_mesh()


    for bone_name, chunk in this.chunks.items():
      
      result_mesh = mesh.Mesh(f'{this.lod_prefix}_{bone_name}')
      mesh_to_join = [result_mesh.to_object()]

      for mtl_index, idx in chunk.idx.items():

        tmp_mesh = mesh.Mesh(f'TMP_MESH_{this.lod_prefix}_{bone_name}')
        tmp_mesh._mesh = mtl_mesh[mtl_index]._mesh.copy()

        bmesh = tmp_mesh.to_bmesh()

        wrong_count = 0

        for vert_idx in idx:
          try:
            bmesh.verts[vert_idx].select = False
          except:
            wrong_count += 1

        if wrong_count > 0:
          error = f'ERROR: {bone_name} {mtl_index}: {wrong_count} vertex out of range'
          debug.log(error)
          raise ImportError(error)
        
        tmp_mesh._bmesh.delete_selected_vertices()
        tmp_mesh.commit_bmesh()

        mtl_index = int(mtl_index)

        if int(mtl_index) > (len(store.materials) - 1):
          raise ImportError(f'{mtl_index} out of range {len(store.materials) - 1}')

        tmp_mesh.append_material(store.materials[mtl_index])

        mesh_to_join.append(tmp_mesh.to_object())
      
      this.objects[bone_name] = mesh.join(mesh_to_join, f'{this.lod_prefix}_{bone_name}')

    # for tmp_mesh in mtl_mesh.values():
      
    #   if tmp_mesh._object:
    #     store.main_collection.objects.unlink(tmp_mesh._object)
    
    pass


  def build_mesh(this):

    mesh_to_join = []

    for mtl in this.mtl:

      mtl_index = int(mtl.index)

      tmp_mesh = mtl.to_mesh()
      tmp_mesh.set_name(f'TMP_MESH_{this.filename}')

      tmp_mesh_object = tmp_mesh.to_object()

      tmp_mesh.append_material(store.materials[mtl_index])
      
      mesh_to_join.append(tmp_mesh_object)

    mesh_object = mesh.join(mesh_to_join, this.mesh_name)

    mesh.merge_by_distance(mesh_object)

    this.objects[this.mesh_name] = mesh_object
    pass



  def has_object(this, bone_name: str):

    return bone_name in this.objects
  

  def get_object(this, bone_name: str):

    ret: Object = this.objects[bone_name]
    ret.name = f'{this.lod_prefix}_{bone_name}'
    return ret

    

    