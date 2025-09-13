
class Chunk:

  def __init__(this):
    this.idx: dict[str, set[int]] = {}
    pass


  def set(this, mtl_index: str, idx: int):
    
    if not mtl_index in this.idx:
      this.idx[mtl_index] = set()

    this.idx[mtl_index].add(idx)

class VehChunks:

  def __init__(this):
    this.chunks: dict[str, Chunk] = {}

  
  def set(this, bone_name: str, mtl_index: str, idx: int):

    if not bone_name in this.chunks:
      this.chunks[bone_name] = Chunk()

    this.chunks[bone_name].set(mtl_index, idx)


  def items(this):
    return this.chunks.items()