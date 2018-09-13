# encoding: utf-8
from os import path

import django
import django_tables2 as tables
from django.contrib.staticfiles import finders
from django.test import Client, TestCase

from django_tables2_column_shifter.tests.models import Author

if tuple(map(int, django.__version__.split(".")[:2])) >= (1, 10):
    from django.urls import reverse
else:
    from django.core.urlresolvers import reverse


class DjangoTables2ColumnShifterTest(TestCase):

    def setUp(self):
        # Add authors to database
        Author.objects.create(first_name='Bradley', last_name='Ayers', age=21)
        Author.objects.create(first_name='Haris', last_name='Scoot', age=22)
        Author.objects.create(first_name='Barbara', last_name='Cartland', age=23)

        # Create http client
        if not hasattr(self, 'client'):
            self.client = Client()

    def test_status(self):
        response = self.client.get(reverse("bootstrap_default"))
        assert response.status_code == 200

    def test_bootstrap2_status(self):
        response = self.client.get(reverse("bootstrap2"))
        assert response.status_code == 200

    def test_general_html_content(self):
        response = self.client.get(reverse("bootstrap_default"))
        self.assertContains(response, "Authors - table 1:")
        self.assertContains(response, "Authors - table 2:")
        self.assertContains(response, "Books - table")
        self.assertContains(response, "Books - queryset")

    def test_bootstrap2_general_html_content(self):
        response = self.client.get(reverse("bootstrap2"))
        self.assertContains(response, "Authors - table 1:")
        self.assertContains(response, "Authors - table 2:")
        self.assertContains(response, "Books - table")
        self.assertContains(response, "Books - queryset")

    def test_container_ids(self):
        response = self.client.get(reverse("bootstrap_default"))
        self.assertContains(response, 'id="AuthorTable"')
        self.assertContains(response, 'id="authors2AuthorTable"')
        self.assertContains(response, 'id="booksBookTable"')

    def test_bootstrap2_container_ids(self):
        response = self.client.get(reverse("bootstrap2"))
        self.assertContains(response, "AuthorTableBootstrap2")
        self.assertContains(response, "authors2AuthorTableBootstrap2")
        self.assertContains(response, "booksBookTableBootstrap2")

    def test_tables_containers_count(self):
        response = self.client.get(reverse("bootstrap_default"))
        self.assertContains(response, "column-shifter-container", count=3)

    def test_buttons_count(self):
        response = self.client.get(reverse("bootstrap_default"))
        self.assertContains(response, "btn-shift-column", count=13)

    def test_btn_on_status_count(self):
        response = self.client.get(reverse("bootstrap_default"))
        self.assertContains(response, 'data-state="on"', count=11)

    def test_btn_off_status_count(self):
        response = self.client.get(reverse("bootstrap_default"))
        self.assertContains(response, 'data-state="off"', count=2)

    def test_is_pagination(self):
        response = self.client.get(reverse("bootstrap_default"))
        self.assertContains(response, "?page=2")
        self.assertContains(response, "authors2page")

    def test_tables_template(self):
        response = self.client.get(reverse("bootstrap_default"))
        template_name = "django_tables2_column_shifter/table.html"

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
