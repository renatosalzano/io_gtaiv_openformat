vec4 = tuple(0.0, 0.0, 0.0, 0.0)

types = {
  "bump_strength": float,
  "bump_texture": str,

  "dirt_decal_mask": vec4,
  "dirt_texture": str,
  "dimmerset_list": tuple(vec4, vec4, vec4, vec4, vec4, vec4, vec4, vec4, vec4, vec4, vec4, vec4, vec4, vec4, vec4),
  
  "emissive_multiplier": float,
  "environment_texture": str,

  "fade_thickness": float,
  
  "diffuse_color": vec4,
  "diffuse2_spec_mod": vec4,
  
  "parallax_scale_bias": float,
  
  "reflective_power": float,
  "reflective_powered": float,
  
  "spec_map_strenght": vec4,
  "spec_texture": str,
  "spec_color_factor": float,
  "spec_factor": float,
  "spec_factored": float,
  "spec2_color_strength": vec4,
  "spec2_factored": vec4,
  
  
  "texture": str,
  "texture2": str,

  "texture_0": str,
  "texture_1": str,
  "texture_2": str,
  "texture_3": str,
  
  "zshift": float,
}