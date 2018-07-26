from django.views.generic import TemplateView
from django_tables2.config import RequestConfig

from .models import Author, Book
from .tables import AuthorTable, BookTable


class Index(TemplateView):
    template_name = "testproject/index.html"


class Base(object):

    container_css = ""
    author_table_class = AuthorTable
    book_table_class = BookTable

    def get_context_data(self, **kwargs):
        context = super(Base, self).get_context_data(**kwargs)

        # Build tabels
        author_queryset = Author.objects.all()
        author_table1 = self.author_table_class(author_queryset)
        author_table2 = self.author_table_class(author_queryset, prefix="authors2")

        book_queryset = Book.objects.all()
        book_table = self.book_table_class(book_queryset, prefix="books")

        # Turn on sorting and pagination
        RequestConfig(self.request, paginate={'per_page': 2}).configure(author_table1)
        RequestConfig(self.request, paginate={'per_page': 2}).configure(author_table2)
        RequestConfig(self.request, paginate={'per_page': 2}).configure(book_table)

        context['container_css'] = self.container_css
        context['author_table1'] = author_table1
        context['author_table2'] = author_table2
        context['book_table'] = book_table
        context['book_queryset'] = book_queryset
        return context


class Bootstrap2(Base, TemplateView):
    container_css = "span10 offset1"
    template_name = "testproject/test_bootstrap2.html"


class Bootstrap3(Base, TemplateView):
    container_css = "col-xs-10 col-xs-offset-1"
    template_name = "testproject/test_bootstrap3.html"


class Bootstrap4(Base, TemplateView):
    container_css = "col-xs-10 col-xs-offset-1"
    template_name = "testproject/test_bootstrap4.html"
