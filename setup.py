# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.readlines()

setuptools.setup(
    name="skydiveapp",
    version="0.0.1",
    author="Andrew Hossack",
    author_email="andrew_hossack@outlook.com",
    description="Skydive Utah App",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andrew-hossack/Skydive-Utah-Community",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    include_package_data=True,
    install_requires=requirements,
)
