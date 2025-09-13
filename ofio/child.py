
from .. import store
from ..utils.parser import Parser, ParserMethods
from ..utils import string, path
from .matrix import Matrix
from .lodgroup import Lodgroup
from .bound.bound import Bound
from .bound.boundTransform import BoundTransform


class Drawable(ParserMethods):

  def __init__(this):
    this.lodgroup = Lodgroup()
  

class Fragment(ParserMethods):

  def __init__(this, filepath: str):
    this.drawable = Drawable()
    this.boundTransform = BoundTransform()
    this.bound = Bound()

    Parser(path.join(store.root_dir, filepath), this)



class Child(ParserMethods):

  def __init__(this, filepath: str, group_name: str, add_child_to_fragments):
    this.path = path.normalize(filepath)
    this.pristineMass = 0.0
    this.damagedMass = 0.0
    this.f50: Matrix = None

    this.fragment: Fragment = Fragment(this.path)

    

    add_child_to_fragments(group_name, this)
    pass


  def set_f50(this, _):
    this.f50 = Matrix()
    return this.f50

    
