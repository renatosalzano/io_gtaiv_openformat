
from ... import config
from ...utils import path
from ...ofio.types import RGBAf, vec3, vec2
from .ShaderNode import ShaderNode
from .. import data
                    
class ImageTexture(ShaderNode):

  def __init__(
    this,
    name: str = None,
    image: str = ''
  ):
    this.name = name
    this.type = 'ShaderNodeTexImage'

    if image:

      filepath, filename = path.find_file(
        filename=image,
        to=[
          f'{config.root_dir}/{config.filename}/texture',
          f'{config.root_dir}/vehshare',
          f'{config.root_dir}/texture'
        ],
        extensions=['.png', '.dds']
      )

      if filepath:

        if data.has_image(filename):
          image = data.get_image(filename)
        else:
          image = data.load_image(filepath)

        this.settings.image = image
    


  @property
  def Vector(this):
    return (this.node, 'Vector', 0)


  def Color(this, link):
    this.material.link((this.node, 'Color'), link)


  def Alpha(this, link):
    this.material.link((this.node, 'Alpha'), link)

