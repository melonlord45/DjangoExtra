from django.db import models


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class Category(TimeStamp):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Label(TimeStamp):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Priority(models.TextChoices):
    LOWEST = "lowest", "Lowest"
    LOW = "low", "Low"
    MEDIUM = "medium", "Medium"
    HIGH = "high", "High"
    HIGHEST = "highest", "Highest"


class Task(TimeStamp):
    name = models.CharField(max_length=255)
    description = models.TextField(
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="todoimg/",
        blank=True,
        null=True,
    )
    task_time = models.DateField(
        blank=True,
        null=True,
    )
    priority = models.CharField(
        max_length=100,
        choices=Priority.choices,
        default=Priority.LOWEST,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    labels = models.ManyToManyField(
        Label,
        blank=True,
    )
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.name
