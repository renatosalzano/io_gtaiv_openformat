from .. import store

from ..utils.parser import ParserMethods
from ..utils import debug, path
from .mesh.mesh import Mesh

from .mesh.types import MeshType


class Lodgroup(ParserMethods):

  def __init__(this, child_lodgroup = False):
    this.high = ""
    this.med = ""
    this.low = ""
    this.vlow = ""
    this.center = (0.0, 0.0, 0.0)
    this.AABBMin = (0.0, 0.0, 0.0)
    this.AABBMax = (0.0, 0.0, 0.0)
    this.radius = 0.0

    this._lods: dict[str, list[str]] = {}
    this._child_lodgroup = child_lodgroup
    this._has_lod_mesh = False


  def set(this, key, value, item):

    match key:
      case 'high' | 'med' | 'low' | 'vlow':

        if value[0] != 'none':
          
          this._has_lod_mesh = True

          count, filepath, *_ = value
          count = int(count)

          this._lods[key] = []

          for _ in range(count):
            debug.log(f'[lodgroup] lod "{key}": {filepath}')
            if this._child_lodgroup:
              this._lods[key].append(path.join(store.root_dir, store.filename, filepath))
            else:
              this._lods[key].append(path.join(store.root_dir, filepath))

        super().set(key, value, item)

      case _:
        super().set(key, value, item)

  
  def get_lods(this):
    return this._lods
  

  def build_mesh(this, mesh_type: MeshType = ''):
      
    lod_mesh: list[Mesh] = []

    if this._has_lod_mesh:

      for lod, filepaths in this.get_lods().items():

        for filepath in filepaths:

          debug.log(f'[lodgroup{".child" if this._child_lodgroup else ""}] build mesh {lod}: "{filepath}"')
          lod_mesh.append(
            Mesh(
              filepath=filepath, 
              type=mesh_type
            )
          )

    return lod_mesh

  # def set(this, key, value, item):

  #   match key:
  #     case 'high' | 'med' | 'low' | 'vlow':
  #       setattr(this, key, value)
  #     case _:
  #       super().set(key, value, item)