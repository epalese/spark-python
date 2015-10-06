# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='spark_python',
    version='0.0.1',

    description='Spark Python wrapper',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/pypa/sampleproject',

    # Author details
    author='epalese',
    author_email='leleplx@gmail.com',

    # Choose your license
    license='Apache',

    # What does your project relate to?
    keywords='spark python library',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['spark_python'],

)