
from ... import store
from ...utils.parser import ParserMethods
from ...utils import debug
from ...blender.mesh import Mesh

from .idx import Idx
from .verts import Verts
from .veh_chunks import VehChunks

class Mtl(ParserMethods):
  '''Multimaterial mesh'''

  def __init__(this, index: str, skinned: int, chunks: VehChunks):

    debug.log(f'[mtl] index: "{index}" skinned: "{skinned}"')

    this.index: str = index
    this.skinned: int = skinned

    this.Prim = 0

    this.idx: Idx = None
    this.verts: Verts = None
    this.chunks: VehChunks = chunks

  def set_prim(this, integer):

    this.Prim = int(integer)
    return this
  

  def set_idx(this, idx_count):
    # breakpoint()
    this.idx = Idx(int(idx_count))
    return this.idx
  

  def set_verts(this, verts_count):
    
    this.verts = Verts(int(verts_count), this.skinned)
    return this.verts


  def merge(this):
    this.idx.set_offset()


  def to_mesh(this):

    mesh = Mesh(f'TMP_MESH_MTL_{this.index}', this.verts.vertices, this.idx.faces)
    bmesh = mesh.to_bmesh()

    uv_1 = bmesh.loops.layers.uv.new("UV1")

    if store.is_vehicle:
      uv_2 = bmesh.loops.layers.uv.new("UV2")

    ao = bmesh.loops.layers.color.new("ao")

    for face in bmesh.faces:
      for loop in face.loops:

        index = loop.vert.index
        vert = this.verts.get_vert_declaration(index)

        loop[uv_1].uv = vert.uv_1
        loop[ao] = vert.color.rgba

        if store.is_vehicle:
          loop[uv_2].uv = vert.uv_2

          this.chunks.set(vert.bone_name, this.index, loop.vert.index)
          # self.chunks[chunk_index].set(mtl_index, loop.vert.index)

    mesh.commit_bmesh()
    
    return mesh




