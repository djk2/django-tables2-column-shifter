from django_tables2_column_shifter.tables import (
    ColumnShiftTable,
    ColumnShiftTableBootstrap2,
)

from .models import Author, Book


class AuthorTable(ColumnShiftTable):

    class Meta:
        model = Author


class BookTable(ColumnShiftTable):
    column_default_show = ['id', 'title', 'author']

    class Meta:
        model = Book


class AuthorTableBootstrap2(ColumnShiftTableBootstrap2):

    class Meta:
        model = Author


class BookTableBootstrap2(ColumnShiftTableBootstrap2):
    column_default_show = ['id', 'title', 'author']

    class Meta:
        model = Book
