from django_tables2_column_shifter.tables import ColumnShiftTable

from .models import Author, Book


class AuthorTable(ColumnShiftTable):

    class Meta:
        model = Author


class BookTable(ColumnShiftTable):

    column_default_show = ['id', 'title', 'author']

    class Meta:
        model = Book
