from setuptools import find_packages, setup
from os.path import dirname, join

with open(join(dirname(__file__), 'README.rst')) as f:
    long_desc = f.read()

setup(
    name='setup-freeze',
    version='0.1.0',
    description='Freezes the install_requires in your setup.py',
    long_description=long_desc,
    url='https://gitlab.com/abre/setup-freeze',
    author='Adam Brenecki',
    author_email='adam@brenecki.id.au',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    keywords='setup.py setuptools development',
    py_modules=['setup_freeze'],
    entry_points={
        'console_scripts': ['setup-freeze=setup_freeze:main'],
    }
)
