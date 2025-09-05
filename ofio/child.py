
from .. import config
from ..utils.parser import Parser, ParserMethods
from ..utils import string, path
from .f50 import F50
from .lodgroup import Lodgroup


class Drawable(ParserMethods):

  def __init__(this):
    this.lodgroup = Lodgroup()
  

class Fragment(ParserMethods):

  def __init__(this):
    this.drawable = Drawable()
    this.boundTransform = None
    this.bound = None



class Child(ParserMethods):

  def __init__(this, filepath: str, group_name: str, add_child_to_fragments):
    this.path = path.normalize(filepath)
    this.pristineMass = 0.0
    this.damagedMass = 0.0
    this.f50: F50 = None

    this.fragment: Fragment = Fragment()

    # Parser(path.join(config.root_dir, this.path), this.fragment)

    add_child_to_fragments(group_name, this)
    pass


  def set_f50(this, _):
    this.f50 = F50()
    return this.f50

    
