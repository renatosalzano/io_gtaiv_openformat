
from ... import store
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
    super().__init__()
    this.name = name
    this.type = 'ShaderNodeTexImage'

    if image:

      filepath, filename = path.find_file(
        filename=image,
        to=[
          f'{store.root_dir}/{store.filename}/texture',
          f'{store.root_dir}/vehshare',
          f'{store.root_dir}/texture'
        ],
        extensions=['.png', '.dds']
      )

      if filepath:

        if data.has_image(filename):
          image = data.get_image(filename)
        else:
          image = data.load_image(filepath)

        this.settings['image'] = image
    


  @property
  def Vector(this):
    return (this.node, 'Vector', 0)


  def _Color(this, link):
    this.material.link((this.node, 'Color'), link)


  def _Alpha(this, link):
    this.material.link((this.node, 'Alpha'), link)

