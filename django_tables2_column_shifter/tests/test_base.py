# encoding: utf-8
from os import path

import django
import django_tables2 as tables
from django.contrib.staticfiles import finders
from django.test import Client, TestCase, RequestFactory
from django.template import Template, Context

from django_tables2_column_shifter.tests.models import Author
from django_tables2_column_shifter.tables import (
    ColumnShiftTableBootstrap2,
    ColumnShiftTableBootstrap3,
    ColumnShiftTableBootstrap4,
    ColumnShiftTableBootstrap5,
)

if tuple(map(int, django.__version__.split(".")[:2])) >= (1, 10):
    from django.urls import reverse
else:
    from django.core.urlresolvers import reverse


class DjangoTables2ColumnShifterTest(TestCase):

    CASE = [
        {
            'bootstrap_version': 'bootstrap2',
            'min_dt_version': (1, 0),
            'max_dt_version': (2, 0),
            'template_name': 'django_tables2_column_shifter/bootstrap2.html',
            'table_clsss': ColumnShiftTableBootstrap2,
        },
        {
            'bootstrap_version': 'bootstrap3',
            'min_dt_version': (1, 0),
            'max_dt_version': (2, 0),
            'template_name': 'django_tables2_column_shifter/bootstrap3.html',
            'table_clsss': ColumnShiftTableBootstrap3,
        },
        {
            'bootstrap_version': 'bootstrap4',
            'min_dt_version': (2, 0),
            'max_dt_version': None,
            'template_name': 'django_tables2_column_shifter/bootstrap4.html',
            'table_clsss': ColumnShiftTableBootstrap4,
        },
        {
            'bootstrap_version': 'bootstrap5',
            'min_dt_version': (2, 0),
            'max_dt_version': None,
            'template_name': 'django_tables2_column_shifter/bootstrap5.html',
            'table_clsss': ColumnShiftTableBootstrap5,
        },
    ]

    dt_version = tuple(map(int, tables.__version__.split(".")[:2]))

    def setUp(self):
        # Add authors to database
        Author.objects.create(first_name='Bradley', last_name='Ayers', age=21)
        Author.objects.create(first_name='Haris', last_name='Scoot', age=22)
        Author.objects.create(first_name='Barbara', last_name='Cartland', age=23)

        # Create http client
        if not hasattr(self, 'client'):
            self.client = Client()

    def test_CASE_status(self):
        for case in self.CASE:
            if (
                (case['min_dt_version'] and case['min_dt_version'] > self.dt_version) or
                (case['max_dt_version'] and case['max_dt_version'] < self.dt_version)
            ):
                continue
            response = self.client.get(reverse(case['bootstrap_version']))
            assert response.status_code == 200

    def test_general_html_content(self):
        for case in self.CASE:
            if (
                (case['min_dt_version'] and case['min_dt_version'] > self.dt_version) or
                (case['max_dt_version'] and case['max_dt_version'] < self.dt_version)
            ):
                continue
            response = self.client.get(reverse(case['bootstrap_version']))
            self.assertContains(response, "Authors - table 1:")
            self.assertContains(response, "Authors - table 2:")
            self.assertContains(response, "Books - table")
            self.assertContains(response, "Books - queryset")

    def test_container_ids(self):
        for case in self.CASE:
            if (
                (case['min_dt_version'] and case['min_dt_version'] > self.dt_version) or
                (case['max_dt_version'] and case['max_dt_version'] < self.dt_version)
            ):
                continue
            response = self.client.get(reverse(case['bootstrap_version']))
            self.assertContains(response, 'id="AuthorTable"')
            self.assertContains(response, 'id="authors2AuthorTable"')
            self.assertContains(response, 'id="booksBookTable"')

    def test_tables_containers_count(self):
        for case in self.CASE:
            if (
                (case['min_dt_version'] and case['min_dt_version'] > self.dt_version) or
                (case['max_dt_version'] and case['max_dt_version'] < self.dt_version)
            ):
                continue
            response = self.client.get(reverse(case['bootstrap_version']))
            self.assertContains(response, "column-shifter-container", count=3)

    def test_buttons_count(self):
        for case in self.CASE:
            if (
                (case['min_dt_version'] and case['min_dt_version'] > self.dt_version) or
                (case['max_dt_version'] and case['max_dt_version'] < self.dt_version)
            ):
                continue
            response = self.client.get(reverse(case['bootstrap_version']))
            self.assertContains(response, "btn-shift-column", count=13)

    def test_btn_on_status_count(self):
        for case in self.CASE:
            if (
                (case['min_dt_version'] and case['min_dt_version'] > self.dt_version) or
                (case['max_dt_version'] and case['max_dt_version'] < self.dt_version)
            ):
                continue
            response = self.client.get(reverse(case['bootstrap_version']))
            self.assertContains(response, 'data-state="on"', count=11)

    def test_btn_off_status_count(self):
        for case in self.CASE:
            if (
                (case['min_dt_version'] and case['min_dt_version'] > self.dt_version) or
                (case['max_dt_version'] and case['max_dt_version'] < self.dt_version)
            ):
                continue
            response = self.client.get(reverse(case['bootstrap_version']))
            self.assertContains(response, 'data-state="off"', count=2)

    def test_is_pagination(self):
        for case in self.CASE:
            if (
                (case['min_dt_version'] and case['min_dt_version'] > self.dt_version) or
                (case['max_dt_version'] and case['max_dt_version'] < self.dt_version)
            ):
                continue
            response = self.client.get(reverse(case['bootstrap_version']))
            self.assertContains(response, "?page=2")
            self.assertContains(response, "authors2page")

    def test_tables_template(self):
        for case in self.CASE:
            if (
                (case['min_dt_version'] and case['min_dt_version'] > self.dt_version) or
                (case['max_dt_version'] and case['max_dt_version'] < self.dt_version)
            ):
                continue

            response = self.client.get(reverse(case["bootstrap_version"]))
            template_name = case['template_name']

            # In django_table2 v1.18 was renamed Table.Meta.template to template_name
            version = tuple(map(int, tables.__version__.split(".")[:2]))
            if version < (1, 18):
                template_attr_name = 'template'
            else:
                template_attr_name = 'template_name'

            assert getattr(response.context['author_table1'], template_attr_name) is not None
            assert getattr(response.context['author_table1'], template_attr_name) == template_name
            assert getattr(response.context['author_table2'], template_attr_name) is not None
            assert getattr(response.context['author_table2'], template_attr_name) == template_name
            assert getattr(response.context['book_table'], template_attr_name) is not None
            assert getattr(response.context['book_table'], template_attr_name) == template_name

    def test_static_files(self):
        prefix = "django_tables2_column_shifter"
        statics = [
            'js/django_tables2_column_shifter.min.js',
            'img/check.png',
            'img/uncheck.png',
            'img/cols.png',
            'img/loader.gif',
        ]

        for static in statics:
            static_path = path.join(prefix, static)
            abs_path = finders.find(static_path)
            assert abs_path is not None
            assert path.exists(abs_path) is True

    def test_column_excluded(self):
        """
        Check that excluded columns not render in tempalte
        """

        for case in self.CASE:

            if (
                (case['min_dt_version'] and case['min_dt_version'] > self.dt_version) or
                (case['max_dt_version'] and case['max_dt_version'] < self.dt_version)
            ):
                continue

            class Tab(case['table_clsss']):
                column_excluded = ["first_name", "last_name"]

                class Meta:
                    model = Author

            table = Tab(Author.objects.all())
            request = RequestFactory().get('/fake/url')
            template = Template("""
                {% load django_tables2 %}
                {% render_table table %}
            """)
            ctx = Context({"table": table, "request": request})
            render = template.render(ctx)

            self.assertTrue('data-td-class="id"' in render)
            self.assertTrue('data-td-class="age"' in render)
            self.assertFalse('data-td-class="first_name"' in render)
            self.assertFalse('data-td-class="last_name"' in render)
