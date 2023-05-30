import os
from PIL import Image

assets_dir = os.path.join(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))), 'assets')


def get_image():
    img = Image.open(os.path.join(assets_dir, 'phoebe_bridgers_punisher.jpg'))
    return img
