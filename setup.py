from setuptools import setup
import pincer

with open("README.md", "r") as f:
    long_description = f.read()

setup(name =pincer.__name__,
        version = pincer.__version__,
        description = pincer.__description__,
        long_description = long_description,
        url = pincer.__url__,
        author = pincer.__author__,
        author_email = pincer.__email__,
        license = pincer.__license__,
        packages = ["pincer"],
        zip_safe = False,
        install_requires = ["biopython"],
        test_suite = "nose.collector",
        tests_require = ["nose"],
        scripts = ["bin/pincer"],
        classifiers = [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Natural Language :: English",
            "Programming Language :: Python :: 3 :: Only",
            "Topic :: Scientific/Engineering :: Bio-Informatics"
        ]
    )