try:
    from setuptools import setup
    setup  # quiet "redefinition of unused ..." warning from pyflakes
    # arguments that distutils doesn't understand
    setuptools_kwargs = {
        'install_requires': [
            'numpy',
            'scipy'
        ],
        'provides': ['rdc'],
    }
except ImportError:
    from distutils.core import setup
    setuptools_kwargs = {}

setup(name='rdc',
      version="1.0",
      description=(
        'Implements the Randomized Dependence Coefficient'
      ),
      author='Gary Doran',
      author_email='garydoranjr@gmail.com',
      url='https://github.com/garydoranjr/rdc.git',
      license="BSD compatable (see the LICENSE file)",
      packages=['rdc'],
      platforms=['unix'],
      **setuptools_kwargs
)

