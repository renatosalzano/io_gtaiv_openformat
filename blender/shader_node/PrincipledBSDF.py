
from ...ofio.types import RGBAf, vec3, vec2
from .ShaderNode import ShaderNode
                    
class PrincipledBSDF(ShaderNode):

  def __init__(
    this,
    name: str = None,
    BaseColor: RGBAf = None,
    Metallic: float = None,
    Roughness: float = None,
    IOR: float = None,
    Alpha: float = None,
    Weight: float = None,
    DiffuseRoughness: float = None,
    SubsurfaceWeight: float = None,
    SubsurfaceRadius: vec3 = None,
    SubsurfaceScale: float = None,
    SubsurfaceIOR: float = None,
    SubsurfaceAnisotropy: float = None,
    SpecularIORLevel: float = None,
    SpecularTint: RGBAf = None,
    Anisotropic: float = None,
    AnisotropicRotation: float = None,
    TransmissionWeight: float = None,
    CoatWeight: float = None,
    CoatRoughness: float = None,
    CoatIOR: float = None,
    CoatTint: RGBAf = None,
    SheenWeight: float = None,
    SheenRoughness: float = None,
    SheenTint: RGBAf = None,
    EmissionColor: RGBAf = None,
    EmissionStrength: float = None,
    ThinFilmThickness: float = None,
    ThinFilmIOR: float = None,

  ):
    this.name = name
    this.type = 'ShaderNodeBsdfPrincipled'

    if BaseColor:
      this.inputs.append('Base Color', BaseColor)

    if Metallic:
      this.inputs.append('Metallic', Metallic)

    if Roughness:
      this.inputs.append('Roughness', Roughness)

    if IOR:
      this.inputs.append('IOR', IOR)

    if Alpha:
      this.inputs.append('Alpha', Alpha)

    if Weight:
      this.inputs.append('Weight', Weight)

    if DiffuseRoughness:
      this.inputs.append('Diffuse Roughness', DiffuseRoughness)

    if SubsurfaceWeight:
      this.inputs.append('Subsurface Weight', SubsurfaceWeight)

    if SubsurfaceRadius:
      this.inputs.append('Subsurface Radius', SubsurfaceRadius)

    if SubsurfaceScale:
      this.inputs.append('Subsurface Scale', SubsurfaceScale)

    if SubsurfaceIOR:
      this.inputs.append('Subsurface IOR', SubsurfaceIOR)

    if SubsurfaceAnisotropy:
      this.inputs.append('Subsurface Anisotropy', SubsurfaceAnisotropy)

    if SpecularIORLevel:
      this.inputs.append('Specular IOR Level', SpecularIORLevel)

    if SpecularTint:
      this.inputs.append('Specular Tint', SpecularTint)

    if Anisotropic:
      this.inputs.append('Anisotropic', Anisotropic)

    if AnisotropicRotation:
      this.inputs.append('Anisotropic Rotation', AnisotropicRotation)

    if TransmissionWeight:
      this.inputs.append('Transmission Weight', TransmissionWeight)

    if CoatWeight:
      this.inputs.append('Coat Weight', CoatWeight)

    if CoatRoughness:
      this.inputs.append('Coat Roughness', CoatRoughness)

    if CoatIOR:
      this.inputs.append('Coat IOR', CoatIOR)

    if CoatTint:
      this.inputs.append('Coat Tint', CoatTint)

    if SheenWeight:
      this.inputs.append('Sheen Weight', SheenWeight)

    if SheenRoughness:
      this.inputs.append('Sheen Roughness', SheenRoughness)

    if SheenTint:
      this.inputs.append('Sheen Tint', SheenTint)

    if EmissionColor:
      this.inputs.append('Emission Color', EmissionColor)

    if EmissionStrength:
      this.inputs.append('Emission Strength', EmissionStrength)

    if ThinFilmThickness:
      this.inputs.append('Thin Film Thickness', ThinFilmThickness)

    if ThinFilmIOR:
      this.inputs.append('Thin Film IOR', ThinFilmIOR)


  @property
  def BaseColor(this):
    return (this.node, 'Base Color', 0)


  @property
  def Metallic(this):
    return (this.node, 'Metallic', 1)


  @property
  def Roughness(this):
    return (this.node, 'Roughness', 2)


  @property
  def IOR(this):
    return (this.node, 'IOR', 3)


  @property
  def Alpha(this):
    return (this.node, 'Alpha', 4)


  @property
  def Normal(this):
    return (this.node, 'Normal', 5)


  @property
  def Weight(this):
    return (this.node, 'Weight', 6)


  @property
  def DiffuseRoughness(this):
    return (this.node, 'Diffuse Roughness', 7)


  @property
  def SubsurfaceWeight(this):
    return (this.node, 'Subsurface Weight', 8)


  @property
  def SubsurfaceRadius(this):
    return (this.node, 'Subsurface Radius', 9)


  @property
  def SubsurfaceScale(this):
    return (this.node, 'Subsurface Scale', 10)


  @property
  def SubsurfaceIOR(this):
    return (this.node, 'Subsurface IOR', 11)


  @property
  def SubsurfaceAnisotropy(this):
    return (this.node, 'Subsurface Anisotropy', 12)


  @property
  def SpecularIORLevel(this):
    return (this.node, 'Specular IOR Level', 13)


  @property
  def SpecularTint(this):
    return (this.node, 'Specular Tint', 14)


  @property
  def Anisotropic(this):
    return (this.node, 'Anisotropic', 15)


  @property
  def AnisotropicRotation(this):
    return (this.node, 'Anisotropic Rotation', 16)


  @property
  def Tangent(this):
    return (this.node, 'Tangent', 17)


  @property
  def TransmissionWeight(this):
    return (this.node, 'Transmission Weight', 18)


  @property
  def CoatWeight(this):
    return (this.node, 'Coat Weight', 19)


  @property
  def CoatRoughness(this):
    return (this.node, 'Coat Roughness', 20)


  @property
  def CoatIOR(this):
    return (this.node, 'Coat IOR', 21)


  @property
  def CoatTint(this):
    return (this.node, 'Coat Tint', 22)


  @property
  def CoatNormal(this):
    return (this.node, 'Coat Normal', 23)


  @property
  def SheenWeight(this):
    return (this.node, 'Sheen Weight', 24)


  @property
  def SheenRoughness(this):
    return (this.node, 'Sheen Roughness', 25)


  @property
  def SheenTint(this):
    return (this.node, 'Sheen Tint', 26)


  @property
  def EmissionColor(this):
    return (this.node, 'Emission Color', 27)


  @property
  def EmissionStrength(this):
    return (this.node, 'Emission Strength', 28)


  @property
  def ThinFilmThickness(this):
    return (this.node, 'Thin Film Thickness', 29)


  @property
  def ThinFilmIOR(this):
    return (this.node, 'Thin Film IOR', 30)


  def BSDF(this, link):
    this.material.link((this.node, 'BSDF'), link)

