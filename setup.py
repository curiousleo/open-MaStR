from setuptools import setup, find_packages
from os import path
import os

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='open_mastr',
    packages=find_packages(),
    version='0.1',
    description='MaStR data download tool',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/OpenEnergyPlatform/open-MaStR',
    # author='',  # Optional
    # author_email='',  # Optional

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: AGPL-3.0 License',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='>=3.6, <4',
    install_requires=[
        'pandas',
        'numpy',
        'sqlalchemy',
        'psycopg2-binary',
        "geoalchemy2",
        'zeep',
        "tqdm",
        "geopandas",
        "pyyaml",
        "requests",
        "keyring",
        'bokeh',
        # 'geoviews',
        'xmltodict',
        'pynodo',
    ],
    package_data = {
        "open_mastr": [os.path.join("soap_api", "config", "*.yml"),
                       os.path.join("soap_api", "metadata", "LICENSE")]
    },
    project_urls={
        'Bug Reports': 'https://github.com/OpenEnergyPlatform/open-MaStR/issues',
        'Source': 'https://github.com/OpenEnergyPlatform/open-MaStR',
    },
)

os.system("ulimit -n 1000000")
