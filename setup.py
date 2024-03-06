from setuptools import setup, find_packages

setup(
    name='datamug',
    version='0.0.1',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
