from .fragments import Fragments
from .drawable import Drawable
from .matrix import Matrix

from ..utils.parser import Parser, ParserMethods
from ..utils import debug

class Oft(ParserMethods):

  def __init__(this, filepath: str = ''):

    this.Version = '112 2'
    this.fragments = Fragments()
    this.drawable = Drawable()
    this.f8 = F8()

    Parser(filepath, this)

    # debug.debug_object(this)

    pass


  def get_shaders(this):
    return this.drawable.shadinggroup.shaders.get_shaders()
  

  def import_materials(this):
    this.drawable.shadinggroup.import_materials()


  def get_bone_by_name(this, bone_name: str):
    debug.log(f'[oft] get bone by name "{bone_name}"')
    return this.drawable.skel.get_bone_by_name(bone_name)


  def get_child(this, bone_name: str):
    debug.log(f'[oft] get child "{bone_name}"')
    return this.fragments.get_child(bone_name)
  

  def get_f8(this, index: str) -> Matrix | None:

    return getattr(this.f8, index)


class F8(ParserMethods):

  def __init__(this):
    this._is_array_block = True
    this._set_block = True
    pass

  def set_block(this, key, value):
    setattr(this, key, Matrix())
    return getattr(this, key)




