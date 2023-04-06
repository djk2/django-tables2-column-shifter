django-tables2-column-shifter
------------------------------


.. image:: https://badge.fury.io/py/django-tables2-column-shifter.svg
    :target: https://badge.fury.io/py/django-tables2-column-shifter
    :alt: Latest PyPI version


.. image:: https://github.com/djk2/django-tables2-column-shifter/actions/workflows/tests.yaml/badge.svg?branch=master
    :target: https://github.com/djk2/django-tables2-column-shifter/actions/workflows/tests.yaml
    :alt: GitHub Actions


.. image:: https://requires.io/github/djk2/django-tables2-column-shifter/requirements.svg?branch=master
    :target: https://requires.io/github/djk2/django-tables2-column-shifter/requirements/?branch=master
    :alt: Requirements Status


**About the app:**
Simple extension for django-tables2 to dynamically show or hide columns using jQuery.
Application uses web storage to store information whih columns are visible or not.
Using JQuery, Bootstrap3 or Bootstrap4 or Bootstrap5 and Django >=1.9.


**Warning** : - Since version 2.0 my extension works by default with bootstrap4.
  I highly recommend to inherit explicite from tables class indicate on bootstrap version.
  I.e if you use in your project bootstrap in version 5.
  Your `Table` classes should inherit from:
  `django_tables2_column_shifter.tables.ColumnShiftTableBootstrap5`.

  Now you should inherit from:

  * for bootstrap2 - ColumnShiftTableBootstrap2,
  * for bootstrap3 - ColumnShiftTableBootstrap3,
  * for bootstrap4 - ColumnShiftTableBootstrap4,
  * for bootstrap5 - ColumnShiftTableBootstrap5,

**Tested by tox with:**

* Python :3.6, 3.8, 3.10
* Django : 1.9, 1.10, 1.11, 2.0, 2.1, 3.0, 3.1, 3.2, 4.0, 4.2, master
* django-tables2 : 1.15, ..., 1.21, 2.0, 2.1, 2.2, 2.3, 2.5, master

**Supported:**

