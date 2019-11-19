# encoding: utf-8

from setuptools import setup

setup(name='pygenesis',
      version='0.0.1',
      description='PyGenesis - get access to german statistical offices using the genesis API',
      long_description='The aim of the project is to provide simplified data access to German statistical offices in '
                       'Python using the so-called '
                       '[Genesis API](https://www.destatis.de/EN/Service/OpenData/_node.html).',
      long_description_content_type="text/markdown",
      author='Rudolf Bauer',
      author_email='github@rudi-bauer.com',
      url='https://github.com/rudolf-bauer/genesisclient.git',
      license="MIT",
      packages=['pygenesis'],
      install_requires=['logging',
                        'lxml',
                        'numpy',
                        'pandas',
                        'requests',
                        'urllib3',
                        'zeep'])
