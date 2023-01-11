# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="TAOS API",
    author_email="cli94@wisc.edu",
    url="",
    keywords=["Swagger", "TAOS API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    Accounting firms need to collect detailed information on a client’s tax situation to prepare return on the client’s behalf. They currently send PDFs (like a form) with their own questions to clients via email. Moreover, it requires clients printing out PDFs, writing answers using pen, scanning and sending them back. This approach is simple but yet insecure and requires a lot of repeated efforts. This doc proposes a design for digitalize this process and provide a simplified streamlined solution for both clients and the accounting firms. 
    """
)
