from ..utils.parser import ParserMethods
from .shadinggroup import Shadinggroup
from .skel.skel import Skel
from .lodgroup import Lodgroup

from ..utils import debug

class Drawable(ParserMethods):

  def __init__(this):
    this.shadinggroup = Shadinggroup()
    this.skel: Skel = Skel()
    this.lodgroup = Lodgroup()

  
  # def set_skel(this, filepath):

  #   if filepath == '':
  #     return this

  #   debug.log(f'[drawable] - skel path: "{filepath}"')
  #   setattr(this, 'skel', Skel(filepath))
  #   return this.skel