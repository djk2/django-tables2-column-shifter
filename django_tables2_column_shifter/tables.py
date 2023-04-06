import django_tables2 as tables


class ColumnShiftTable(tables.Table):

    # If button for shifting columns is visible
    shift_table_column = True

    # Which columns are visible by default
    column_default_show = None

    # List of columns to exclude from choice
    column_excluded = None

    # Shifter template for tabel inherit from django_table2/bootstrap.html
    shifter_template = "django_tables2_column_shifter/table.html"

    # Css class for dropdown button above table
    dropdown_button_css = "btn btn-default btn-xs"

    def __init__(self, *args, **kwargs):
        """Override init for set shifter template"""
        super(ColumnShiftTable, self).__init__(*args, **kwargs)
        # Override default template
        if hasattr(self, "template_name"):
            self.template_name = self.shifter_template
        else:
            self.template = self.shifter_template

    def get_column_default_show(self):
        """
        Returns the columns that are visible by default
        If self.column_default_show is None then
        # default visible columns will be return from sequence
        """
        return self.column_default_show or self.sequence

    def get_column_excluded(self):
        """
        Excluded columns are not shown on list to choice
        """
        return self.column_excluded or []

    @property
    def uniq_table_class_name(self):
        """Return unique name of table class
        using in template for container div id
        prefix in django_tables2 is always a string, can be empty or not
        """
        class_name = self.__class__.__name__
        prefix = self.prefix
        return "{pref}{cls}".format(pref=prefix, cls=class_name)

    @property
    def get_dropdown_button_css(self):
        """Return css class for dropdown button above table."""
        return self.dropdown_button_css

    def get_column_class_names(self, classes_set, bound_column):
        """
        Ovveriden method to save back compability.
        Add column names as css class to the attribute of table cells.
        This functionality was changed in django table2 >= 2.0.
        """
        cset = super(ColumnShiftTable, self).get_column_class_names(classes_set, bound_column)
        cset.add(bound_column.name)
        return cset


class ColumnShiftTableBootstrap2(ColumnShiftTable):
    """
    Table class compatible with bootstrap 2
    """
    dropdown_button_css = "btn btn-small"
    shifter_template = "django_tables2_column_shifter/bootstrap2.html"


class ColumnShiftTableBootstrap3(ColumnShiftTable):
    """
    Table class compatible with bootstrap 3
    """
    shifter_template = "django_tables2_column_shifter/bootstrap3.html"


class ColumnShiftTableBootstrap4(ColumnShiftTable):
    """
    Table class compatible with bootstrap 4
    """
    shifter_template = "django_tables2_column_shifter/bootstrap4.html"


class ColumnShiftTableBootstrap5(ColumnShiftTable):
    """
    Table class compatible with bootstrap 5
    """
    dropdown_button_css = "btn btn-light btn-sm"
    shifter_template = "django_tables2_column_shifter/bootstrap5.html"
