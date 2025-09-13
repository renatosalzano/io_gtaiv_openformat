from ...blender.material import Material
from ...blender.shader_node.shaders import PrincipledBSDF, ShaderNodeMix, ShaderBump, ShaderUVMap, ImageTexture, ShaderInvert
from ..shadinggroup import Shader
from ..types import RGBAf, vec3

from ...utils import debug

def shader_to_material(shader: Shader):

  material = Material(shader.mtl_name)

  MaterialOuput = material.get_output()

  color = int(shader.diffuse_color.x) if shader.diffuse_color else 1

  # TODO create COLOR group
  debug.log(f'[shader_to_material] {shader.shader_name}')

  match shader.shader_name:
    case 'gta_vehicle_paint1' | 'gta_vehicle_paint2':

      Main = material.add_node(PrincipledBSDF())
      
      MixColor = material.add_node(ShaderNodeMix(
        Factor=0.1,
        A=RGBAf(0.2, 0.2, 0.2, 1.),
        data_type='RGBA',
        blend_type='ADD'
      ))

      MixColor._Result(Main.BaseColor)

      MudTexture = material.add_node(ImageTexture(
        image=shader.dirt_texture
      ))

      UV2 = material.add_node(ShaderUVMap(
        uv_map='UV2'
      ))

      MudTexture._Color(MixColor.B)
      UV2._UV(MudTexture.Vector)


      NoiseTexture = material.add_node(ImageTexture(
        image=shader.spec_texture
      ))

      UV1 = material.add_node(ShaderUVMap(
        uv_map='UV1'
      ))

      InvertColor = material.add_node(ShaderInvert())

      InvertColor._Color(Main.Roughness)
      NoiseTexture._Color(InvertColor.Color)
      UV1._UV(NoiseTexture.Vector)
    
    case 'gta_vehicle_paint3':

      Main = material.add_node(PrincipledBSDF(
        Roughness=0.0
      ))

      MixColor = material.add_node(ShaderNodeMix(
        data_type='RGBA',
        blend_type='MIX'
      ))

      MixColor._Result(Main.BaseColor)

      LiveryTexture = material.add_node(ImageTexture(
        image=shader.texture2
      ))

      LiveryTexture._Color(MixColor.B)
      LiveryTexture._Alpha(MixColor.Factor)

      UV = material.add_node(ShaderUVMap(
        uv_map='UV2'
      ))

      UV._UV(LiveryTexture.Vector)
    
    case (
      "gta_vehicle_generic"
      | "gta_vehicle_tire" 
      | "gta_vehicle_mesh" 
      | "gta_vehicle_shuts" 
      | "gta_vehicle_badges" 
      | "gta_vehicle_interior2" 
      | "gta_vehicle_rubber" 
      | "gta_vehicle_chrome" 
      | "gta_vehicle_interior"
      ):

      Main = material.add_node(PrincipledBSDF())
      Texture = material.add_node(ImageTexture(
        image=shader.texture
      ))

      Texture._Color(Main.BaseColor)

      if not shader.shader_name == 'gta_vehicle_interior':

        Normal = material.add_node(ShaderBump(
          Strength=0.100
        ))
        NormalTexture = material.add_node(ImageTexture(
          image=shader.bump_texture
        ))

        NormalTexture._Color(Normal.Height)
        Normal._Normal(Main.Normal)

      SpecTexture = material.add_node(ImageTexture(
        image=shader.spec_texture
      ))

      SpecTexture._Color(Main.Roughness)

    case (
      "gta_vehicle_lights" 
      | "gta_vehicle_vehglass" 
      | "gta_vehicle_lightsemissive"
      ):

      Main = material.add_node(PrincipledBSDF(
        Roughness=0.0
      ))

      MixColor = material.add_node(ShaderNodeMix(
        data_type='RGBA',
        blend_type='ADD'
      ))

      MixColor._Result(Main.BaseColor)

      Texture = material.add_node(ImageTexture(
        image=shader.texture
      ))

      Texture._Color(MixColor.A)
      Texture._Alpha(Main.Alpha)

      MudTexture = material.add_node(ImageTexture(
        image=shader.dirt_texture
      ))

      MudTexture._Color(MixColor.B)

      UV1 = material.add_node(ShaderUVMap(uv_map='UV1'))
      UV2 = material.add_node(ShaderUVMap(uv_map='UV2'))

      UV1._UV(Texture.Vector)
      UV2._UV(MudTexture.Vector)

    case 'gta_vehicle_nowater' | 'gta_vehicle_nosplash':

      pass

    case _:

      pass


  Main._BSDF(MaterialOuput.Surface)

  return material




      




