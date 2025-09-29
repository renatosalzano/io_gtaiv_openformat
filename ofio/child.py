
from .. import store
from ..utils.parser import Parser, ParserMethods
from ..utils import debug, path
from .matrix import Matrix
from .lodgroup import Lodgroup
from .bound.bound import Bound
from .bound.boundTransform import BoundTransform
from typing import Callable
from .child_struct import ChildStruct

from .mesh.mesh import Mesh
import mathutils


class Child(ParserMethods):

  def __init__(
      this,
      filepath: str,
      bone_name: str,
      set_child_by_bone: Callable,
      group_parent = None
    ):

    this._path = path.normalize(filepath)
    this._name = bone_name
    this._parent: Child = group_parent.child if hasattr(group_parent, 'child') else None
    this._group_index = path.filename(filepath).split('_')[-1]
    this._transform: mathutils.Matrix = None

    this.pristineMass = 0.0
    this.damagedMass = 0.0
    this.f50: Matrix = None

    this.fragment: Fragment = Fragment(this._path)

    set_child_by_bone(bone_name, this)

    pass


  def set_f50(this, _):
    this.f50 = Matrix()
    return this.f50
  

  def build_bound(this):
    debug.log(f'[child] {this._name} - build bound')
    bound = this.fragment.bound.build(this)
    return bound


  def build_mesh(this):
    return this.fragment.drawable.lodgroup.build_mesh()
  

  def has_parent(this):
    return this._parent != None
  

  def on_parse_complete(this):

    # breakpoint()
    this._transform = this.f50.get_matrix()

    if this._parent:
      translation = this._parent._transform.translation
      this._transform.translation += translation
      # parent_transform = this._parent._transform

    

    debug.log(f'[child] {this._name} - TRANSFORM \n {this._transform}')
  

  @property
  def boundTransform(this):
    return this.fragment.boundTransform.get_matrix()

    

class Fragment(ParserMethods):

  def __init__(this, filepath: str):

    string = path.filename(filepath)
    
    last_underscore_index = string.rfind('_')

    if last_underscore_index != -1:
      string = string[:last_underscore_index]

    bound_name = string
    
    this.drawable = Drawable()
    this.boundTransform = BoundTransform()
    this.bound = Bound(bound_name)

    Parser(path.join(store.root_dir, filepath), this)



class Drawable(ParserMethods):

  def __init__(this):
    this.lodgroup = Lodgroup(child_lodgroup=True)