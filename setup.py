from setuptools import setup, find_packages

setup(
    name="showz",
    version="0.0.1",
    author="Ark Chauhan",
    # url="https://bit.ly/edeediong-resume",
    description="An application that gets your favourite movie info from CLI!",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests", "jinja2"],
    entry_points={"console_scripts": ["showz = src.parser:main"]},
)
