import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='mercadolibre-python',
      version='0.2',
      description='API wrapper for MercadoLibre written in Python',
      long_description=read('README.md'),
      url='https://github.com/GearPlug/mercadolibre-python',
      author='Miguel Ferrer',
      author_email='ingferrermiguel@gmail.com',
      license='GPL',
      packages=['mercadolibre'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
