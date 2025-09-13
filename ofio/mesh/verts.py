from ... import store
from ...utils.parser import ParserMethods
from ...utils import string
from ..types import  vec3, vec2, RGBAf

class Verts(ParserMethods):

  def __init__(this, count: int, skinned: int):
    this._is_array_block = True
    this._separator = '/'
    this._skinned: int = skinned

    this.vertices: list[vec3] = []
    this.vert_declaration: list[SkinnedVert | Vert] = []
    this.count: int = count

  def set(this, _k, _v, vertex_declaration):

    # breakpoint()

    if this._skinned == 1:

      coord, normal, bone_weights, bone_indexes, color, tangent, uv_1, uv_2 = vertex_declaration

      coord = to_vec3(coord)
      color = to_RGBAf(color)

      uv_1 = to_vec2(uv_1)
      uv_2 = to_vec2(uv_2)

      bone_index = get_bone_index(bone_indexes)

      this.vertices.append(coord)
      this.vert_declaration.append(SkinnedVert(coord, color, uv_1, uv_2, bone_index))
    else:
      # TODO wheelmesh
      coord, normal, color, tangents, uv_1, *_ = vertex_declaration
      pass


  def get_vert_declaration(this, index: int):
    return this.vert_declaration[index]




class SkinnedVert:

  def __init__(this, coord: vec3, color: RGBAf, uv_1: vec2, uv_2: vec2, bone_index: int):
    this.coord = coord
    this.color = color
    this.uv_1 = uv_1
    this.uv_2 = uv_2
    this.bone_index = bone_index
    this.bone_name = store.get_bone_name(bone_index)


class Vert:

  def __init__(this, color: RGBAf, uv_1: vec2):
    this.color = color
    this.uv_1 = uv_1
    # TODO
    pass


def to_vec3(value: str) -> vec3:
  x, y, z = string.float_map(value)
  return vec3(-x, -y, z)


def to_vec2(value: str) -> vec2:
  x, y = string.float_map(value)
  return vec2(x, -y + 1)


def to_RGBAf(value: str) -> RGBAf:
  value = value.strip()
  r, g, b, _ = list(map(lambda i: int(i) / 255, value.split(" ")))
  return RGBAf(r, g, b)


def get_bone_index(value: str) -> str:
  value = value.strip()
  index = value.split(" ")[2]
  return index