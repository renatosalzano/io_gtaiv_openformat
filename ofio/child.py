
from .. import store
from ..utils.parser import Parser, ParserMethods
from ..utils import string, path
from .matrix import Matrix
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
    this.f50: Matrix = None

    this.fragment: Fragment = Fragment()

    Parser(path.join(store.root_dir, this.path), this.fragment)

    add_child_to_fragments(group_name, this)
    pass


  def set_f50(this, _):
    this.f50 = Matrix()
    return this.f50

    
