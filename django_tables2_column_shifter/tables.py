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
    def uniq_table_class_name(self):
        """Return unique name of table class
        using in template for container div id
        prefix in django_tables2 is always a string, can be empty or not
        """
        class_name = self.__class__.__name__
        prefix = self.prefix
        return "{pref}{cls}".format(pref=prefix, cls=class_name)
