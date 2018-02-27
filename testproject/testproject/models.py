from django.db import models


class Author(models.Model):
    first_name = models.CharField("First name", null=False, blank=False, max_length=50)
    last_name = models.CharField("Last name", null=False, blank=False, max_length=50)
    age = models.IntegerField("Age")

    def __str__(self):
        return "{fn} {ln}".format(fn=self.first_name, ln=self.last_name)


class Book(models.Model):
    title = models.CharField("Title", null=False, blank=False, max_length=120)
    form = models.CharField("Format", default="A5", max_length=10)
    pages = models.IntegerField("Count pages")

    # FK
    author = models.ForeignKey(
        Author,
        verbose_name='Author',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
