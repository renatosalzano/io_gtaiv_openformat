
from ...utils.parser import Parser, ParserMethods
from ...utils import path, debug
from ... import store
from .mtl import Mtl
from .veh_chunks import VehChunks
from ...blender import mesh, context

from bpy.types import Object

class Mesh(ParserMethods):

  def __init__(this, filepath: str):

    this._is_array_block = True

    this.Version = '11 13'
    this.Skinned = 0
    this.mtl: list[Mtl] = []
    this.lod = this.set_lod(filepath)

    this.chunks = VehChunks()
    this.objects: dict[str, Object] = {}

    this.parse(path.join(store.root_dir, path.normalize(filepath)))

    this.build()


  def set_mtl(this, index: str):
    
    # index = int(index)

    curr_mtl = this.mtl[-1] if this.mtl else None

    if curr_mtl is not None and curr_mtl.index == index:
      debug.log(f'[mesh] merge Mtl {index}')
      curr_mtl.merge()
    else:
      debug.log(f'[mesh] add Mtl {index}')
      this.mtl.append(Mtl(index, this.Skinned, this.chunks))

    return this.mtl[-1]
  

  def set_lod(this, filepath: str):

    if 'high' in filepath:
      return 'L0'
    if 'med' in filepath:
      return 'L1'
    if 'low' in filepath:
      return 'L2'
  

  def build(this):

    mtl_mesh: dict[str, mesh.Mesh] = {}

    for mtl in this.mtl:
      mtl_mesh[mtl.index] = mtl.to_mesh()


    for bone_name, chunk in this.chunks.items():
      
      result_mesh = mesh.Mesh(f'{this.lod}_{bone_name}')
      mesh_to_join = [result_mesh.to_object()]

      for mtl_index, idx in chunk.idx.items():

        tmp_mesh = mtl_mesh[mtl_index].copy()
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
      
      this.objects[bone_name] = mesh.join(mesh_to_join, f'{this.lod}_{bone_name}')

    for tmp_mesh in mtl_mesh.values():
      
      if tmp_mesh._object:
        store.main_collection.objects.unlink(tmp_mesh._object)
    
    pass


  def has_object(this, bone_name: str):

    return bone_name in this.objects
  

  def get_object(this, bone_name: str):

    ret: Object = this.objects[bone_name]
    ret.name = f'{this.lod}_{bone_name}'
    return ret

    

    