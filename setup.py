import os
import setuptools
from pip.req import parse_requirements
from pip.download import PipSession


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(
    name='steamfiles',
    version='0.0.1',
    url='https://github.com/leovp/steamfiles',
    license='MIT',

    author='Leonid Runyshkin',
    author_email='runyshkin@gmail.com',

    keywords='steam files parse appinfo vdf acf',
    description='',
    long_description=read('README.md'),

    include_package_data = True,
    package_data={'': ['README.md', 'LICENSE']},

    platforms=['any'],
    packages=setuptools.find_packages(exclude=['tests']),

    install_requires=[
        str(req.req) for req in parse_requirements('requirements.txt',
                                                    session=PipSession())
    ],

    tests_require=[
        str(req.req) for req in parse_requirements('requirements_test.txt',
                                                    session=PipSession())
    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)