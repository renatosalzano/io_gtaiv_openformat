from .child import Child
from ..utils.parser import ParserMethods


class Group(ParserMethods):

  def _add_child(name: str, child: Child):
    pass

  def __init__(this, group_name, add_child_to_fragments):
    this._group_name = group_name

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

    this._add_child = add_child_to_fragments


  def set_group(this, group_name):

    if this.group is None:
      this.group = {}

    name = f'{len(this.group)}.{group_name}'

    try:
      this.group[name] = Group(group_name, this._add_child)
      return this.group.get(name)
    except:
      print('ERROR')
      return None

  def set_child(this, value):

    this.child = Child(value, this._group_name, this._add_child)

    return this.child
  