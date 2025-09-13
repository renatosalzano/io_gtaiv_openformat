import os
import builtins
from . import debug

from .string import is_int, to_float, is_float
from . import path

from typing import NewType, Literal, Callable

Types = Literal['oft', 'mesh', 'child', 'skel']


class ParserMethods:

  _is_array_block = False
  _set_block = False
  _separator = ' '


  def parse(this, filepath):
    Parser(filepath, this)


  def to_JSON(this):

    output = {}

    for key, value in this.__dict__.items():

      if key.startswith('_'):
        # print('JSON avoid', key)
        continue

      elif isinstance(value, ParserMethods):
        output[key] = value.to_JSON()

      elif isinstance(value, dict):

        output[key] = {}

        for _key, _value in value.items():
          output[key][_key] = _value.to_JSON()

      else:
        output[key] = value

    return output


  def set_block(this, key: str, value: str):
    pass


  def set(this, key, value, item: list[str]):

    debug.log(f'[parser] set {this.__class__.__name__} "{key}": {value}')

    if has_setter(this, key):
      debug.log(f'[parser] "{key}" has custom setter')
      return

    if hasattr(this, key):

      v = getattr(this, key)

      if isinstance(v, ParserMethods):
        debug.log(f'[parser] cannot set "{key}" because is block')
        return

      match type(v):

        case builtins.tuple:
          match type(v[0]):
            # case builtins.str:
            #   value = value
            case builtins.int | builtins.float:
              value = tuple(map(to_float, value))
          pass
        case builtins.float:
          value = float(value)
          pass
        case builtins.int:
          value = int(value)
          pass
        case builtins.str:
          pass
      
      setattr(this, key, value)
      debug.log(f'[parser] setted "{key}": {value}')
    else:
      debug.log(f'[parser] cannot set property: "{key}" in {this.__class__.__name__}')


  def get_name(this):
    return this.__class__.__name__
  
  def get_separator(this):
    return this._separator

  def on_parse_complete(this):
    pass


class Parser:

  def __init__(this, filepath: str, target: ParserMethods):

    debug.log(f'[parser] init parsing: "{filepath}"')

    file = open(filepath, 'r')

    # this.ctor: ParserMethods = ctor
    this.ext: Types = path.ext(filepath)
    this.lines = file.readlines()
    this.index = 0

    this.prev_line: str = ''
    this.curr_line: str = ''

    # if 'mesh' in this.ext:
    #   breakpoint()

    this.parse(target)

    file.close()

  
  def parse(this, ctor: ParserMethods):

    # path = ''

    # init_blocks = False
    # root_block: ParserMethods = ctor
    curr_block: ParserMethods | None = ctor
    ref = [ctor]

    for index, line in enumerate(this.lines):

      this.index = index
      this.prev_line = this.curr_line
      this.curr_line = clean_line(line)

      if "{" in line:

        type, value = this.start_block()

        if this.set_block(curr_block):
          debug.log(f'[parser] SET BLOCK "{curr_block.get_name()}"')
          curr_block = curr_block.set_block(type, value)
          ref.append(curr_block)
          continue

        if has_setter(curr_block, type):
          debug.log(f'[parser] SET BLOCK "{curr_block.get_name()}"')

          set_block: Callable[[str], ParserMethods] = get_setter(curr_block, type)
          curr_block = set_block(value)
          ref.append(curr_block)
          continue


        if this.is_array_block(curr_block):
          debug.log(f'[parser] ARRAY BLOCK "{curr_block.get_name()}"')
          continue

        debug.log(f'[parser] BLOCK "{type}"')

        if hasattr(curr_block, type):
          curr_block = getattr(curr_block, type)
        else:
          debug.log(f'[parser] BLOCK "{type}" is not defined')

        if isinstance(curr_block, list):
          breakpoint()

        if isinstance(curr_block, object):
          ref.append(curr_block)
        else:
          debug.log(f'[parser] ERROR - {curr_block} is not object')
        continue

      if "}" in line:

        curr_block = ref[-1]

        if isinstance(curr_block, ParserMethods):
          debug.log(f'[parser] END BLOCK "{curr_block.get_name()}"')
          curr_block.on_parse_complete()

        ref.pop()

        if len(ref) != 0:
          curr_block = ref[-1]
        else:
          curr_block = None
        continue


      if curr_block is not None:
        separator = curr_block.get_separator() if hasattr(curr_block, '_separator') else " "
        item = this.curr_line.split(separator)

        key, value = unpack(item)

        if value is not None:
          # print('set', key, value)
          curr_block.set(key, value, item)

        
        # name, value = this.curr_line.split(' ')
        # print(name, value)


    pass


  def start_block(this):

    type, *rest = this.prev_line.split(' ')

    value = ''

    if len(rest) > 0:
      value = rest[0]

    return type, value
  

  def set_block(this, curr_block):
    if hasattr(curr_block, '_set_block'):
      return getattr(curr_block, '_set_block')
    return False

  def is_array_block(this, curr_block):
    if hasattr(curr_block, '_is_array_block'):
      return getattr(curr_block, '_is_array_block')
    return False


def has_setter(cls, key):
  setter_key = f'set_{key}'
  return hasattr(cls, setter_key)

def get_setter(cls, key):
  setter_key = f'set_{key}'
  return getattr(cls, setter_key)



def clean_line(string):
  return string.replace('\n', '').replace('\t', '')


def unpack(item: list) -> tuple[str, str | list[str]]:
  
  match len(item):

    case 1:
      return item[0], None
    case 2:
      key, value = item
      return key, value
    case _:
      key, *value = item
      return key, value
