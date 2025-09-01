import re

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