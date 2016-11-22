# encoding: utf-8
from django.test import TestCase, Client
from django_tables2_column_shifter.tests.models import Author, Book


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
        self.assertContains(response, "Authors")
        self.assertContains(response, "Books - table")
        self.assertContains(response, "Books - queryset")

    def test_tables_containers_count(self):
        response = self.client.get('/')
        self.assertContains(response, "column-shifter-container", count=2)

    def test_buttons_count(self):
        response = self.client.get('/')
        self.assertContains(response, "btn-shift-column", count=9)

    def test_btn_on_status_count(self):
        response = self.client.get('/')
        self.assertContains(response, 'data-state="on"', count=7)

    def test_btn_off_status_count(self):
        response = self.client.get('/')
        self.assertContains(response, 'data-state="off"', count=2)

    def test_is_pagination(self):
        response = self.client.get('/')
        self.assertContains(response, "authorspage")

    def test_tables_template(self):
        response = self.client.get('/')
        template_name = "django_tables2_column_shifter/table.html"
        assert response.context['author_table'].template is not None
        assert response.context['author_table'].template == template_name
        assert response.context['book_table'].template is not None
        assert response.context['book_table'].template == template_name
