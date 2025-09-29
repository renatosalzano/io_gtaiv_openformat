from .group import Group
from .child import Child

from ..utils.parser import ParserMethods
from ..utils import debug

class Fragments(ParserMethods):

  def __init__(this):

    this.unbrokenCGOffset = (0.0, 0.0, 0.0)
    this.dampingLinearC = (0.0, 0.0, 0.0)
    this.dampingLinearV = (0.0, 0.0, 0.0)
    this.dampingLinearV2 = (0.0, 0.0, 0.0)
    this.dampingAngularC = (0.0, 0.0, 0.0)
    this.dampingAngularV = (0.0, 0.0, 0.0)
    this.dampingAngularV2 = (0.0, 0.0, 0.0)
    this.estimatedCacheSize = 0
    this.estimatedArticulatedCacheSize = 0
    this.becomeRope = 0
    this.artAssetID = 0
    this.attachBottomEnd = 0
    this.minMoveForce = 0.0
    this.CenterOfMass = (0.0, 0.0, 0.0)
    this.gravityFactor = 1.0
    this.buoyancyFactor = 0.0
    this.flags = ""
    this.group: dict[str, Group] = {}

    this._child: dict[str, Child] = {}
    this._child_map: dict[str, Child] = {}


  def set_group(this, name: str):
    this.group = { name: Group(name, this.set_child_by_bone) }
    return this.group.get(name)
  

  def set_child_by_bone(this, bone_name: str, child: Child):
    debug.log(f'[fragments] SET CHILD "{bone_name}"')
    this._child[bone_name] = child
    this._child_map[child._group_index] = child


  def get_child(this, bone_name: str):
    
    if bone_name in this._child:
      debug.log(f'[fragments] FOUND CHILD "{bone_name}"')
      return this._child[bone_name]
    debug.log(f'[fragments] NOT FOUND CHILD "{bone_name}"')
    return None
  
