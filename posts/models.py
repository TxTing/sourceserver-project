from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to='images/')
    #icon = models.ImageField(upload_to='images/')
    likes_total = models.IntegerField(default=0)
    post_owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]
    def less_pub_date(self):
        return self.pub_date.strftime('%b %e %Y')
