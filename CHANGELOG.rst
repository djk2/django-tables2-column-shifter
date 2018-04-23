CHANGELOG
===========

v. 0.4.1
---------

    * Add greek translation
    * Fix small css bug

v. 0.4.0
---------
    * Support for django-tables2 v1.19.0 and all previous versions
    * Remove support for django-tables2 < v1.5.0


v. 0.3.1
---------
    * Support for django-tables2 v1.5 and v1.6
    * Update requirements
    * PEP8


v. 0.3.0
--------
    * Remove ColumnShiftTable from __init__.py,
      Now you must import ColumnShiftTable not from django_tables2_column_shifter but
      django_tables2_column_shifter.tables

    * Support for bootstrap4
    * Reorganize templates for ColumnShiftTable
    * Add bootstrap4 support to testproject.
    * Less environments in tox- tests only for last minor django-tables2 versions
    * Replace glyphicons via inside images from static.
    * Sort imports by isort.

v. 0.2.2
--------

    * Tests + support for Django 1.11, Django 2.0

v. 0.2.1
--------

    * Upgrade django_tables2 to 1.2.9 + tests

v. 0.2
-------

    * Tests and check compability for: django-tables2 v1.2.7 + Django 1.10.4


v. 0.1
-------

    * Create app
