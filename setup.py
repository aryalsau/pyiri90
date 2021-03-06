#!/usr/bin/env python
import setuptools #enables develop
from numpy.distutils.core import setup,Extension
from glob import glob
from os.path import join

try:
    import conda.cli
    conda.cli.main('install','--file','requirements.txt')
except Exception as e:
    print(e)
    import pip
    pip.main(['install','-r','requirements.txt'])

#%% fortran data files
iridata = glob(join('data','*.asc'))
#%% install
setup(name='pyiri90',
      packages=['pyiri90'],
      ext_modules=[Extension(name='iri90',
                    sources=['fortran/iri90.f'],
                    f2py_options=['--quiet'])],
     data_files=[('pyiri90/data',iridata)]
	  )
