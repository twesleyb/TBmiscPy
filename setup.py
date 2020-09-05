#!/usr/bin/env python3

'''
This is a regular python file!
'''

import setuptools

#with open("README.md", "r") as fh:
#    long_description = fh.read()

setuptools.setup(

    name="twesleyb",

    version="0.0.1",

    author="Tyler W A Bradshaw",

    author_email="twesleyb10@gmail.com",

    maintainer="twesleyb",

    maintainer_email="twesleyb10@gmail.com",

    url="https://github.com/twesleyb/TBmiscPy",

    description="miscellanous python functions",

    #long_description=long_description,

    #long_description_content_type="",

    download_url="https://github.com/twesleyb/TBmiscPy",

    packages=['TBmiscPy'],

    package_dir={'TBmiscPy':'src/'},

    package_data={'TBmiscPy' : ['data/*']},

    #data_files=[(data,[])],

    #packages=setuptools.find_packages(), # automatically finds python code

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: None"
    ],

    python_requires='>=3.6',

    requires = ['numpy'],
)
