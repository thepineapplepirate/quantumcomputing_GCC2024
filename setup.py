import sys

import setuptools

from qufold import __version__, TOOL_ID

if sys.version_info[0] < 3 or (sys.version_info[0] == 3 and sys.version_info[1] < 6):
    sys.exit(
        "{} requires Python 3.6 or higher. Your current Python version is {}.{}.{}\n".format(
            TOOL_ID, sys.version_info[0], sys.version_info[1], sys.version_info[2]
        )
    )

setuptools.setup(
    author="Bryan Raubenolt",
    author_email="raubenb@ccf.org",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    description="A basic repo for protein folding with quantum computers",
    download_url="https://github.com/thepineapplepirate/quantumcomputing_GCC2024",
    keywords=[
        "bioinformatics",
        "chemistry",
        "pdb",
        "proteins",
        "qiskit",
        "quantum"
    ],
    license="MIT",
    license_files=["LICENSE"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    name=TOOL_ID,
    packages=setuptools.find_packages(),
    project_urls={
        "Issues": "https://github.com/thepineapplepirate/quantumcomputing_GCC2024/issues",
        "Source": "https://github.com/thepineapplepirate/quantumcomputing_GCC2024",
    },
    python_requires=">=3.6",
    url="https://github.com/thepineapplepirate/quantumcomputing_GCC2024",
    version=__version__,
    zip_safe=False,
)
