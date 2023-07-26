import os

from PIL import Image

assets_dir = os.path.join(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))), 'assets')

filenames = [
    'alvvays_antisocialites.jpg',
    'conan_gray_superache.jpg',
    'ethel_cain_preachers_daughter.jpg',
    'lana_del_rey_ultraviolence.jpg',
    'men_i_trust_oncle_jazz.jpg',
    'phoebe_bridgers_punisher.jpg'
    'the_weeknd_dawn_fm.jpg'
]


class DecorifyClient:
    def __init__(self) -> None:
        self.index = 0

    def get_image(self):
        img = Image.open(os.path.join(assets_dir, filenames[self.index]))
        return img

    def next_image(self):
        self.index += 1

        if self.index >= len(filenames):
            self.index = 0
