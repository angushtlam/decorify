from setuptools import setup

setup(
    name='waveshare-epd',
    description='Waveshare e-Paper Display',
    author='Waveshare',
    packages=['waveshare_epd'],
    install_requires=['RPi.GPIO', 'spidev'],
)

setup(
    name='decorify_client',
    description='On device client for home decor with customizable display',
    author='Angus Lam <me@anguslam.com>',
    packages=['decorify_device'],
    install_requires=['Pillow'],
)
