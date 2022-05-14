from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="showz",
    version="0.0.4",
    author="Ark Chauhan",
    url="https://github.com/arknandan25/test_py_pkg",
    description="An application that gets your favourite movie info from CLI!",
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests", "jinja2", "MarkupSafe"],
    entry_points={"console_scripts": ["showz = src.parser:main"]},
)
