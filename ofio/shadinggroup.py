from .shaders import gta, gta_decal, gta_emissive, gta_glass, gta_hair, gta_normal, gta_ped, gta_reflect, gta_spec, gta_terrain, gta_vehicle, types
from .shaders.types import vec3, vec4, dimmerset_vec4
from ..utils.parser import ParserMethods
from ..utils import path, string, debug
import builtins
from typing  import NewType

index = {
  'vehicle': gta_vehicle,
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
    this.shaders = Shaders()
    pass

  def set_Shaders(this, value):
    print(value)
    pass


class Shaders(ParserMethods):

  def __init__(this):
    this._list = True

  def set(this, key, _v, item: list[str]):
    
    shader = Shader(item)
    setattr(this, shader.shader_name, shader)
    print('setted', shader.shader_name)

    # this.Shaders.append(shader)
    pass

  def to_JSON(this):
    print('try to JSONIFY')
    return {}


class Shader:

  def __init__(this, shader: list[str]):

    shader_name, *shader_data = shader

    this.shader_name = path.filename(shader_name)

    this.bump_strength: float = None
    this.bump_strength_vec4: vec4 = None
    this.bump_texture: str = None

    this.dirt_decal_mask: vec4 = None
    this.dirt_texture: str = None

    this.dimmerset: dimmerset_vec4 = None
    this.emissive_multiplier: float = None
    this.environment_texture: str = None

    this.fade_thickness: float = None
    this.diffuse_color: vec3 = None
    this.diffuse2_spec_mod: vec4 = None
    this.parallax_scale_bias: float = None
    this.reflective_pow: float = None

    this.spec_map_strenght: vec3 = None
    this.spec_texture: str = None
    this.spec_color_factor: float = None
    this.spec_factor: float = None
    this.spec_factor: float = None

    this.spec2_color_strength: vec4 = None
    this.spec2_factor: vec4 = None

    this.texture: str = None
    this.texture2: str = None
    this.texture_0: str = None
    this.texture_1: str = None
    this.texture_2: str = None
    this.texture_3: str = None

    this.zshift: float = None

    index_key = this.shader_name.split("_")[1]

    module = index[index_key] if index_key in index else gta

    # if hasattr(index, index_key):
    #   module = getattr(index, index_key)
    debug.log(f'[shader] "{this.shader_name}"')
    
    if hasattr(module, this.shader_name):
      shader_keys = getattr(module, this.shader_name)
      this.parse_shader(shader_keys, shader_data)

    else:
      debug.log(f'[shader] - ERROR - {this.shader_name} is not defined')

    pass


  def parse_shader(this, shader_keys: tuple[str], shader_data: list[str]):
    
    keys_len = len(shader_keys)
    data_len = len(shader_data)

    index = 0

    for key in shader_keys:

      vecT, type_value = types.get_type(key)
      value = shader_data[index]

      debug.log(f'[shader] "{key}": {value}')
      # optional value
      if key.startswith('?'):
        
        key = key[1:]

        if keys_len > data_len:
          # skip optional value
          debug.log(f'[shader] - optional "{key}" is not present')
          continue

      match (type_value):
        case builtins.tuple:
          data = value.split(';')
          parsed_value = []

          if key == 'dimmerset':

            for i in range(15):

              Vec4 = (
                float(data[0 + i]),
                float(data[1 + i]),
                float(data[2 + i]),
                float(data[3 + i])
              )

              parsed_value.append(Vec4)
            pass
          else:

            for i in range(len(vecT)):
              parsed_value.append(float(data[i]))
            pass

          setattr(this, key, parsed_value)

          pass
        case builtins.float:
          setattr(this, key, float(value))
          pass

      index += 1
      
      # end for
    
    if index != data_len:
      debug.log(f'[shader] - ERROR - mismatch')


  def to_JSON(this):

    output = {}

    # for key, value in this.__dict__.items():

    #   if value is not None:
    #     output[key] = value

    return output