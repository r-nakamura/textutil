#!/usr/bin/env python3

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="textutil",
    version="1.0",
    author="Ryo Nakamura",
    author_email="nakamura@zebulun.net",
    description="Utility functions to deal with strings including East Asia characters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/r-nakamura/textutil",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
