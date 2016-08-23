# -*- coding: UTF-8 -*-
from setuptools import setup


authors = [
    'João André <joao.andre@axado.com.br>',
    'Fabio Menegazzo <fabio.menegazzo@axado.com.br>',
]

setup(
    name='ojson',
    version='0.1.0',
    packages=['ojson'],

    # metadata for upload to PyPI
    author=', '.join(authors),
    description='Keep your JSON structure as it is',
    long_description=open('README.rst').read(),
    license='MIT',
    keywords='json ordered dict',
    url='https://github.com/joaoandrepsilva/ojson',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
