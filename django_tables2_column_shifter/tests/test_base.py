# encoding: utf-8
from django.test import TestCase, Client
from django_tables2_column_shifter.tests.models import Author


class DjangoTables2ColumnShifterTest(TestCase):

    def setUp(self):

        # Add authors to database
        Author.objects.create(first_name='Bradley', last_name='Ayers', age=21)
        Author.objects.create(first_name='Haris', last_name='Scoot', age=22)
        Author.objects.create(first_name='Barbara', last_name='Cartland', age=23)

        # Create http client
        if not hasattr(self, 'client'):
            self.client = Client()

    def test_fake(self):
        self.assertTrue(1 == 1)

    def test_status(self):
        response = self.client.get('/')
        assert response.status_code == 200

    def test_general_html_content(self):
        response = self.client.get('/')
        self.assertContains(response, "Authors - table 1:")
        self.assertContains(response, "Authors - table 2:")
        self.assertContains(response, "Books - table")
        self.assertContains(response, "Books - queryset")

    def test_container_ids(self):
        response = self.client.get('/')
        self.assertContains(response, "AuthorTable")
        self.assertContains(response, "authors2AuthorTable")
        self.assertContains(response, "booksBookTable")

    def test_tables_containers_count(self):
        response = self.client.get('/')
        self.assertContains(response, "column-shifter-container", count=3)

    def test_buttons_count(self):
        response = self.client.get('/')
        self.assertContains(response, "btn-shift-column", count=13)

    def test_btn_on_status_count(self):
        response = self.client.get('/')
        self.assertContains(response, 'data-state="on"', count=11)

    def test_btn_off_status_count(self):
        response = self.client.get('/')
        self.assertContains(response, 'data-state="off"', count=2)

    def test_is_pagination(self):
        response = self.client.get('/')
        self.assertContains(response, "?page=2")
        self.assertContains(response, "authors2page")

    def test_tables_template(self):
        response = self.client.get('/')
        template_name = "django_tables2_column_shifter/table.html"
        assert response.context['author_table1'].template is not None
        assert response.context['author_table1'].template == template_name

        assert response.context['author_table2'].template is not None
        assert response.context['author_table2'].template == template_name

        assert response.context['book_table'].template is not None
        assert response.context['book_table'].template == template_name
