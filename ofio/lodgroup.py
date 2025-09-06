from ..utils.parser import ParserMethods
from ..utils import debug, path
from .. import config

class Lodgroup(ParserMethods):

  def __init__(this):
    this.high = ""
    this.med = ""
    this.low = ""
    this.vlow = ""
    this.center = (0.0, 0.0, 0.0)
    this.AABBMin = (0.0, 0.0, 0.0)
    this.AABBMax = (0.0, 0.0, 0.0)
    this.radius = 0.0

    this._lods: dict[str, list[str]] = {}


  def set(this, key, value, item):

    match key:
      case 'high' | 'med' | 'low' | 'vlow':

        if value[0] != 'none':
          count, filepath, *_ = value
          count = int(count)

          this._lods[key] = []

          for _ in range(count):
            debug.log(f'[lodgroup] lod "{key}": {filepath}')
            this._lods[key].append(path.join(config.root_dir, filepath))

        super().set(key, value, item)

      case _:
        super().set(key, value, item)

  
  def get_lods(this):
    return this._lods

  # def set(this, key, value, item):

  #   match key:
  #     case 'high' | 'med' | 'low' | 'vlow':
  #       setattr(this, key, value)
  #     case _:
  #       super().set(key, value, item)