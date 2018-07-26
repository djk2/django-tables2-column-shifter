from django.views.generic import TemplateView
from django_tables2.config import RequestConfig

from .models import Author, Book
from .tables import (
    AuthorTable,
    AuthorTableBootstrap2,
    BookTable,
    BookTableBootstrap2,
)


class BootstrapDefault(TemplateView):
    template_name = "django_tables2_column_shifter_tests/index.html"
    author_table_class = AuthorTable
    book_table_class = BookTable

    def get_context_data(self, **kwargs):
        context = super(BootstrapDefault, self).get_context_data(**kwargs)

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

        context['author_table1'] = author_table1
        context['author_table2'] = author_table2
        context['book_table'] = book_table
        context['book_queryset'] = book_queryset
        return context


class Bootstrap2(BootstrapDefault):
    author_table_class = AuthorTableBootstrap2
    book_table_class = BookTableBootstrap2
