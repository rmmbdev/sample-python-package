#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pip
from setuptools import setup

if int(pip.__version__.split('.')[0]) < 20:
    raise Exception("[pip > 20] is required!")

with open("classifier/requirements.txt") as fp:
    requirements = fp.readlines()

setup(
    name='classifier',
    version='0.1.0',
    description="Python Library for Classify inputs",
    author="Programmed by RMM",
    packages=[
        'classifier',
        'classifier.resources',
    ],
    install_requires=requirements,
    package_data={
        '': [
            '*.json',
            '*.h5',
            '*.pb',
            '*.index',
            '.keep',
            # TODO add your resource file types here
        ]
    }
    ,
    python_requires='>=3.10',  # TODO set your python version
    zip_safe=False
)
