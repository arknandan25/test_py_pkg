from setuptools import setup, find_packages

setup(
    name="showz",
    version="0.0.3",
    author="Ark Chauhan",
    url="https://github.com/arknandan25/test_py_pkg",
    description="An application that gets your favourite movie info from CLI!",
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
