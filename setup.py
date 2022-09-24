#!/usr/bin/env python
import shutil
import os.path
from distutils.command.build_ext import build_ext
from setuptools import setup, Extension, find_packages


class build_ext(build_ext):
    def run(self):
        pass

    def output_dir(self):
        if not self.inplace:
            return os.path.join(self.get_finalized_command('build').build_platlib, 'invokescons')

        build_py = self.get_finalized_command('build_py')
        package_dir = os.path.abspath(build_py.get_package_dir('invokescons'))
        return package_dir

content = ""
try:
    descriptor = open("readme.md", "r")
    content = descriptor.read()
    descriptor.close()
except:
    content = ""
setup(name='invokescons',
      version='1.7',
      maintainer="Pierce L. Brooks",
      maintainer_email="piercebrks@gmail.com",
      author="Pierce L. Brooks",
      author_email="piercebrks@gmail.com",
      url="https://github.com/PierceLBrooks/invokescons",
      description="SCons - a software construction tool",
      long_description=content,
      long_description_content_type="text/markdown",
      classifiers=["Environment :: Console",
                   "License :: OSI Approved :: MIT License",
                   "Intended Audience :: Developers",
                   "Topic :: Software Development"],
      license="MIT",
      entry_points={
          'console_scripts': [
              'scons = invokescons.command_line:main',
              ]},
      packages=["invokescons"],
      install_requires=[
          "scons",
      ],
      zip_safe=True,
      cmdclass={'build_ext': build_ext})
