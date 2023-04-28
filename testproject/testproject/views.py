from django.views.generic import TemplateView
from django_tables2.config import RequestConfig

from django_tables2_column_shifter.tables import (
    ColumnShiftTableBootstrap2,
    ColumnShiftTableBootstrap3,
    ColumnShiftTableBootstrap4,
    ColumnShiftTableBootstrap4Responsive,
    ColumnShiftTableBootstrap5,
    ColumnShiftTableBootstrap5Responsive,
)

from .models import Author, Book
from .tables import get_author_table_class, get_book_table_class


class Index(TemplateView):
    template_name = "testproject/index.html"


class Base(object):
    container_css = "span10 offset1"
    template_name = "testproject/test_bootstrap2.html"
    table_class_version = ColumnShiftTableBootstrap2

    def get_context_data(self, **kwargs):
        context = super(Base, self).get_context_data(**kwargs)

        # Build tabels
        author_queryset = Author.objects.all()
        author_table1 = get_author_table_class(
            self.table_class_version
        )(author_queryset)
        author_table2 = get_author_table_class(
            self.table_class_version
        )(author_queryset, prefix="authors2")

        book_queryset = Book.objects.all()
        book_table = get_book_table_class(
            self.table_class_version
        )(book_queryset, prefix="books")

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
    pass


class Bootstrap3(Base, TemplateView):
    container_css = "col-xs-10 col-xs-offset-1"
    template_name = "testproject/test_bootstrap3.html"
    table_class_version = ColumnShiftTableBootstrap3


class Bootstrap4(Base, TemplateView):
    container_css = "col-xs-10 col-xs-offset-1"
    template_name = "testproject/test_bootstrap4.html"
    table_class_version = ColumnShiftTableBootstrap4


class Bootstrap4Responsive(Base, TemplateView):
    container_css = "col-xs-10 col-xs-offset-1"
    template_name = "testproject/test_bootstrap4.html"
    table_class_version = ColumnShiftTableBootstrap4Responsive


class Bootstrap4_1_3(Base, TemplateView):
    container_css = "col-xs-10 col-xs-offset-1"
    template_name = "testproject/test_bootstrap4.1.3.html"
    table_class_version = ColumnShiftTableBootstrap4


class Bootstrap5(Base, TemplateView):
    container_css = "col-xs-10 col-xs-offset-1"
    template_name = "testproject/test_bootstrap5.html"
    table_class_version = ColumnShiftTableBootstrap5


class Bootstrap5Responsive(Base, TemplateView):
    container_css = "col-xs-10 col-xs-offset-1"
    template_name = "testproject/test_bootstrap5.html"
    table_class_version = ColumnShiftTableBootstrap5Responsive
