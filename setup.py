# coding=utf-8
'''DM: a deep learning experimentation toolbox
'''
from codecs import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line]

extra_requirements = {}

tensorflow_gpu = 'tensorflow-gpu'
for req in requirements:
    if req.startswith('tensorflow'):
        tensorflow_gpu = req.replace('tensorflow', 'tensorflow-gpu')
extra_requirements['gpu'] = [tensorflow_gpu]

setup(
    name='dm',

    version='0.2.1.2',

    description='A deep learning experimentation toolbox',
    # long_description=long_description,
    # long_description_content_type='text/markdown',

    url='https://whyte.biz',

    author='Gavin Whyte',
    author_email='gavin@whyte.biz',

    license='Apache 2.0',

    keywords='deskminder deep learning deep_learning machine machine_learning natural language processing computer vision',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    python_requires='>=3',

    include_package_data=True,
    package_data={'deskminder': ['etc/*', 'examples/*.py']},

    install_requires=requirements,
    extras_require=extra_requirements,

    entry_points={
        'console_scripts': [
            'dm=deskminder.cli:main'
        ]
    }
)
