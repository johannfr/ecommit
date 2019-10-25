from setuptools import setup, find_packages

setup(
    name='git-ecommit',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        git-ecommit=ecommit.cli:cli
    ''',
)
