
from ...utils.parser import Parser, ParserMethods
from ...utils import path, debug
from ... import config
from .mtl import Mtl
from .veh_chunks import VehChunks

class Mesh(ParserMethods):

  def __init__(this, filepath: str):

    this._is_array_block = True

    this.Version = '11 13'
    this.Skinned = 0
    this.mtl: list[Mtl] = []
    this.lod = this.set_lod(filepath)

    this.chunks = VehChunks()

    this.parse(path.join(config.root_dir, path.normalize(filepath)))

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

    debug.log(f'[mesh] build mesh')

    test = this.mtl[0]
    test.to_mesh()
    breakpoint()

    