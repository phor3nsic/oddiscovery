from setuptools import setup, find_packages

setup(
    name='o365domscan',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'tldextract',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'o365domscan = o365domscan.main:run',
        ],
    },
)
