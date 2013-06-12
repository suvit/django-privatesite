# -*- coding: utf-8 -
#
# This file is part of django-privatesite released under the MIT license. 
# See the LICENSE for more information.

from setuptools import setup, find_packages

setup(
    name='django-privatesite',
    version=__import__('privatesite').VERSION,
    description='Django custom admins',
    long_description=open('README.md').read(),
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
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Environment :: Web Environment',
        'Topic :: Software Development',
    ]
)
