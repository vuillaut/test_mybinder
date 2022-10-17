#!/usr/bin/env python

from pathlib import Path

from setuptools import find_packages, setup


setup(
    name='testmybinder',
    description="testmybinder",
    setup_requires="setuptools_scm",
    install_requires=[
        "markdown>=3.3.6,<4.0",
    ],
    packages=find_packages(),
    scripts=[],
    tests_require=[],
    author='Thomas Vuillaume',
    author_email='vuillaume@lapp.in2p3.fr',
    license='MIT',
)
