from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    parent_item = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name




