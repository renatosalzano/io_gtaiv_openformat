from .bone import Bone
from ... import config
from ...utils.parser import Parser, ParserMethods
from ...utils import debug, path

class Skel(ParserMethods):

  def __init__(this):

    this.skel = ""

    # .skel
    this.Version = "107 11"
    this.NumBones = 0
    this.Flags = ""

    this.bone: dict[str, Bone] = {}

    this._bones: dict[str, str] = {}

  def set(this, key, value, _):
    
    if key == 'skel':
      this.skel = path.normalize(value)
      debug.log(f'[skel] filepath: "{this.skel}"')
      Parser(path.join(config.root_dir, this.skel), this)
    else:
      super().set(key, value, _)


  # def set_children(this, number):
    
  #   # breakpoint()
  #   # this.Children = number
  #   return this


  def set_bone(this, bone_name):

    debug.log(f'[skel] add bone: "{bone_name}"')

    this.bone[bone_name] = Bone(bone_name, this._add_bone)
    return this.bone.get(bone_name)
    
  
  def _add_bone(this, bone: Bone):
    this._bones[bone.Index] = bone.name
    config.bones_map[bone.Index] = bone.name

  
  def _get_bone(this, bone_index: str):
    
    if bone_index in this._bones:
      return this._bones[bone_index]
    else:
      raise IndexError(f"Index out of range for vec3 (expected 0 to {this._bones.__len__() - 1})")