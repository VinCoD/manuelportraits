from django.db import models

# Create your models here.


class Gallery(models.Model):
    # uploaded_by = models.ForeignKey(Client, on_delete=models.CASCADE)
    photos = models.ImageField(upload_to='photos', default='default.png')
    gallery_name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    caption = models.TextField(max_length=200)

    class Meta:
        verbose_name_plural = "Galleries"

    def __str__(self):
        return self.gallery_name
