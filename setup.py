from setuptools import setup

setup(name="pincer",
        version="1.0",
        description="In Silico PCR for Python3",
        url="https://github.com/Andre-Tan/Pincer",
        author="Andre Tan",
        author_email="andre.sutanto.91@gmail.com",
        license="GPL-3.0",
        packages=["pincer"],
        install_requires=["biopython"],
        test_suite="unittest.TestCase",
        tests_require=["unittest", "biopython"],
        scripts=["run_Pincer.py"],
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Natural Language :: English",
            "Programming Language :: Python :: 3 :: Only",
            "Topic :: Scientific/Engineering :: Bio-Informatics"
        ]
    )