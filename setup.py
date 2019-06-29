from setuptools import setup


from pycollision import __version__, __author__



setup(
    name='pycollision',
    version=__version__,
    author=__author__,
    packages=['pycollision'],
    install_requires=[
     'numpy',
    ],
)
