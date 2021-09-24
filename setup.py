#!/usr/bin/env python3
"""
Python reference API for the Europeean Materials & Modelling Ontology (EMMO).
"""
from glob import glob
from pathlib import Path
import re
import setuptools


rootdir = Path(__file__).parent


# Read long description from README.md file replacing local references to
# full URLs to support PyPI/external linking.
baseurl = 'https://raw.githubusercontent.com/emmo-repo/EMMO-python/master/'
long_description = re.sub(
    r'(\[[^]]+\])\(([^:)]+)\)', fr'\1({baseurl}\2)',
    Path(rootdir / 'README.md').read_text()
)

# Retrieve emmo-package version
for line in (rootdir / 'ontopy' / '__init__.py').read_text().splitlines(keepends=False):
    match = re.match(r"__version__ = '(?P<version>.*)'", line)
    if match is not None:
        VERSION = match.group("version")
        break
else:
    raise RuntimeError(
        f'Could not determine package version from ontopy/__init__.py !')


setuptools.setup(
    name='EMMOntoPy',
    version=VERSION,
    author='Jesper Friis, Francesca Lønstad Bleken, Bjørn Tore Løvfall',
    author_email='jesper.friis@sintef.no',
    description=('Python reference API for the Europeean Materials & '
                 'Modelling Ontology'),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/emmo-repo/EMMO-python',
    license='BSD',
    python_requires='>=3.6.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=(rootdir / "requirements.txt").read_text().splitlines(keepends=False),
    packages=setuptools.find_packages(),
    scripts=['tools/ontodoc',
             'tools/ontograph',
             'tools/emmocheck',
             'tools/ontoconvert',
             'tools/ontoversion'],
    package_data={
        'ontopy.factpluspluswrapper.java.lib.so': ['*'],
        'ontopy.factpluspluswrapper.java.lib.jars': ['*.jar'],
        'ontopy.factpluspluswrapper.java': ['pom.xml'],
    },
    include_package_data=True,
    data_files=[
        ('share/EMMO-python', ['README.md', 'LICENSE.txt']),
        (
            'share/EMMO-python/examples/emmodoc',
            glob('examples/emmodoc/*.md') +
            glob('examples/emmodoc/*.yaml') +
            glob('examples/emmodoc/pandoc-*'),
        ),
        (
            'share/EMMO-python/examples/emmodoc/figs',
            [str(_.relative_to(rootdir)) for _ in rootdir.glob('examples/emmodoc/figs/*') if _.is_file()],
        ),
        ('share/EMMO-python/demo', [str(_.relative_to(rootdir)) for _ in rootdir.rglob('demo/**') if _.is_file()]),
    ],
)
