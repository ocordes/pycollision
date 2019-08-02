.. pycollision documentation master file, created by
   sphinx-quickstart on Wed Jul 31 18:27:35 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

2D/3D collision detection library for Python
============================================


This library was born from the idea of detecting collisions
between simple bodies in 2D and 3D. One example was a project
which came from Raytracing to simulate a big set of falling
dominos bricks. However, there is another project for collision
detections `fcl <https://github.com/flexible-collision-library/fcl>`_
(C++ library) and the python implementation
`python-fcl <https://github.com/BerkeleyAutomation/python-fcl/>`_ .
These combination was hard to use in the raytracing project, so there
was a need of a similar library purely written in python which is then
by design OS independent. On the other side the library is using
internally maybe not the fasted algorithms but this is a next step to
optimize the running code.


Contents
---------

.. toctree::
   :maxdepth: 3

   collisions
   modules
   license
   installation


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
