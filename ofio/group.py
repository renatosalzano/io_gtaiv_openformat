from .child import Child
from ..utils.parser import ParserMethods


class Group(ParserMethods):

  def set_child_by_bone(name: str, child: Child):
    pass

  def __init__(this, name: str, set_child_by_bone, parent = None):
    this._name = name
    this._parent: Group = parent

    this.strength = 0.0
    this.forceTransmissionScaleUp = 0.0
    this.forceTransmissionScaleDown = 0.0
    this.jointStiffness = 0.0
    this.minSoftAngle1 = 0.0
    this.maxSoftAngle1 = 0.0
    this.maxSoftAngle2 = 0.0
    this.maxSoftAngle3 = 0.0
    this.rotationSpeed = 0.0
    this.rotationStrength = 0.0
    this.restoringStrength = 0.0
    this.restoringMaxTorque = 0.0
    this.latchStrength = 0.0
    this.disappearsWhenDead = 0
    this.minDamageForce = 0.0
    this.damageHealth = 0.0

    this.group: dict[str, Group] = None
    this.child: Child = None

    this.set_child_by_bone = set_child_by_bone


  def set_group(this, name: str):

    if this.group is None:
      this.group = {}

    # name = f'{len(this.group)}.{bone_name}'

    try:
      this.group[name] = Group(name, this.set_child_by_bone, this)
      return this.group.get(name)
    except:
      raise ValueError(f'unexpected error with group[{name}]')
      return None


  def set_child(this, value):

    # breakpoint()

    # bone_name = this._name.split('.')[1]

    this.child = Child(value, this._name, this.set_child_by_bone, this._parent)

    return this.child
  