* Django >= 1.9
* django-tables2 >= 1.15 (earlier version probably will work but wasn't tested)
* **bootstrap2** / **bootstrap3** / **bootstrap4** / **bootstrap4.1.3** / **bootstrap5 beta3**
* **JQuery**

**Supported locale:**

* EN        - (English)
* PL        - (Polish)
* EL        - (Greek / Hellenic Republic)
* PT-BR     - (Portuguese - Brazilian)


More information about django-tables in here: https://django-tables2.readthedocs.io/


Screens:
----------

.. image:: https://raw.githubusercontent.com/djk2/django-tables2-column-shifter/master/doc/static/scr1.png
    :alt: screen 1

.. image:: https://raw.githubusercontent.com/djk2/django-tables2-column-shifter/master/doc/static/scr2.png
    :alt: screen 2


How to Install:
---------------
1. Install django-tables2-column-shifter using::


        pip install django-tables2-column-shifter

    or

        pip install git+https://github.com/djk2/django-tables2-column-shifter

    or

        pip install django-tables2-column-shifter.zip

    or

        pip install django-tables2-column-shifter.tar.gz


2. Add ``django_tables2_column_shifter`` to your ``INSTALLED_APPS`` setting (after django_tables2) like this ::

    INSTALLED_APPS = [
        ...,
        'django_tables2',
        'django_tables2_column_shifter',
        ...,
    ]

3. Add path to js script: ``django_tables2_column_shifter.min.js`` in your base django template.
   Script must be add after jquery.js and bootstrap.js and before </body> tag.
   Draw attention to fact that beginning from version 4 of bootstrap,
   the `Popper.js` is required to proper work of some of JS bootstrap scripts.
   More about dependencies here:
   https://getbootstrap.com/docs/4.0/getting-started/javascript/#dependencies


  base.html::

    {% load static %}

    <body>
        ...
        ...
        <script src="{% static "jquery.min.js" %}"></script> {# require #}
        {# Popper is a dependency for bootstrap >= 4.0 #}
        <script src="{% static "bootstrap/js/popper.min.js" %}"></script>
        <script src="{% static "bootstrap/js/bootstrap.min.js" %}"></script>

        <script
            type="text/javascript"
            src="{% static "django_tables2_column_shifter/js/django_tables2_column_shifter.min.js" %}">
        </script>
    </body>


Usage:
------
To use app, you must inherit your table class from ``django_tables2_column_shifter.tables.ColumnShiftTable``

  models.py - create ordinary model::

    from django.db import models

    class MyModel(models.Model):
        first_name = models.CharField("First name", max_length=50)
        last_name = models.CharField("Last name", max_length=50)

  tables.py - change inherit to one of: ColumnShiftTableBootstrap2,
  ColumnShiftTableBootstrap3, ColumnShiftTableBootstrap4, ColumnShiftTableBootstrap5
  (depends on which bootstrap version of bootstrap you are using)::

    from django_tables2_column_shifter.tables import (
        ColumnShiftTableBootstrap2, # If you use bootstrap2
        ColumnShiftTableBootstrap3, # If you use bootstrap3
        ColumnShiftTableBootstrap4, # If you use bootstrap4
        ColumnShiftTableBootstrap5, # If you use bootstrap5
    )
    from app.models import MyModel

    # By default you probably inherit from django_table2.Table
    # Change inherit to ColumnShiftTableBootstrap4
    # if you use bootstrap4
    class MyModelTable(ColumnShiftTableBootstrap4):
        class Meta:
            model = MyModel

    # or if you use bootstrap5
    class MyModelTable(ColumnShiftTableBootstrap5):
        class Meta:
            model = MyModel


  views.py - In your view, nothing changes::

    from .tables import MyModelTable
    from .models import MyModel

    def simple_list(request):
        queryset = MyModel.objects.all()
        table = MyModelTable(queryset)
        return render(request, 'template.html', {'table': table})

  template.html - use default render_table tag to display table object (using bootstrap3 / bootstrap4 / bootstrap5)::

    {% extends "base.html" %}
    {% load django_tables2 %}
    {% render_table table %}



JS API:
-------
To retrieve the invisible columns you can use the ``$.django_tables2_column_shifter_hidden()`` js API.
You can either pass the 0-based index of the table in the page (i.e use ``$.django_tables2_column_shifter_hidden(1)``
to get the hidden columns for the 2nd table in the page) or just use it without parameters to retrieve the hidden columns
for the first table. This API returns an array with the invisible column names.

These columns can then be used when you want to export only the visible columns,
ie  when the user clicks on the export button it would append an ``&excluded_columns=col1,col2``
to the export button's ``href`` which would then be used by the django-tables2 ``TableExporter``
(http://django-tables2.readthedocs.io/en/latest/pages/export.html#excluding-columns) to exclude
these cols, i.e something like

    exporter = TableExport('csv', table, exclude_columns=self.request.GET.get('excluded_columns').split(',))



Bootstrap2 (support for old projects):
--------------------------------------
If you use Bootstrap v2 in your project then table class has to inherit from `ColumnShiftTableBootstrap2`
imported from `django_tables2_column_shifter.tables`.

Bootstrap3 (support for old projects):
--------------------------------------
If you use Bootstrap v3 in your project then table class has to inherit from `ColumnShiftTableBootstrap3`
imported from `django_tables2_column_shifter.tables`.

Bootstrap4 :
--------------------------------------
If you use Bootstrap v4 in your project then table class has to inherit from `ColumnShiftTableBootstrap4`
imported from `django_tables2_column_shifter.tables`.

Bootstrap5:
--------------------------------------
If you use Bootstrap v5 in your project then table class has to inherit from `ColumnShiftTableBootstrap5`
imported from `django_tables2_column_shifter.tables`.



Warnings:
----------

- **Warning** : - If you use {% render_table %} tag with queryset (not table class instance),
  django-tables2-column-shifter will not be work. Queryset does not have ``template`` attribute::

    {% load django_tables2 %}
    {% render_table queryset %} {# not work #}


- **Warning** : - If you use a different template than ``django_tables2_column_shifter/bootstrap*.html``
  to render your table, probably django-tables2-column-shifter will not be work.
  Your custom template should inherit from ``django_tables2_column_shifter/bootstrap*.html``

- **Warning** : - Since version 2.0 the default template is not used for Table class.
  Moreover template ``django_tables2_column_shifter/table.html`` by default inherit from
  ``django_tables2_column_shifter/bootstrap4.html``




Customizing:
-------------
1. If you use more then one instance of the same Table class, you should use a different prefix for each instance::

    tab1 = MyModelTable(queryset, prefix='tab1')
    tab2 = MyModelTable(queryset, prefix='tab2')
    tab3 = MyModelTable(queryset, prefix='tab3')

2. To disable shifter mechanism - set ``False`` to ``shift_table_column`` in your table class (default value is True)::

    class MyModelTable(ColumnShiftTableBootstrap5):
       shift_table_column = False
       ...


3. By default, all columns from sequence are visible, if you want limit visible columns,
   override method ``get_column_default_show(self)`` like that::

    class MyModelTable(ColumnShiftTableBootstrap5):
        def get_column_default_show(self):
            self.column_default_show = ['column1', 'column2']
            return super(MyModelTable, self).get_column_default_show()

4. By default, all columns from sequence are visible, if you want exclude some colmumns and
   block ability to manipulate then, use: ``column_excluded``

    class MyModelTable(ColumnShiftTableBootstrap5):
        column_excluded = ['ex_column1', 'ex_column2']

    or

    class MyModelTable(ColumnShiftTableBootstrap5):
        def get_column_excluded(self):
            self.column_excluded = ['ex_column1', 'ex_column2']
            return super(MyModelTable, self).get_column_excluded()


Run demo:
---------
1. Download or clone project from `https://github.com/djk2/django-tables2-column-shifter`::

    git clone https://github.com/djk2/django-tables2-column-shifter.git

2. Go to testproject directory::

    cd django-tables2-column-shifter/testproject

3. Install requirements::

    pip install -r requirements.txt

4. Run django developing server::

    python manage.py runserver


Links:
--------
- `Django documentation <https://docs.djangoproject.com/en/dev/>`_
- `django-tables2 documentation <https://django-tables2.readthedocs.io/en/latest/>`_
