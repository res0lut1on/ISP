from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter your book genre pidor!")

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)


class Language(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        return self.name
