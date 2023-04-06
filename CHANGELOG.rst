CHANGELOG
===========

v. 2.1.0
--------

    * Add possibility to exclude columns from shifting via `column_excluded`
    * Support for Python 3.10
    * Support for Django 4.0
    * Support for Django 4.2
    * Support django-tables2 v2.5.3

v. 2.0.3
--------

    * Fix small gaps for documentation in README.rst file

v. 2.0.2
--------

    * Support for Django 3.2

v. 2.0.1
--------

    * Migrate tests from Travis to GitHub Actions + drop tests for Python v2.
      Stil, tests based on 'tox'.

v. 2.0.0
--------

    * Support for Django 3.1
    * Tests with django-tables2 v2.3
    * Add support for Bootstrap5 - issue #19
    * Add special classes `ColumnShiftTableBootstrap3`,
      `ColumnShiftTableBootstrap4` and `ColumnShiftTableBootstrap5`
    * Change default inherit for django_tables2_column_shifter/templtes/table.html
      from `django_tables2_column_shifter/bootstrap.html` to `django_tables2_column_shifter/bootstrap4.html`
      so class `ColumnShiftTable` by default call bootstrap4 template from django-tables2 - refere to issue #18
      **If you use different bootstrap version then 4 please use one of class: ColumnShiftTableBootstrap2/3/4/5 **

v. 0.5.2
--------

    * Add locale Brazilian Portuguese

v. 0.5.1
--------

    * Support Django 2.1
    * Support for bootstrap4.1.3 + example in testproject
    * Add API for retrieving non-visible columns by @spapas

v. 0.5.0
---------

    * Support for django-tables2 v2.0
    * Support for bootstrap2
    * Update README

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
