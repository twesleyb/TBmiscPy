#!/usr/bin/env python3

import numpy
import setuptools

#with open("README.md", "r") as fh:
#    long_description = fh.read()

setuptools.setup(
    name="twesleyb", # Replace with your own username
    version="0.0.1",
    author="Tyler W A Bradshaw",
    author_email="twesleyb10@gmail.com",
    description="Miscellanous python functions",
    long_description="",
    long_description_content_type="",
    url="https://github.com/twesleyb/TBmiscPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
