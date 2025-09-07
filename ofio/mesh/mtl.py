
from ...utils.parser import ParserMethods
from .idx import Idx
from .verts import Verts

class Mtl(ParserMethods):

  def __init__(this, index: int, skinned: int):
    this.index = index
    this.skinned: int = skinned

    this.Prim = 0

    this.idx: Idx = None
    this.verts: Verts = None

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




