import os

from setuptools import find_packages, setup

cwd = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(cwd, "README.md"), encoding="utf-8") as fd:
    LONG_DESCRIPTION = fd.read()

setup(
    #
    # Project Info
    #
    name="olive-sequencer-nifpga",
    version="1",
    description="Open LIVE microscopy",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/liuyenting/olive-core",
    classifiers=["License :: OSI Approved :: Apache Software License"],
    keywords=[],
    #
    # Author
    #
    author="Liu, Yen-Ting",
    author_email="ytliu@gate.sinica.edu.tw",
    #
    # Dependencies
    #
    # use pyproject.toml for setup dependencies instead
    # setup_requires=[],
    install_requires=[],
    #
    # Package Structure
    #
    packages=find_packages(),
    #
    # Build Instruction
    #
    # entry_points={"console_scripts": ["funniest-joke=funniest.command_line:main"]},
    zip_safe=False,
)

