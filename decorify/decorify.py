import os

from PIL import Image

assets_dir = os.path.join(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))), 'assets')

filenames = [
    'alvvays_antisocialites.jpg',
    'ethel_cain_preachers_daughter.jpg',
    'phoebe_bridgers_punisher.jpg'
]


class Decorify:
    def __init__(self) -> None:
        self.index = 0

    def get_image(self):
        img = Image.open(os.path.join(assets_dir, filenames[self.index]))
        return img

    def next_image(self):
        self.index += 1

        if self.index >= len(filenames):
            self.index = 0
