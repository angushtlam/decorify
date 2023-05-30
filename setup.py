from setuptools import setup

setup(
    name='waveshare-epd',
    description='Waveshare e-Paper Display',
    author='Waveshare',
    packages=['waveshare_epd'],
    install_requires=['RPi.GPIO', 'spidev'],
)

setup(
    name='decorify',
    description='Home decor with customizable display',
    author='Angus Lam <me@anguslam.com>',
    packages=['decorify'],
    install_requires=['Pillow'],
)
