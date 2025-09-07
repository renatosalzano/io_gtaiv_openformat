from ...utils.parser import ParserMethods
from ..types import vec3int

class Idx(ParserMethods):

  def __init__(this, count: int):

    this._is_array_block = True

    this.idx: list[vec3int] = []
    this.count: int = count
    this.offset: int = 0
    this.max_idx: int = 0


  def set(this, _k, _v, idx_list: list[str]):
    
    tris: list[int] = []

    for idx in idx_list:

      idx = int(idx)
      idx += this.offset

      this.set_max_idx(idx)

      tris.append(idx)

      if len(tris) == 3:
        this.idx.append(vec3int(*tris))
        tris = []


  def set_max_idx(this, idx: int):
    this.max_idx = max(this.max_idx, idx)

  
  def set_offset(this):
    this.offset = this.max_idx - 1

