

from .models import Author, Book


def get_author_table_class(TableClass):

    class AuthorTable(TableClass):

        class Meta:
            model = Author
            attrs = {'class': 'table table-bordered table-striped table-condensed'}

        def __init__(self, *args, **kwargs):
            super(AuthorTable, self).__init__(*args, **kwargs)
            self.set_hideable_columns(['first_name', 'last_name', 'age'])

    return AuthorTable


def get_book_table_class(TableClass):

    class BookTable(TableClass):

        column_default_show = ['id', 'title', 'author']

        class Meta:
            model = Book
            attrs = {'class': 'table table-bordered table-striped table-condensed'}

    return BookTable
