from setuptools import setup, find_packages
from io import open
from os import path

here = path.abspath(path.dirname(__file__))

# long description from the README file

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pytiming',
    version='1.0.0',
    description=(
          'A Python module for timing your python scripts execution time'
    ),
    long_description=long_description,
    license='MIT',
    url='https://github.com/CITGuru/PyTiming/',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: '
        'Libraries :: Application Frameworks',
    ],
    keywords='timing, python, timer, time, timeit, pytimer, pytiming',
    include_package_data=True,
    author='Oyetoke Toby',
    download_url='https://github.com/CITGuru/PyTiming/archive/1.0.0.tar.gz',
    author_email='oyetoketoby80@gmail.com',
)
