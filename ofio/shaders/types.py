from ...utils import debug
from typing import NewType
from ..types import vec3, vec4

Vec3 = vec3(0.0, 0.0, 0.0)
Vec4 = vec4(0.0, 0.0, 0.0, 0.0)
dimmerset = (Vec4, Vec4, Vec4, Vec4, Vec4, Vec4, Vec4, Vec4, Vec4, Vec4, Vec4, Vec4, Vec4, Vec4, Vec4)

dimmerset_vec4 = NewType('dimmerset_vec4', tuple[vec4, vec4, vec4, vec4, vec4, vec4, vec4, vec4, vec4, vec4, vec4, vec4, vec4, vec4, vec4])

types = {
  "bump_strength": float(),
  "bump_strength_vec4": Vec4,
  "bump_texture": str(),

  "dirt_decal_mask": Vec4,
  "dirt_texture": str(),
  "dimmerset": dimmerset,
  
  "emissive_multiplier": float(),
  "environment_texture": str(),

  "fade_thickness": float(),
  
  "diffuse_color": Vec3,
  "diffuse2_spec_mod": Vec4,
  
  "parallax_scale_bias": float(),
  
  "reflective_pow": float(),
  
  "spec_map_strenght": Vec3,
  "spec_texture": str(),
  "spec_color_factor": float(),
  "spec_factor": float(),
  "spec_factor": float(),
  "spec2_color_strength": Vec4,
  "spec2_factor": Vec4,

  "texture": str(),
  "texture2": str(),
  "texture_0": str(),
  "texture_1": str(),
  "texture_2": str(),
  "texture_3": str(),
  
  "zshift": float(),
}


def get_type(key: str):
  if key in types:
    return types[key]
  else:
    debug.log(f'[types] - "{key}" is not defined')
    return None