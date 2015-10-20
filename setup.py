#!/usr/bin/env python3
import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        super().initialize_options()
        self.pytest_args = []

    def finalize_options(self):
        super().finalize_options()
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        exit_code = pytest.main(self.pytest_args)
        sys.exit(exit_code)


def read(*path):
    return open(os.path.join(os.path.dirname(__file__), *path)).read()


setup(
    name='tchart',
    version='1.0.0',
    url='https://github.com/andras-tim/tchart',
    license='GPLv2',
    author='Andras Tim',
    author_email='andras.tim@gmail.com',
    description='Minimal graph renderer for fixed size canvas',
    long_description=read('README.rst'),

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Visualization',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3',
    ],
    keywords='chart bar barchart',

    install_requires=[
        'numpy',
    ],
    tests_require=[
        'pytest'
    ],

    packages=find_packages(exclude=['tests']),
    cmdclass={
        'test': PyTest
    },
)
