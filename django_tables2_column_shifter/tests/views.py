from django.views.generic import TemplateView
from django_tables2.config import RequestConfig
from .models import Author, Book
from .tables import AuthorTable, BookTable


class Index(TemplateView):
    template_name = "django_tables2_column_shifter_tests/index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        # Build tabels
        author_table = AuthorTable(Author.objects.all(), prefix="authors")
        book_queryset = Book.objects.all()
        book_table = BookTable(book_queryset, prefix="books")

        # Turn on sorting and pagination
        RequestConfig(self.request, paginate={'per_page': 2}).configure(author_table)
        RequestConfig(self.request, paginate={'per_page': 2}).configure(book_table)

        context['author_table'] = author_table
        context['book_table'] = book_table
        context['book_queryset'] = book_queryset
        return context
