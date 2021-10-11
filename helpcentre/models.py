from feedback.models import Author
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User

class Booking(models.Model): #move this to booking app later
    bid = models.CharField(max_length=100, unique=True)
    created_by = models.ForeignKey(Author,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.CharField(max_length=100, unique=True) # later remove this and connect to booking items model instead

    def __str__(self):
        return self.bid

    def save(self, *args, **kwargs):
        self.slug = slugify(self.bid)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('helpcentre:helpcentre_home', kwargs={'slug':self.slug})
    # add here redirect links args, kwargs


class Comment(models.Model):
    booking = models.ForeignKey(Booking,null=True, on_delete=models.CASCADE,related_name='comments')
    comm_name = models.CharField(max_length=100, blank=True)
    # reply = models.ForeignKey("Comment", null=True, blank=True, on_delete=models.CASCADE,related_name='replies') 
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    body = models.TextField(max_length=500) # change this to richtext field or more advanced html editor plugin
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.comm_name = slugify("comment by" + "-" + str(self.author) + str(self.date_added))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.comm_name

    class Meta:
        ordering = ['-date_added']

class Reply(models.Model):
    comment_name = models.ForeignKey(Comment, on_delete=models.CASCADE,related_name='replies')
    reply_body = models.TextField(max_length=500) # same here, change to rich text or other so users are able to format the text
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "reply to " + str(self.comment_name.comm_name)
