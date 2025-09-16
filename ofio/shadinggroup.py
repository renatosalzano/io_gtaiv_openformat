from .. import store
from .shaders.shader import Shader
from .shaders.shader_to_material import shader_to_material
from ..utils.parser import ParserMethods
from ..utils import debug


class Shadinggroup(ParserMethods):

  def __init__(this):

    debug.log(f'[shaders] init')

    this.Shaders = Shaders()
  

  def import_materials(this):

    for shader in this.Shaders.values():

      if isinstance(shader, Shader):
        material = shader_to_material(shader)
        store.materials.append(material)



class Shaders(ParserMethods):

  def __init__(this):
    this._is_array_block = True
    this._mtl_index = 0

  def set(this, key, _v, item: list[str]):
    
    shader = Shader(this._mtl_index, item)

    setattr(this, shader.mtl_name, shader)
    debug.log(f'[shaders] add shader: "{shader.shader_name}"')
    
    this._mtl_index += 1

    # this.Shaders.append(shader)
    pass

  def get_shaders(this):
    res: dict[str, Shader] = this.__dict__

    return res
  

  def items(this):
    return this.__dict__.items()
  

  def values(this):
    return this.__dict__.values()


  def to_JSON(this):

    output = {}

    for key, value in this.__dict__.items():

      if isinstance(value, Shader):
        output[key] = value.to_JSON()

    return output


