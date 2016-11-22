from .models import Author, Book
from django_tables2_column_shifter import ColumnShiftTable


class AuthorTable(ColumnShiftTable):

    class Meta:
        model = Author


class BookTable(ColumnShiftTable):

    column_default_show = ['id', 'title', 'author']

    class Meta:
        model = Book
