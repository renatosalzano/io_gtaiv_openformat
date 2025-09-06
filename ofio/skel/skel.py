from .bone import Bone
from ... import config
from ...utils.parser import Parser, ParserMethods
from ...utils import debug, path

class Skel(ParserMethods):

  def __init__(this, filepath: str):

    this.filepath = path.normalize(filepath)
    this.Version = "107 11"
    this.NumBones = 0
    this.Flags = ""

    this.bone = dict[str, Bone] = {}
    this._bones = list[Bone]

    Parser(path.join(config.root_dir, this.filepath), this)


  def set_bone(this, bone_name):

    try:
      this.bone[bone_name] = Bone(bone_name, this._add_bone)
      return this.bone.get(bone_name)
    except:
      print('ERROR')
      return None
    
  
  def _add_bone(this, bone: Bone):
    this._bones.insert(bone.Index, bone)