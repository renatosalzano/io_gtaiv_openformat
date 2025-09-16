class vec4:
    
  def __init__(this, x: float, y: float, z: float, w: float):
    this.x = x
    this.y = y
    this.z = z
    this.w = w


  @property
  def xyzw(this):
    return (this.x, this.y, this.z, this.w)
  

  @property
  def xyz(this):
    return (this.x, this.y, this.z)


  def __getitem__(this, index):
    if index == 0:
      return this.x
    elif index == 1:
      return this.y
    elif index == 2:
      return this.z
    elif index == 3:
      return this.w
    else:
      raise IndexError("Index out of range for vec3 (expected 0, 1, 2, 3)")


  def __setitem__(this, index, value):
    if index == 0:
      this.x = value
    elif index == 1:
      this.y = value
    elif index == 2:
      this.z = value
    elif index == 3:
      this.w = value
    else:
      raise IndexError("Index out of range for vec3 (expected 0, 1, 2, 3)")
      

  def __repr__(this):
    return f"vec3(x={this.x}, y={this.y}, z={this.z}, w={this.w})"


class vec3int:
    
  def __init__(this, x: int, y: int, z: int):
    this.x = x
    this.y = y
    this.z = z


  def __getitem__(this, index):
    if index == 0:
      return this.x
    elif index == 1:
      return this.y
    elif index == 2:
      return this.z
    else:
      raise IndexError("Index out of range for vec3int (expected 0, 1, or 2)")


  def __setitem__(this, index, value):
    if index == 0:
      this.x = value
    elif index == 1:
      this.y = value
    elif index == 2:
      this.z = value
    else:
      raise IndexError("Index out of range for vec3int (expected 0, 1, or 2)")
    

  def __len__(this):
    return 3
      

  def __repr__(this):
    return f"vec3int(x={this.x}, y={this.y}, z={this.z})"
  

class vec3:
    
  def __init__(this, x: float, y: float, z: float):
    this.x = x
    this.y = y
    this.z = z


  def __getitem__(this, index):
    if index == 0:
      return this.x
    elif index == 1:
      return this.y
    elif index == 2:
      return this.z
    else:
      raise IndexError("Index out of range for vec3 (expected 0, 1, or 2)")


  def __setitem__(this, index, value):
    if index == 0:
      this.x = value
    elif index == 1:
      this.y = value
    elif index == 2:
      this.z = value
    else:
      raise IndexError("Index out of range for vec3 (expected 0, 1, or 2)")
      

  def __repr__(this):
    return f"vec3(x={this.x}, y={this.y}, z={this.z})"
  

class vec2:
    
  def __init__(this, x: float, y: float):
    this.x = x
    this.y = y


  def __getitem__(this, index):
    if index == 0:
      return this.x
    elif index == 1:
      return this.y
    else:
      raise IndexError("Index out of range for vec3 (expected 0, 1, or 2)")


  def __setitem__(this, index, value):
    if index == 0:
      this.x = value
    elif index == 1:
      this.y = value
    else:
      raise IndexError("Index out of range for vec3 (expected 0, 1, or 2)")
      

  def __repr__(this):
    return f"vec3(x={this.x}, y={this.y})"
  

class RGBAf:

  def __init__(this, r: float, g: float, b: float, a = 1.0):
    this.r = r
    this.g = g
    this.b = b
    this.a = a

  @property
  def rgb(this):
    return (this.r, this.g, this.b)
  
  @property
  def rgba(this):
    return (this.r, this.g, this.b, this.a)
  

def to_vector(value: list):
  vector_len = len(value)

  if isinstance(value[0], int) and vector_len == 3:
    return vec3int(*value)
  
  match vector_len:
    case 4:
      return vec4(*value)
    case 3:
      return vec3(*value)
    case _:
      return value