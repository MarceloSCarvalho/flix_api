from django.db import models


NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('Brazil', 'Brasil'),
    ('Canadian', 'Canadá'),
    ('Australian', 'Austrália'),
    ('British', 'Britânica'),
    ('USA/Israeli','EUA/israelense'),
    ('Other', 'Outros')

)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name
