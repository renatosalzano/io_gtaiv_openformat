from ...utils.parser import ParserMethods
from ...utils import debug, path

from typing import Callable

class Bone(ParserMethods):

  def _add_bone(bone):
    pass

  def __init__(this, name: str, _add_bone: Callable):

    this.name = name

    this.Flags = ""
    this.Index = 0
    this.Id = 0
    this.Mirror = 0
    this.LocalOffset = (0.0, 0.0, 0.0)
    this.RotationEuler = (0.0, 0.0, 0.0)
    this.RotationQuaternion = (0.0, 0.0, 0.0, 0.0)
    this.Scale = (0.0, 0.0, 0.0)
    this.WorldOffset = (0.0, 0.0, 0.0)
    this.Orient = (0.0, 0.0, 0.0)
    this.Sorient = (0.0, 0.0, 0.0)
    this.TransMin = (0.0, 0.0, 0.0)
    this.TransMax = (0.0, 0.0, 0.0)
    this.RotMin = (0.0, 0.0, 0.0)
    this.RotMax = (0.0, 0.0, 0.0)
    this.Children = 0

    this.children: dict[str, Bone] = None

    this._add_bone = _add_bone


  def set_children(this, count: int):
    # this.Children = count
    return this
  
  def set_bone(this, bone_name):

    if this.children is None:
      this.children = {}

    this.children[bone_name] = Bone(bone_name, this._add_bone)
    
    return this.children.get(bone_name)
  

  def haschildrens(this):
    return this.children is not None

  
  def on_parse_complete(this):
    this._add_bone(this)