from setuptools import setup, find_packages

setup(
    name='oddiscovery',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'tldextract',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'oddiscovery = oddiscovery.main:run',
        ],
    },
)
