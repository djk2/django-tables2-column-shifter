import django_tables2 as tables


class ColumnShiftTable(tables.Table):

    # If button for shifting columns is visible
    shift_table_column = True

    # Which columns are visible by default
    column_default_show = None

    # Shifter template for tabel inherit from django_table2/bootstrap.html
    shifter_template = "django_tables2_column_shifter/table.html"

    def __init__(self, *args, **kwargs):
        """Override init for set shifter template"""
        super(ColumnShiftTable, self).__init__(*args, **kwargs)
        # Override default template
        self.template = self.shifter_template

    def get_column_default_show(self):
        """
        Returns the columns that are visible by default
        If self.column_default_show is None then
        # default visible columns will be return from sequence
        """
        if self.column_default_show is None:
            return self.sequence
        else:
            return self.column_default_show

    @property
    def table_class_name(self):
        """Return name of table class
        using in template for container div id"""
        return self.__class__.__name__
