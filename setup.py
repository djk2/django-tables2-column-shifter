# encoding:utf-8
from setuptools import find_packages, setup

from django_tables2_column_shifter import __version__ as version


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='django-tables2-column-shifter',
    version=version,
    description='Extension for django_tables2 can dynamically show or hide columns',
    url='https://github.com/djk2/django-tables2-column-shifter',
    author='Grzegorz Tężycki',
    author_email='grzegorz.tezycki@gmail.com',
    long_description=readme(),
    license='BSD',
    packages=find_packages(exclude=['testproject', 'docs']),
    tests_require=['Django', 'django-tables2'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Django>=1.9', 'django-tables2>=1.5.0'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities',
    ],
    keywords='django_tables2 django columns',
)
