from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(name="pincer",
        version="1.0",
        description="In Silico PCR for Python3",
        long_description=long_description,
        url="https://github.com/Andre-Tan/Pincer",
        author="Andre Tan",
        author_email="andre.sutanto.91@gmail.com",
        license="GPL-3.0",
        packages=["pincer"],
        zip_safe=False,
        install_requires=["biopython"],
        test_suite="nose.collector",
        tests_require=["nose"],
        scripts=["bin/pincer"],
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Natural Language :: English",
            "Programming Language :: Python :: 3 :: Only",
            "Topic :: Scientific/Engineering :: Bio-Informatics"
        ]
    )