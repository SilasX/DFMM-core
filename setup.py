import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='DFMM-core',
    version='0.1',
    packages=['DFMM_core'],
    include_package_data=True,
    license='MIT License',
    description='The core API for Drucker-Flick Mental Math',
    long_description=README,
    url='http://github.com/SilasX/DFMM-core',
    author='Silas Barta',
    author_email='sbarta@gmail.com',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
