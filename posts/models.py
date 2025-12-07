from django.db import models
from django.utils import timezone


class Post(models.Model):
    CATEGORY_CHOICES = [
        ('nature', 'Nature'),
        ('adventure', 'Adventure'),
        ('food', 'Food'),
        ('friends', 'Friends'),
        ('winter', 'Winter'),
        ('spring', 'Spring'),
        ('summer', 'Summer'),
        ('autumn', 'Autumn'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    image_url = models.URLField(
        blank=True, null=True, default='https://static.vecteezy.com/system/resources/thumbnails/024/654/096/small/fluffy-squirrel-munching-on-acorns-in-tree-generated-by-ai-free-photo.jpg')
    thumbnail_url = models.URLField(
        blank=True, null=True, default='https://static.vecteezy.com/system/resources/thumbnails/024/654/096/small/fluffy-squirrel-munching-on-acorns-in-tree-generated-by-ai-free-photo.jpg')
    published_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    author = models.CharField(max_length=100, default="Squirrel Rusty")
    user_id = models.IntegerField(default=1)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='nature'
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.published_at:
                self.published_at = timezone.now()
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
