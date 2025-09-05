import re
import builtins

def to_float(value: str) -> float:
  value = value.replace(",", ".")
  return float(value)


def is_float(value: str) -> bool:
  try:
    float(value)
    return True
  except:
    return False


def is_int(value: str) -> bool:
  float = to_float(value)
  return float.is_integer()


def to_path(path):
  path = re.sub("\\\\", "/", path)
  return path


def string_to_value(value: str, type_value: type):

  match (type_value):
    case builtins.tuple:
      pass
    case builtins.str:
      return value