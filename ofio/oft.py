from .fragments import Fragments
from .drawable import Drawable

from ..utils.parser import Parser, ParserMethods
from ..utils import debug

class Oft(ParserMethods):

  def __init__(this, filepath: str = ''):

    this.Version = '112 2'
    this.fragments = Fragments()
    this.drawable = Drawable()
    this.f8 = F8()

    Parser(filepath, this)

    debug.debug_object(this)

    pass


class F8(ParserMethods):

  def __init__(this):
    pass
