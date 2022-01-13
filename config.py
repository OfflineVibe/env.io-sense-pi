from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='env.io Sense-Client for Raspberry Pi (Docker Container)',
    version='0.0.3',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/offlinevibe/env.io_sense_pi',
    author='FFLNVB',
    author_email='envio@offlinevibe.de',
    keywords='temperature, DB18B20',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4'
)