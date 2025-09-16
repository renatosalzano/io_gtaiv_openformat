from .group import Group
from .child import Child

from ..utils.parser import ParserMethods

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


  def set_group(this, name: str):
    this.group = { name: Group(name, this.set_child) }
    return this.group.get(name)
  

  def set_child(this, key: str, value: Child):
    this._child[key] = value


  def get_child(this, key: str):
    
    if key in this._child:
      return this._child[key]
    return None