
from ... import store
from ...utils.parser import ParserMethods
from ...utils import debug
from ...blender.mesh import Mesh

from .idx import Idx
from .verts import Verts
from .veh_chunks import VehChunks

from .types import MeshType

class Mtl(ParserMethods):
  '''Multimaterial mesh'''

  def __init__(this, index: str, skinned: int, chunks: VehChunks, type: MeshType):

    debug.log(f'[mtl] index: "{index}" skinned: "{skinned}"')
    this._is_merging = False

    this.index: str = index
    this.skinned: int = skinned

    this.Prim = 0

    this.idx: Idx = None
    this.verts: Verts = None
    this.chunks: VehChunks = chunks
    this.type: MeshType = type

  def set_Prim(this, integer):

    if this._is_merging:
      return this

    this.Prim = int(integer)
    return this
  

  def set_Idx(this, idx_count):
    # breakpoint()
    if this._is_merging:
      return this.idx
    
    this.idx = Idx(int(idx_count))
    return this.idx
  

  def set_Verts(this, verts_count):

    if this._is_merging:
      return this.verts
    
    this.verts = Verts(int(verts_count), this.skinned)
    return this.verts


  def merge(this):
    this._is_merging = True
    this.idx.set_offset()
    debug.log(f'[mtl] merge offset: {this.idx.offset}')


  def to_mesh(this):

    mesh = Mesh(f'TMP_MESH_MTL_{this.index}', this.verts.vertices, this.idx.faces)
    bmesh = mesh.to_bmesh()

    if this.skinned == 1:
      uv_1 = bmesh.loops.layers.uv.new("UV1")

      if this.type == 'vehicle':
        uv_2 = bmesh.loops.layers.uv.new("UV2")

      ao = bmesh.loops.layers.color.new("ao")

      for face in bmesh.faces:
        for loop in face.loops:

          index = loop.vert.index
          vert = this.verts.get_vert_declaration(index)

          loop[ao] = vert.color.xyzw
          loop[uv_1].uv = vert.uv_1

          if this.type == 'vehicle':
            loop[uv_2].uv = vert.uv_2
            this.chunks.set(vert.bone_name, this.index, loop.vert.index)
    else:
      # MEMO: non skinned have 6 uv
      uv_1 = bmesh.loops.layers.uv.new("UV1")
      ao = bmesh.loops.layers.color.new("ao")

      for face in bmesh.faces:
        for loop in face.loops:

          index = loop.vert.index
          vert = this.verts.get_vert_declaration(index)

          loop[ao] = vert.color.xyzw
          loop[uv_1].uv = vert.uv_0


    mesh.commit_bmesh()
    
    return mesh




