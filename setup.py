from setuptools import setup


from pycollision import __version__, __author__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pycollision',
    version=__version__,
    author=__author__,
    author_email="ocordes@astro.uni-bonn.de",
    description="Python module to detect collisions between 2d/3d objects", 
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ocordes/pycollision",
    packages=['pycollision'],
    install_requires=[
     'numpy',
     'pytypevalidation',
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
    ],
)
