from setuptools import find_packages, setup

__version__ = "0.1.0"

setup(
    name="spawningtool",
    description="Build order parser for SC2 replays",
    version=__version__,
    author="Kevin Leung",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Games/Entertainment",
        "Topic :: Games/Entertainment :: Real Time Strategy",
    ],
    entry_points={
        'console_scripts': [
            "spawningtool = spawningtool.main:main",
        ],
    },
    install_requires=[
        'argparse',
        'sc2reader>=0.5.0',
    ],
    packages=find_packages(),
)