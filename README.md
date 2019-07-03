-Rusinkiewicz

This script "CalculCurvature.py" is a deduction of Rusinkiewicz's paper for curvature estimation . In our case we don't go far to derivatives.

Paper : Estimation of curvatures and their derivatives on triangle Meshes by Rusinkiewicz

You need only numpy module to run the script "CalculCurvature.py", while to run examples, you need also trimesh to work with triangular meshes and matplotlib to do the Delaunay triangulation.



Trimesh is an open source python module dedicated to general mesh processing using only triangular mesh : 
https://github.com/mikedh/trimesh

This method of estimation is used so as many others existing in slam to estimate curvatures on the brain.

Requirements :

Trimesh
~~~~~~~~~~~~~~~~~

User installation
~~~~~~~~~~~~~~~~~

If you already have a working installation of trimesh ,
the easiest way to install trimesh is using ``pip``   ::

    pip install trimesh

or ``conda``::

    conda install trimesh

The documentation includes more detailed `installation instructions <https://trimsh.org/trimesh.html>`_.

  
