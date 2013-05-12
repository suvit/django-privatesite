# -*- coding: utf-8 -
#
# This file is part of django-privatesite released under the MIT license. 
# See the NOTICE for more information.

import os
import sys
from setuptools import setup, find_packages

from privatesite import VERSION

setup(
    name='django-privatesite',
    version=VERSION,
    description='Django custom admins',
    long_description=file(
        os.path.join(
            os.path.dirname(__file__),
            'README.md'
        )
    ).read(),
    author='Victor Safronovich',
    author_email='vsafronovich@gmail.com',
    license='MIT',
    url='http://github.com/suvit/django-privatesite',
    zip_safe=False,
    packages=find_packages(exclude=['docs', 'examples', 'tests']),
    install_requires=['django>=1.3',
                      'django-apptemplates>=0.0.1',
                     ],
    include_package_data=True,
)
