from ...utils import string

class Shader:

  def __init__(this, shader_keys: tuple[str], shader: list[str]):

    for index, value in enumerate(shader):
      key = shader_keys[index]

      value_type = type(getattr(this, key))
      setattr(this, key, string.string_to_value(value, value_type))
      
    pass