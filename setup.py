#!/usr/bin/env python
import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ''

    def run_tests(self):
        import shlex
        import pytest

        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


def read(*path):
    with open(os.path.join(os.path.dirname(__file__), *path)) as fd:
        return fd.read()


setup(
    name='tchart',
    version='2.0.0',
    url='https://github.com/andras-tim/tchart',
    license='GPLv3',
    author='Andras Tim',
    author_email='andras.tim@gmail.com',
    platforms='any',
    description='Minimal graph renderer for fixed size canvas',
    long_description=read('README.rst'),

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Visualization',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='chart bar barchart',

    install_requires=read('requirements.txt').splitlines(),
    tests_require=read('requirements-dev.txt').splitlines(),

    packages=find_packages(exclude=['tests']),
    cmdclass={
        'test': PyTest
    },
)
