from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()
    print (required)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="first_pip_module",
    version="0.1",
    author="Sanjay Singh Shekhawat",
    author_email="shekhawatsanjay23@gmail.com",
    description="This is a python module.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="git@github.com:sanster23/makefiles.git",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=required, 
    zip_safe=False
)