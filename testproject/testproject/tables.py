

from .models import Author, Book


def get_author_table_class(TableClass):

    class AuthorTable(TableClass):

        class Meta:
            model = Author
            attrs = {'class': 'table table-bordered table-striped table-condensed'}

    return AuthorTable


def get_book_table_class(TableClass):

    class BookTable(TableClass):

        column_default_show = ['id', 'title', 'author']

        class Meta:
            model = Book
            attrs = {'class': 'table table-bordered table-striped table-condensed'}

    return BookTable
