from setuptools import setup, Extension

module = Extension('myparser.parser', sources=['myparser/parser.c'])

setup(
    name='myparser',
    version='0.1',
    description='A buggy parser',
    packages=['myparser'],
    ext_modules=[module],
)
