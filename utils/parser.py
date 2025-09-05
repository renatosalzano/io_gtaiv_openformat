import os
import builtins

from .string import is_int, to_float, is_float

from typing import Literal, Callable

Types = Literal['oft', 'mesh', 'child', 'skel']

class ParserMethods:

  _list = False

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
  

  def set(this, key, value, item: list[str]):

    if has_setter(this, key):
      # print(f'{key} is protected')
      return

    if hasattr(this, key):

      v = getattr(this, key)

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
        case builtins.int:
          value = int(value)
        case builtins.str:
          value = " ".join(value)
      
      setattr(this, key, value)
    else:
      print(f'{key} not exist')

class Parser:

  def __init__(this, filepath: str, ctor):

    print('parse', filepath)

    file = open(filepath, 'r')

    # this.ctor: ParserMethods = ctor
    this.ext: Types = os.path.splitext(filepath)[1]
    this.lines = file.readlines()
    this.index = 0

    this.prev_line: str = ''
    this.curr_line: str = ''

    this.parse(ctor)

    file.close()

  
  def parse(this, ctor: ParserMethods):

    path = ''

    init_blocks = False
    root_block: ParserMethods = ctor
    curr_block: ParserMethods | None = ctor
    ref = [ctor]

    for index, line in enumerate(this.lines):

      this.index = index
      this.prev_line = this.curr_line
      this.curr_line = clean_line(line)

      if "{" in line:
        type, value = this.start_block()

        # get nested block
        print(f'BLOCK - {type}')

        if getattr(curr_block, '_list') == True:
          print(f'BLOCK LIST - {type}')
          continue
        
        if has_setter(curr_block, type):
          set_block: Callable[[str], ParserMethods] = get_setter(curr_block, type)
          curr_block = set_block(value)
        else:

          if hasattr(curr_block, type):
            curr_block = getattr(curr_block, type)
          else:
            print(f'{type} - is not defined')
            

        ref.append(curr_block)
        continue

      if "}" in line:

        ref.pop()

        if len(ref) != 0:
          curr_block = ref[-1]
        else:
          curr_block = None
        continue


      if curr_block is not None:
        item = this.curr_line.split(' ')

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

    return type.lower(), value


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