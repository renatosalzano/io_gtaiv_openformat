from .shaders import gta, gta_decal, gta_emissive, gta_glass, gta_hair, gta_normal, gta_ped, gta_reflect, gta_spec, gta_terrain, gta_vehicle
from ..utils.parser import ParserMethods
from ..utils import path

index = {
  'gta': gta,
  'vechicle': gta_vehicle,
  'decal': gta_decal,
  'emissive': gta_emissive,
  'glass': gta_glass,
  'hair': gta_hair,
  'normal': gta_normal,
  'ped': gta_ped,
  'reflect': gta_reflect,
  'spec': gta_spec,
  'terrain': gta_terrain,
}

class Shadinggroup(ParserMethods):

  def __init__(this):
    this.Shaders: list[Shader] = []
    this._list = True
    pass

  def set_Shaders(this, value):
    print(value)
    pass

  def set(this, key, _v, item: list[str]):
    
    if key != 'Shaders':
      shader = Shader(item)

    # this.Shaders.append(shader)
    pass


class Shader:

  def __init__(this, shader: list[str]):
    shader_name, *shader_data = shader

    shader_name = path.filename(shader_name)

    index_key = shader_name.split("_")[1]

    if hasattr(index, index_key):
      t = getattr(index, index_key)

    print(shader_name)
    pass