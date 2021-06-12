from .models import Author, Book


def get_author_table_class(TableClassVersion):

    class AuthorTable(TableClassVersion):

        class Meta:
            model = Author

        def __init__(self, *args, **kwargs):
            super(AuthorTable, self).__init__(*args, **kwargs)
            self.set_hideable_columns(['first_name', 'last_name', 'age'])

    return AuthorTable


def get_book_table_class(TableClassVersion):

    class BookTable(TableClassVersion):
        column_default_show = ['id', 'title', 'author']

        class Meta:
            model = Book

    return BookTable
