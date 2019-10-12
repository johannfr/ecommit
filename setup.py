from setuptools import setup, find_packages

setup(
    name='ecommit',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        ecommit=ecommit.cli:cli
    ''',
)
