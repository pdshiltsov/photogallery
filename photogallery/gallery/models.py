from django.db import models

class Album(models.Model):
    title = models.CharField(
        max_length=256, 
        verbose_name="название альбома"
    )


class Photo(models.Model):
    image = models.ImageField(
        upload_to="photos/",
        blank=True,
        null=False,
        verbose_name="картинка"
    )
    pub_date = models.DateTimeField("date published")
    description = models.CharField(
        max_length=256, 
        verbose_name="описание"
    )
    album = models.ForeignKey(
        Album, 
        on_delete=models.CASCADE
    )
