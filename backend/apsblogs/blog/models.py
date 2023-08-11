from django.db import models

class blog(models.Model):
    category_choices = (
        ('general', 'General'),
        ('science', 'Science'),
        ('english', 'English'),
        ('maths', 'Maths'),
        ('sst', 'SST'),
        ('gaming', 'Gaming'),
        ('news', 'News'),
        ('announcements', 'Announcements'),
        ('sports', 'Sports'),
        ('cooking', 'Cooking'),
        ('lifestyle', 'Lifestyle'),
        ('news', 'News'),
    )
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    date = models.DateField()
    content = models.CharField(max_length=5000)
    thumbnail = models.ImageField(upload_to='blog/thumbnail')
    category = models.CharField(max_length=20, choices=category_choices, default='general')
    likes = models.IntegerField()

    def __str__(self):
        return self.title
class upload(models.Model):
    pass